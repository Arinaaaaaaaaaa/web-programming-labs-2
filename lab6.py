from flask import Blueprint, render_template, request, redirect
from Db import db
#Данные объекты представляют из себя таблицы users и articles в БД
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user


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


