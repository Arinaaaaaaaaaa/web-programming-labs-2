from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
            errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():    
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    #Пусть кофе стоит 120 рублей, чёрный чай - 80 рублей, зелёный - 70 рублей.
    if drink == 'coffee':
        price = 120
    elif drink == 'black tea':
        price = 80
    else:
        price = 70

    #Добавка молока удорожает напиток на 30 рублей, а сахара - на 10.
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)

@lab3.route('/lab3/success')
def success():    
    return render_template('success.html')    

@lab3.route('/lab3/buy_tickets')
def buy_tickets():

    errors = {}
    users = request.args.get('users')
    age = request.args.get('age')
    departure_point = request.args.get('departure_point')
    destination_point = request.args.get('destination_point')
    date = request.args.get('date')

    if users == '':
        errors['users'] = 'Заполните поле!'
    if age == '':
        errors['age'] = 'Заполните поле!'
    if departure_point == '':
        errors['departure_point'] = 'Заполните поле!'
    if destination_point == '':
        errors['destination_point'] = 'Заполните поле!'
    if date == '':
        errors['date'] = 'Заполните поле!'
 
    price = 0 
 
    # Пусть взрослый билет стоит 450 рублей, а детский 300 рублей 
    ticket_type = request.args.get('ticket_type') 
    if ticket_type == 'adult': 
        price = 450 
    elif ticket_type == 'kid': 
        price = 300 
     
    # Пусть провоз багажа стоит 150 рублей 
    if request.args.get('baggage') == 'yes': 
        price += 150 
 

    return render_template('buy_tickets.html', users=users, age=age, departure_point=departure_point, 
    destination_point=destination_point,  date=date, price=price, errors=errors) 

@lab3.route('/lab3/ticket_payment')
def ticket_payment():

    errors = {}
    card = request.args.get('card')
    name = request.args.get('name')
    code = request.args.get('code')
    price = request.args.get('price')

    if card == '':
        errors['card'] = 'Заполните поле!'
    if name == '':
        errors['name'] = 'Заполните поле!'
    if code == '':
        errors['code'] = 'Заполните поле!'
    
    return render_template('ticket_payment.html', card=card, name=name, code=code, price=price, errors=errors) 

@lab3.route('/lab3/success_2')
def success_2():    
    return render_template('success_2.html')   


@lab3.route('/lab3/zashita')
def zashita():

    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d')

    diff = 0 


    if a == b == c: 
        diff = 4
    elif a == b == d:
        diff = 3
    elif a == c == d:
        diff = 2
    else:
        diff = 1


    return render_template('zashita.html', a=a, b=b, c=c, d=d, diff=diff)  


@lab3.route('/lab3/for_23/<float:X>/<int:N>')
def for_23(X,N): 

    p = X
    S = X
    k = 0

    for i in range(1, N+1):
        k +=2
        p *= (-1)*X*X/(k*(k+1))
        S += p

    return render_template('for_23.html', X=X, k=k, N=N, p=p, S=S)  