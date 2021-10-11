import requests

def accumultate():
    total = 0
    while True:
        x = (yield)
        if x is None:
            return total
        total += x


co = accumultate()
next(co)

for i in range(1, 11):
    co.send(i)
co.send(None)



