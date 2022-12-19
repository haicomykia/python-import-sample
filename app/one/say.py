from app.two import calc


def hello():
    print('Hello World! from package one')


def plus(a, b):
    return calc.plus(a, b)
