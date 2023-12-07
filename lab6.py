from flask import Blueprint, render_template, request, redirect, session
from Db import db
#Данные объекты представляют из себя таблицы users и articles в БД
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user


lab6 = Blueprint('lab6', __name__)


@lab6.route('/lab6/')
def lab6_pages():
    return render_template('lab6.html')


@lab6.route("/lab6/check")
def main():
    #Тоже самое, что slect * from users
    my_users = users.query.all()
    print(my_users)
    return "result in console!"


@lab6.route("/lab6/checkarticles")
def mainart():
    my_articles = articles.query.all()
    for article in my_articles:
        print(f"{article.title}-{article.article_text}")
    return "Result in console!"


@lab6.route('/lab6/menu')
def lab6_menu():
    username_form = session.get('username')
    return render_template('menu_6.html', username = username_form)


@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register_6.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    #Проверяем существование пользователя в БД с таким же именем 
    #Если такого пользователя нет, то в isUserExist вернется None, т.e. мы можем интерпретировать это как False

    #select * from users
    #WHERE username = username_form
    #LIMIT 1
    #где username_form - это имя, которое мы получили из формы
    isUserExist = users.query.filter_by(username = username_form).first()
    errors = []
    if isUserExist is not None:
        errors.append("Такой пользователь уже существует!")
        return render_template("register_6.html", errors = errors)
    elif not username_form:
        errors.append("Введите имя пользователя!")
        return render_template("register_6.html", errors=errors)
    elif len(password_form) < 5:
        errors.append("Пароль должен содержать не менее 5 символов!")
        return render_template("register_6.html", errors=errors)

    #Хэшируем пароль
    hashedPswd = generate_password_hash(password_form, method="pbkdf2")
    #Создаем объект users с нужными полями
    newUser = users(username = username_form, password = hashedPswd)

    #Это INSERT
    db.session.add(newUser)
    #Тоже самое, что и conn.commit()
    db.session.commit()

    #Перенаправляем на страницу логина
    return redirect("/lab6/login")


@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_6.html")

    errors = []

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    my_user = users.query.filter_by(username = username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            #Сохраняем JWT токен
            login_user(my_user, remember=False)
            return redirect("/lab6/articles")

    if not (username_form or password_form):
        errors.append("Введите имя пользователя и пароль!")
        return render_template("login_6.html", errors = errors)
    elif my_user is None:
        errors.append("Такого пользователя не существует! Зарегестрируйтесь!")
        return render_template("login_6.html", errors = errors)
    elif my_user is not check_password_hash(my_user.password, password_form):
        errors.append("Введите правильный пароль!")
        return render_template("login_6.html", errors = errors)
    elif my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect("/lab6/articles")

    return render_template("login_6.html")


#login_required - авторизация обязательна, если пользователь не авторизован, то перенаправить
#на страницу lab6/login (lab6/login мы указывали в app.pу)

#Функцию login_required и переменнyю current_user мы импортировали ранее из Flask-Login
@lab6.route('/lab6/articles', methods = ['GET', 'POST'])
@login_required
def articles_list():
    username_form = request.form.get('username')
    my_articles = articles.query.filter((articles.user_id == current_user.id) | (articles.is_public == True)).order_by(articles.is_favorite.desc()).all()
    print(my_articles)
    return render_template('articles_6.html', articles=my_articles, username_form = username_form)


@lab6.route("/lab6/newarticle", methods=["GET", "POST"])
@login_required
def createArticle():
    if request.method == "GET":
        return render_template("new_article_6.html")
    if request.method == "POST":
        article_text = request.form.get("article_text")
        title = request.form.get("article_title")
        if len(article_text) == 0 or title is None:
            errors = ["Заполните текст и заголовок"]
            return render_template("new_article_6.html", errors=errors)
        new_article = articles(user_id=current_user.id, title=title, article_text=article_text)

        db.session.add(new_article)
        db.session.commit()

        return redirect("/lab6/articles")


@lab6.route("/lab6/articles/<int:article_id>", methods=['GET', 'POST'])
def getArticle(article_id):
    if current_user.is_authenticated:
        if request.method == 'POST':
            article = articles.query.filter_by(id=article_id).first()
        article = articles.query.filter_by(id=article_id).first()
        if article:
            if article.user_id == current_user.id or article.is_public:
                text = article.article_text.splitlines()
                return render_template("articlescheck_6.html", article_text=text, article_title=article.title, username=current_user.username)

    return redirect("/lab6/articles")


@lab6.route('/lab6/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab6/menu')