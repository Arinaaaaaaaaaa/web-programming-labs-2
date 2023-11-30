from flask import Blueprint, render_template, request, redirect
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
  #Закрываем курсор и соединение. Порядок важен!
  cursor.close()
  connection.close()


@lab5.route('/lab5/')
def lab_pages():
  return render_template('lab5.html')


@lab5.route('/lab5/result')
def main():
  conn = dbConnect()
  cur = conn.cursor()

  cur.execute("SELECT * FROM users;")

  result = cur.fetchall()

  print(result)

  dbClose(cur, conn)

  return render_template('result.html', result=result)


@lab5.route("/lab5/main_page")
def main_page():
  visibleUser = "Anon"
  return render_template('main_page.html', username=visibleUser)


@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerPage():
  errors = []

  if request.method == "GET":
      return render_template('register.html', errors=errors)

  #Если мы попали сюда, значит метод POST, т.к. GET мы уже обработали и сделали return.
  #После return функция немедленно завершается
  username = request.form.get("username")
  password = request.form.get("password")

  #Проверяем username и password на пустоту. Если любой из них путой, то добавляем ошибку и рендерим шаблон
  if not (username or password):
    errors.append("Пожалуйста заполните все поля")
    print(errors)
    return render_template('register.html', errors=errors)

  #Если мы попали сюда, значит username и password заполнены, подключаемся к БД
  conn = dbConnect()
  cur = conn.cursor()

  #Проверяем наличие клиента в базе
  #У нас не может быть 2 пользователя с одинаковыми логинами
  #Используем какие-то f-строки, что не рекомендуетмя делать
  cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

#fetchone, a отличие, от fetchall, получает только одну строку 
#мы задали свойство UNIQUE для пользователя, значит больше одной строки мы не можем получить
#Только один пользователь с таким именем может быть в БД
  if cur.fetchone() is not None:
    errors.append("Пользователь с данным именем уже существует")

    dbClose(cur, conn)

    return render_template('register.html', errors=errors)

  # Если мы попали сюда, что значит в cur fetchone нет ни одной строки, значит пользователя с таким же логином не существует
  cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{password}');")

  conn.commit
  dbClose(cur, conn)

  return redirect("/lab5/login")