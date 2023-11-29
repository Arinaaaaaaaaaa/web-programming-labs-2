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
def main():
  conn = dbConnect()
  cur = conn.cursor()

  cur.execute("SELECT * FROM users;")

  result = cur.fetchall()

  print(result)

  dbClose(cur, conn)

  return result


@lab5.route("/lab5/users")
def users_bd():
  conn =  dbConnect()
  cur = conn.cursor()

  cur.execute("SELECT username FROM users;")

  result = cur.fetchall()

  print(result)

  dbClose(cur, conn)

  return render_template('lab5.html', result=result) 