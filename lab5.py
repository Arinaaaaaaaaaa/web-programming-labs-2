from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2


lab5 = Blueprint('lab5', __name__)

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