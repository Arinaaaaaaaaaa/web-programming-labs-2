from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu",code=302)

@app.route("/menu")
def menu():
    return """    
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
           НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <h1>Лабораторные работы по WEB-программированию</h1>
            <ol>
                <li>
                    <a href="http://127.0.0.1:5000/lab1",target="_blank">Первая лабораторная работа</a>
                </li>
            </ol>
        </main>

        <footer>
            &copy; Малкова А.О., Зенкова А.М., ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def first():
    return """
<!doctype html>
<html>
    <head>
        <title>Малкова Арина Олеговна и Зенкова Алина Максимовна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <p>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности</p>

        <footer>
            &copy; Малкова А.О., Зенкова А.М., ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""    
