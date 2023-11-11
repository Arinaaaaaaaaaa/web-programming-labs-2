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
