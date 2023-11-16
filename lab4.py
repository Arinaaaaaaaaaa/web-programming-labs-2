from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


    username = request.form.get('username') 
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success_3.html', username=username)


    if not username and not password:
        error = "Не введён логин и пароль!"
        return render_template('login.html', error=error, username=username, password=password)
    elif not password:
        error = "Не введён пароль!"
        return render_template('login.html', error=error, username=username, password=password)
    elif not username:
        error = "Не введён логин!"
        return render_template('login.html', error=error, username=username, password=password)
    else:
        error = "Неверный логин и/или пароль!"
        return render_template('login.html', error=error, username=username, password=password)


@lab4.route('/lab4/fridge', methods = ['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('fridge.html')
    

    temperature = request.form.get('temperature') 
    

    if not temperature:
        error = "Ошибка: не задана температура!"
        return render_template('fridge.html', error=error, temperature=temperature)
    elif int(temperature) < -12:
        error = "Не удалось установить температуру — слишком низкое значение!"
        return render_template('fridge.html', error=error, temperature=temperature)
    elif int(temperature) > -1:
        error = "Не удалось установить температуру — слишком высокое значение!"
        return render_template('fridge.html', error=error, temperature=temperature)
    elif int(temperature) >= -12 and int(temperature) <= -9:
        correct = "Установлена температура: "+ str(temperature)+"°С ❄❄❄"
        return render_template('fridge.html', correct=correct, temperature=temperature)
    elif int(temperature) >= -8 and int(temperature) <= -5:
        correct = "Установлена температура: "+ str(temperature)+"°С ❄❄"
        return render_template('fridge.html', correct=correct, temperature=temperature)
    else:
        correct = "Установлена температура: "+ str(temperature)+"°С ❄"
        return render_template('fridge.html', correct=correct, temperature=temperature)


@lab4.route('/lab4/seed', methods = ['GET', 'POST'])
def seed():
    choise_zerno = request.form.get('choise_zerno')
    if request.method == 'GET':
        return render_template('seed.html')

    weight = request.form.get('weight')

    if not weight:
        error = "Ошибка: не введён вес!"
        return render_template('seed.html', error=error, weight=weight)
    elif int(weight) <= 0:
        error = "Ошибка: Неверное значение веса!"
        return render_template('seed.html', error=error, weight=weight)
    elif int(weight) >= 500:
        error = "К сожалению, такого объёма сейчас нет в наличии!"
        return render_template('seed.html', error=error, weight=weight)
    elif str(choise_zerno) == "zerno":
        error = "Выберите тип зерна!"
        return render_template("seed.html", error = error)    
    elif int(weight) <= 500 and int(weight) >= 50:
        correct = "Дарим Вам скидку 10% за крупный заказ!"

        weight = int(weight)
        prices = {
        'barley': 12000,
        'oats': 8500,
        'wheat': 8700,
        'rye': 14000
        }
        price_per_ton = prices[choise_zerno]
        total_price = weight * price_per_ton
        total_price *= 0.9

        if choise_zerno == "barley":
            choise_zerno = "ячмень"
        elif choise_zerno == "wheat":
            choise_zerno = "пшеницу"
        elif choise_zerno == "rye":
            choise_zerno = "рожь"
        else:
            choise_zerno = "овёс"

        return render_template("success_4.html", total_price = total_price, choise_zerno=choise_zerno, correct=correct, weight=weight)

    else:
        weight = int(weight)
        prices = {
        'barley': 12000,
        'oats': 8500,
        'wheat': 8700,
        'rye': 14000
        }
        price_per_ton = prices[choise_zerno]
        total_price = weight * price_per_ton

        if choise_zerno == "barley":
            choise_zerno = "ячмень"
        elif choise_zerno == "wheat":
            choise_zerno = "пшеницу"
        elif choise_zerno == "rye":
            choise_zerno = "рожь"
        else:
            choise_zerno = "овёс"

        return render_template("success_4.html", total_price = total_price, weight = weight, choise_zerno=choise_zerno)


    return render_template("seed.html")

@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')

    if request.method == 'POST':
        color = request.form.get('color')
        background_color = request.form.get('background_color')
        font_size = request.form.get('font_size')
        headers = {
            'Set-Cookie' : [ 
                'color=' + color + '; path=/',
                'background-color=' + background_color + '; path=/',
                'font-size=' + font_size + "px" +'; path=/',
            ],
            'location': '/lab4/cookies'
        }

        if color == background_color:
            error = "Цвет текста и фона не должны совпадать!"
            return render_template('cookies.html', error=error)

        if font_size is None or font_size == '':
            error = "Введите размер шрифта!"
            return render_template('cookies.html', error=error)    

        if int(font_size) > 30 or int(font_size) < 5:
            error = "Введите размер шрифта от 5 до 30!"
            return render_template("cookies.html", error=error)
            
    return '', 303, headers