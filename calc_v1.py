def calc():
    num_1 = int(input('Число 1: '))
    oper = input('Операция: ')
    num_2 = int(input('Число 2: '))

    if oper == '+':
        return num_1 + num_2
    elif oper == '-':
        return num_1 - num_2
    elif oper == '*':
        return num_1 * num_2
    elif oper == '/':
        return num_1 / num_2
    elif oper == '%':
        return num_1 % num_2
    elif oper == '//':
        return num_1 // num_2

print(calc())