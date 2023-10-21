from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
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

    return render_template('example.html', number_lab=number_lab, fruits=fruits, books=books)
    

@lab2.route('/lab2/')
def lab_2():
    return render_template('lab2.html')


@lab2.route('/lab2/flowers')
def lab2_flowers():
    return render_template('flowers.html')

@lab2.route('/lab2/for_1/<int:K>/<int:N>')
def for_1(N,K):

    # for i in range(N):
    #     print (K)

    return render_template('for_1.html', K=K, N=N)  

@lab2.route('/lab2/if_16/<float:a>/<float:b>/<float:c>')
def if_16(a,b,c):

    if c > b > a:
        a *= 2
        b *= 2
        c *= 2
    else:
        a = a*(-1)
        b = b*(-1)
        c = c*(-1)

    return render_template('if_16.html', a=a, b=b, c=c)  

@lab2.route('/lab2/for_36/<int:K>/<int:N>')
def for_36(N,K):

    sum = 0 
    for i in range(N):
        sum += i**K

    return render_template('for_36.html', K=K, N=N, sum=sum)  