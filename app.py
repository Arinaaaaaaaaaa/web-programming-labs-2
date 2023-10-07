from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)


@app.route('/lab2/example')
def example():
    name = 'Зенкова Алина, Малкова Арина'
    number_lab = "2"
    group = 'ФБИ-11'
    number_course = '3'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}   
    ]
    books = [
        {'writer': 'Стефан Цвейг', 'name': 'Нетерпение сердца', 'style': 'классическая литература', 'page_count': '448 с.'},
        {'writer': 'Александр Дюма', 'name': 'Граф Монте-Кристо', 'style': 'классическая литература', 'page_count': '1264 с.'},
        {'writer': 'Иван Тургенев', 'name': 'Отцы и дети', 'style': 'классиче-ская литература', 'page_count': '416 с.'},
        {'writer': 'Михаил Булгаков', 'name': 'Мастер и Маргарита', 'style': 'классическая литература', 'page_count': '420 с.'},
        {'writer': 'Александр Пушкин', 'name': 'Дубровский', 'style': 'класси-ческая литература', 'page_count': '256 с.'},
        {'writer': 'Эдогава Рампо', 'name': 'Человек-кресло', 'style': 'клас-сическая литература', 'page_count': '144 с.'},
        {'writer': 'Стивен Кинг', 'name': 'Оно', 'style': 'ужасы', 'page_count': '1184 с.'},
        {'writer': 'Лев Толстой', 'name': 'Анна Каренина', 'style': 'классиче-ская литература', 'page_count': '832 с.'},
        {'writer': 'Джон Фаулз', 'name': 'Волхв', 'style': 'классическая про-за', 'page_count': '736 с.'},
        {'writer': 'Джек Лондон', 'name': 'Странник по звездам', 'style': 'научная фантастика', 'page_count': '352 с.'}
    ]
    a=11.5
    b=12.5
    c=13.5
    k=24
    n=5
    z=3
    x=4
    sum = 0
    for d in range(1,z+1):
        sum += d ** x

    return render_template('example.html', number_lab=number_lab, fruits=fruits, books=books, a=a, b=b, c=c, k=k, n=n, z=z, x=x, sum=sum)
    
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/flowers')
def lab2_flowers():
    return render_template('flowers.html')