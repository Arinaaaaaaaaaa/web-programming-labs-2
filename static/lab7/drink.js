function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(obj) 
        })
        .then(function (resp) {
            return resp.json();
        })
        .then(function (data) {
            document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб`;
            document.querySelector('#pay').style.display = '';
        });
}


function pay() {
    const drink = document.querySelector('[name=drink]:checked').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const card = document.querySelector('[name=card]').value;
    const name = document.querySelector('[name=name]').value;
    const cvv = document.querySelector('[name=cvv]').value;

    const obj = {
        "method": "pay",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar,
            card: card,
            name: name,
            cvv: cvv
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(obj)
    })
        .then(function (resp) {
            if (!resp.ok) {
                throw new Error('Ошибка ' + resp.status);
            }
            return resp.json();
        })
        .then(function (data) {
            if (data.error) {
                    document.querySelector('#price').innerHTML = `Ошибка: ${data.error}`;
            } else {
                document.querySelector('#price').innerHTML = 'Оплата прошла успешно: ' + data.result;;
                document.querySelector('#price').style.display = 'block';
            }
        });
}

function cancel_pay() {
    const drink = document.querySelector('[name=drink]:checked').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const card = document.querySelector('[name=card]').value;
    const name = document.querySelector('[name=name]').value;
    const cvv = document.querySelector('[name=cvv]').value;

    const obj = {
        "method": "refund",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar,
            card: card,
            name: name,
            cvv: cvv
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        if (data.error) {
            document.querySelector('#pay-status').innerHTML = `Ошибка: ${data.error}`;
        } else {
            document.querySelector('#pay-status').innerHTML = 'Возврат средств прошёл успешно на карту: ' + card;
            document.querySelector('#pay-status').style.display = 'block';
        }
    });
}