import ccxt


def number_coroutine():
    while True:
        x = (yield)
        print(x)

co = number_coroutine()
next(co)

co.send(1)
co.send(2)
co.send(3)

def authorize():
    auth_dict = (yield)

    binance = ccxt.binance(config={
        'apiKey': auth_dict.get("api_key"),
        'secret': auth_dict.get("secret"),
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future'
        }
    })
    while True:






# while True:
#     x = (yield)
#     if x is None:
#         return total
#     total += x
#
# def sum_coroutine():
#     while True:
#         total = yield from accumultate()
#         print(total)

auth = authorize()
next(auth)

for i in range(1, 11):
    co.send(i)
co.send(None)

for i in range(1, 101):
    co.send(i)import ccxt


def number_coroutine():
    while True:
        x = (yield)
        print(x)

co = number_coroutine()
next(co)

co.send(1)
co.send(2)
co.send(3)

def authorize():
    auth_dict = (yield)

    binance = ccxt.binance(config={
        'apiKey': auth_dict.get("api_key"),
        'secret': auth_dict.get("secret"),
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future'
        }
    })
    while True:






# while True:
#     x = (yield)
#     if x is None:
#         return total
#     total += x
#
# def sum_coroutine():
#     while True:
#         total = yield from accumultate()
#         print(total)

auth = authorize()
next(auth)

for i in range(1, 11):
    co.send(i)
co.send(None)

for i in range(1, 101):
    co.send(i)
co.send(None)

co.send(None)
