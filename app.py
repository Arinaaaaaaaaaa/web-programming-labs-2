from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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

        <footer>
            &copy; Малкова А.О., Зенкова А.М., ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""
