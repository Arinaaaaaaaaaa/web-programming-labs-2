from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2


lab5 = Blueprint('lab5', __name__)

# Прописываем параметры подключения к БД
def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="admin_knowledge_base",
        password="123")
    return conn

def dbClose(cursor, connection):
    # Закрываем курсор и соединение. Порядок важен!
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def lab_pages():
    return render_template('lab5.html')

@lab5.route('/lab5_1')
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return "go to console"

@lab5.route('/lab5/result')
def main_1():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return render_template('result.html', result=result)


@lab5.route('/lab5/main_page')
def main_page():
    username = session.get('username1')
    return render_template('main_page.html', username=username)



@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerPage():
    errors = []

    if request.method == "GET":
        return render_template('register.html', errors=errors)


    # Если мы попали сюда, значит метод POST, т.к. GET мы уже обработали и сделали return.
    # После return функция немедленно завершается
    username = request.form.get("username")
    password = request.form.get("password")


    # Проверяем username и password на пустоту. Если любой из них пустой, то добавляем ошибку и рендерим шаблон
    if not (username and password):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)


    # Получаем пароль от пользователя, хэшируем его
    hashPassword = generate_password_hash(password)
    # Если мы попали сюда, значит username и password заполнены, подключаемся к БД
    conn = dbConnect()
    cur = conn.cursor()


    # Проверяем наличие клиента в базе
    # У нас не может быть 2 пользователей с одинаковыми логинами
    # Используем параметры в запросе, чтобы избежать SQL-инъекций
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cur.fetchone()


    if existing_user:
        errors.append("Пользователь с данным именем уже существует")
        conn.close()
        cur.close()
        return render_template('register.html', errors=errors)


    # Если мы попали сюда, значит в cur.fetchone нет ни одной строки, значит пользователя с таким же логином не существует
    # Сохраняем пароль в виде хэша в БД
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))


    # Делаем commit, т.е. фиксируем изменения
    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/login_5")



@lab5.route('/lab5/login_5', methods=["GET", "POST"])
def loginPage():
    errors = []

    if request.method == "GET":
        return render_template("login_5.html", errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login_5.html", errors=errors)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("login_5.html", errors=errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        
        session['id'] = userID
        session['username1'] = username
        dbClose(cur, conn)
        return redirect("/lab5/main_page")

    else:
        errors.append("Неправильный логин или пароль")
        return render_template("login_5.html", errors=errors)


@lab5.route("/lab5/new_article", methods=["GET", "POST"])
def createArticle():
    errors = []

    # Проверяем авторизован ли пользователь
    # Мы читаем из JWT токена (session.get) ID пользователя
    userID = session.get("id")
    username = session.get('username1')

    if userID is not None:
        # Пользователь авторизован, мы прочитали jwt-токен
        # Проверили его валидность. Получили его id
        if request.method == "GET":
            return render_template("new_article.html", username=username)

        if request.method == "POST":
            article_text = request.form.get("article_text")
            title = request.form.get("title_article")

            if len(article_text) == 0:
                errors.append("Заполните текст")
                return render_template("new_article.html", errors=errors, username=username)
        
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id", (userID, title, article_text))
        # Получаем ID от вновь созданной записи
        # В нашем случае мы будем получать статьи следующим образом
        # /lab5/article/id_article
            new_article_id = cur.fetchone()[0]
            conn.commit()

        # Делаем Рудирект на новую статью
        # Пока этот роут не сделан, будет ошибка
        # Чтобы получить статью под номером 5, необходимо ввести в роут /lab5/article/5

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_article_id}")

# Пользователь не авторизован, отправить на страницу логина
    return redirect("/lab5/login_5")



# SQL injectino!!!!

# Конструкция /<string:article_id> позволяет нам получить это значение в роуте 
# параметр к функции getArticle, как показано ниже

# Например, если /lab5/articles/123, то article_id = '123'

@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):

    userID = session.get("id")
    username = session.get("username1")

    # Пользователь авторизован ли пользователь
    if userID is not None:    
        conn = dbConnect()
        cur = conn.cursor()

    # SQL injection example!!!
    cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

    # Возьми одну строку
    articleBody = cur.fetchone()

    dbClose(cur, conn)

    if  articleBody is None:
        return "Not found!"

    # Разбиваем строку на массив по "Enter", чтобы с помощью цикла for в jinja разбить статью на параграфы
    text = articleBody[1].splitlines()

    return render_template("articlescheck.html", article_text=text, article_title=articleBody[0], username = username)



@lab5.route('/lab5/articles')
def list_articles():
    userID = session.get('id')
    username = session.get("username1")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT id, title FROM articles WHERE user_id = %s;", (userID,))
        articles_data = cur.fetchall()

        articles = [{'id': row[0], 'title': row[1]} for row in articles_data]

        dbClose(cur, conn)

        return render_template('articles.html', articles=articles, username=username)

    return redirect("/lab5/login_5")


@lab5.route('/lab5/logout')
def logout():
    session.clear()
    return render_template('main_page.html')