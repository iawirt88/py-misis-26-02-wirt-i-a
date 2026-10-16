def plus(a, b):
    return a + b
def minu(a, b):
    return a - b
def umn(a, b):
    return a * b
def dele(a, b):
    return a / b
def ost(a, b):
    return a % b
def celdel(a, b):
    return a // b

def calc():
    num_1 = int(input('Число 1: '))
    oper = input('Операция: ')
    num_2 = int(input('Число 2: '))

    if oper == '+':
        return plus(num_1, num_2)
    elif oper == '-':
        return minu(num_1, num_2)
    elif oper == '*':
        return umn(num_1, num_2)
    elif oper == '/':
        return dele(num_1, num_2)
    elif oper == '%':
        return ost(num_1, num_2)
    elif oper == '//':
        return celdel(num_1, num_2)

while True:
    print('=', calc())
    print()