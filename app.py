from flask import Flask, redirect, url_for, render_template
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

        <a href="http://127.0.0.1:5000/menu",target="_blank">Меню</a>

        <h2>Реализованные роутеры</h2>

        <ul>
                <li>
                    <a href="http://127.0.0.1:5000//lab1/oak",target="_blank">/lab1/oak - дуб</a>
                </li>

                <li>
                    <a href="http://127.0.0.1:5000/lab1/student",target="_blank">/lab1/student - студент</a>
                </li>

                <li>
                    <a href="http://127.0.0.1:5000/lab1/python",target="_blank">/lab1/python - python</a>
                </li>

                <li>
                    <a href="http://127.0.0.1:5000/lab1/nstu",target="_blank">/lab1/nstu - НГТУ</a>
                </li>
        </ul>

        <footer>
            &copy; Малкова А.О., Зенкова А.М., ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""    

@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
        <style>
            img {width: 750px;
            height: 500px;
            padding: 5px 0px 35px 370px;}
            </style>
    </head>

    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Дуб</h1>
        <img src="'''+ url_for('static', filename='oak.jpg')+'''">
        <footer>
            &copy; Малкова А.О., Зенкова А.М., ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
         <style>
            p{
                 font-size: 25px;
                 padding-left: 20px;
            }
            img{
                width: 750px;
                height: 300px;
                padding-left: 20px;
            }
         </style>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <p>Зенкова Алина Максимовна <br> Малкова Арина Олеговна</p>
            <img src="'''+ url_for('static', filename='logo_NSTU.png')+'''">
        </main>
        
        <footer>
            &copy; Малкова А.О., Зенкова А.М., ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
         <style>
            p{
                font-size: 20px;
                padding: 0px 20px;
                text-align: justify;
                text-indent: 45px;
            }
            img{
                width: 350px;
                height: 300px;
                padding-left: 20px;
            }
         </style>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <p>Python - это высокоуровневый язык программирования общего назначения. 
            Его философия дизайна подчеркивает удобочитаемость кода с использованием значительных отступов.</p>

            <p>Python динамически типизируется и собирает мусор. Он поддерживает множество парадигм программирования,
             включая структурированное (в частности, процедурное), объектно-ориентированное и функциональное программирование.
            Его часто описывают как язык с "включенными батарейками" из-за его обширной стандартной библиотеки.</p>
            
            <p>Гвидо ван Россум начал работать над Python в конце 1980-х годов как преемником языка программирования ABC и 
            впервые выпустил его в 1991 году как Python 0.9.0. Python 2.0 был выпущен в 2000 году. Python 3.0, выпущенный в 2008
            году, был серьезной редакцией, не полностью обратно совместимой с более ранними версиями. Python 2.7.18, выпущенный 
             в 2020 году, был последним выпуском Python 2.</p>
            <img src="'''+ url_for('static', filename='Python.png')+'''">
        </main>

        <footer>
            &copy; Малкова А.О., Зенкова А.М., ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/nstu')
def nstu():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
         <style>
            p{
                font-size: 20px;
                padding: 0px 20px;
                text-align: justify;
                text-indent: 45px;
                line-height: 28px;
            }
            img{
                padding-left: 20px;
            }
         </style>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <p>Создан постановлением Совета министров СССР от 19 августа 1950, 
            как Новосибирский электротехнический институт (НЭТИ), в том же году 
            началась закладка первого корпуса. Первые занятия начались в 1953 году. 
            Первое крупное здание (студенческое общежитие) было построено в 1954. 
            Первый учебный корпус был возведён только в 1960, до этого времени занятия 
            проводились в 6 переоборудованных квартирах дома на ул. Римского-Корсакова. 
            Первый выпуск состоялся в 1958 году и составил 153 инженера. Среди них — будущие 
            ведущие специалисты крупных предприятий и НИИ, видные руководители, академики. 
            В 1991 году институт одним из первых в России перешёл на многоуровневую систему образования. 
            В 1992 года был переименован в Новосибирский государственный технический университет в связи с 
            добавлением нетехнических факультетов. В 1995 году в состав университета вошёл Новосибирский институт 
            социальной реабилитации, единственное в Сибири учебное заведение, где обучаются лица с ограниченными физическими 
            возможностями из различных регионов России (от Северного Кавказа до Камчатки). На базе университета работает филиал 
            исследовательского центра РФ по проблемам качества подготовки специалистов.</p>

            <p>Основатели НЭТИ-НГТУ: Алабужев Пётр Михайлович — д. т. н., профессор, зав. кафедрой (1908—1995); 
            Веселовский Олег Николаевич — д. т. н., профессор, проректор по учебной работе (1928—2018); 
            Лыщинский Георгий Павлович — профессор, ректор НЭТИ (1922—1995); Орлов Василий Тимофеевич — 
            к. т. н., доцент, проректор по учебной работе (1906—1965); Городецкий Александр Фомич — к. т. н., 
            профессор, зав. кафедрой (1910—1968); Грабовецкий Георгий Владимирович — д. т. н., профессор, зав. кафедрой 
            (1922—2013); Пазухин Сергей Павлович — д. т. н., профессор, зав. кафедрой (1895—1966); Потужный Андрей Ксенофонтович — 
            к. т. н., доцент, директор НЭТИ (1905—1955; Казанский Василий Михайлович — д. т. н., профессор, проректор по научной 
            работе (1922—2011); Колкер Иосиф Григорьевич — д. т. н., профессор, декан (1918—2005); Тушинский Леонид Иннокентьевич — 
            д. т. н., профессор, зав. кафедрой (1926—2010); Щербаков Василий Кузьмич — д. т. н., профессор, зав. кафедрой (1903—1980)</p>
            <img src="'''+ url_for('static', filename='Nstu.jpg')+'''">
        </main>

        <footer>
            &copy; Малкова А.О., Зенкова А.М., ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Зенкова Алина, Малкова Арина'
    number_lab = "2"
    group = 'ФБИ-11'
    number_course = '3'
    return render_template('example.html', name=name, number_lab=number_lab, group=group, number_course=number_course)