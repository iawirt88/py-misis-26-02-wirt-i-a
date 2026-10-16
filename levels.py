import sys
import re

def main():
    print("Напишите exit для выхода")
    lvl = input("Выберите уровень: ")
    if lvl == "exit":
        sys.exit()
    txt = input("Введите текст: ")
    if lvl == '1':
        print(lvl_1(txt))
    if lvl == '2':
        print(lvl_2(txt))
    if lvl == '3':
        print(lvl_3(txt))
    if lvl == '4':
        print(lvl_4(txt))
    if lvl == '5':
        print(lvl_5(txt))
    

def lvl_1(txt, meth=' '):
    meth = meth if meth != ' ' else input("Выбирите метод (Lower - нижний ригистр, Upper - верхний регистр, Capitalize - первое слово с большой буквы, остальные в нижнем регистре): ")
    if meth == "Upper":
        txt = txt.upper()
    elif meth == "Lower":
        txt = txt.lower()
    elif meth == "Capitalize":
        txt = txt.capitalize()
    return txt

def lvl_2(txt, meth=' ', a=' ', b=' '):
    meth = meth if meth != ' ' else input("Выбирите метод (Find - найти символ, Replace - заменить символ, Count - количество символов): ")
    if meth == "Find":
        a = a if a != ' ' else input("Какое слово найти: ")
        return txt.find(a)
    elif meth == "Replace":
        a = a if a != ' ' else input("Каое слово заименить: ")
        b = b if b != ' ' else input("На какое слово выполнить замену: ")
        return txt.replace(a, b)
    elif meth == "Count":
        a = a if a != ' ' else input("Кол-во вхождений какого слова нужна посчитать: ")
        return txt.count(a)
#    elif meth == "Index":
  #      a = input("Какое слово найти: ") # если слова нет выдаст ошибку ValueError
    #    return txt.index(a)

def lvl_3(txt, meth=' ', a=' ', b=' '):
    meth = meth if meth != ' ' else input("Выбирите метод (Split - разделить текст через символ, Join - соеденить текст через символ): ")
    if meth == "Split":
        a = a if a != ' ' else input("Укажите разделитель: ")
        return txt.split(sep=a)
    elif meth == "Join":
        a = a if a != ' ' else input("Укажите соединтель: ")
        return a.join(txt.split(sep=b))
def lvl_4(txt, meth=' ', a=' '):
    meth = meth if meth != ' ' else input("Выбирите метод (Digit - проврить есть ли сиволы кроме цифр, Alpha - есть ли символы кроме букв, Strip - очищает текст от лишних символов с конца и начала): ")
    if meth == "Digit":
        return "Только цифры" if txt.isdigit() else "Не только цифры"
    elif meth == "Alpha":
        return "Только бувы" if txt.isalpha() else "Не только буквы или строка пуста"
    elif meth == "Strip":
        return txt.strip()
 #   elif meth == "Format":
 #       a = a if a != ' ' else input("Укажите связь между словами: ")
#      return 
def lvl_5(txt): #привести текст в нормальный формат (убрать лишние пробелы, отформатировать в нижний ригистр, отформатировать через capitalize)
    print("Приводит текст в нормальный формат, удаляя спецсимволы и лишние пробелы")
    txt = txt.strip()
    txt = re.sub(r'[^\w\s]', ' ', txt)
    return txt.capitalize()
def test_1():
    print()
    print(lvl_1("пРиВет МИР", meth="Upper"))
    print(lvl_1("пРиВет МИР", meth="Lower"))
    print(lvl_1("пРиВет МИР", meth="Capitalize"))    
def test_2():
    print()
    print(lvl_2("Ботать это круто. Очень круто", meth="Find", a="круто"))
    print(lvl_2("Ботать это круто. Очень круто", meth="Replace", a="круто", b="слово"))
    print(lvl_2("Ботать это круто. Очень круто", meth="Count", a="о"))
def test_3():
    print()
    print(lvl_3("1,2,3,4", meth="Split", a=','))
    print(lvl_3("1,2,3,4", meth="Join", a=',', b=',')) 
def test_4():
    print()
    print(lvl_4("1234*&%^$", meth="Digit"))
    print(lvl_4("1234*&%^$", meth="Alpha"))
    print(lvl_4("1234*&%^$", meth="Strip"))
    print(lvl_4("   abc1234    ", meth="Digit"))
    print(lvl_4("   abc1234    ", meth="Alpha"))
    print(lvl_4("   abc1234    ", meth="Strip"))
def test_5():
    print()
    print(lvl_5("    pYtHon;is;AWESome   "))
test_1()
test_2()
test_3()
test_4()
test_5()

while True:
    main()
    