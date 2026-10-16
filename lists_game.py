import sys
import os
import subprocess

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

# # рисуем строки
# def pole():
#     for row in game:
#         print(f"| {row[0]:<3} | {row[1]:<3} | {row[2]:<3} | {row[3]:<3} |")
#         # Рисуем горизонтальный разделитель под каждой строкой
#         print("-" * 25)

pos = [0, 0]

up = False
down = False
right = False
left = False 

def move():
    global pos, up, down, left, right
    # движение по оси x
    if pos[1] == 0:
        left = False
        right = True
    elif pos[1] == 3:
        left = True
        right = False
    else:
        left = True
        right = True
    # движение по оси y
    if pos[0] == 0:
        up = False
        down = True
    elif pos[0] == 3:
        up = True
        down = False
    else:
        up = True
        down = True
    return f"Доступное перемещение: {'Вверх - W' if up else ''} {'Вниз - S' if down else ''} {'Влево - A' if left else ''} {'Вправо - D' if right else ''}"

def new_pos(): # выбор направления для перемещения       
    global pos
    movement = input().lower()
    if movement == "exit":
        sys.exit()
    if movement == 'w' and up:
        return [pos[0] - 1, pos[1]]
    elif movement == 's' and down:
        return [pos[0] + 1, pos[1]]
    elif movement == 'a' and left:
        return [pos[0], pos[1] - 1]
    elif movement == 'd' and right:
        return [pos[0], pos[1] + 1]
    else:
        print("Ошибочный ввод! Попробуйте еще раз")
        return new_pos()

class Subject:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

weapon = Subject(name="Оружие", value=1)
key_chest = Subject(name="Ключ от сундука")
key_secret = Subject(name="Ключ от тайника")
key_exit = Subject(name="Особый ключ")
lifes = Subject(name="Жизни", value=3)

all_subjects = [weapon, key_chest, key_secret, key_exit]

class Inventar:

    def __init__(self, subjects):
        self.subjects = subjects

    def catch(self, item=None): # добавление новых предметов
        if item == None:
            print("Не удалось выполнить операцию")
            return
        operand = input("Введите операцию: a-добавить первый предмет, b-добавить все предметы: ")
        while len(item) > 0:
            if operand == "a":
                self.subjects.append(item[-1])
                item.pop()
            elif operand == "b":
                self.subjects.extend(item)
                item = []
            else:
                print("Неверная операция!")
                return self.catch(item)

    def throw(self): # удаление предметов
        operand = input("Введите операцию: a-удалить последний предмет в инвентаре, b-удалить предмет: ")
        if len(self.subjects) == 0:
            print("Инвентарь пуст")
        else:
            if operand == "a":
                self.subjects.pop()
            elif operand == "b":
                number = input("Введите номер предмета, который хотите выбросить: ")
                if number.isdigit() and 1 <= int(number) <= len(self.subjects):
                    self.subjects.pop(int(number) - 1)
                    print("Предмет выброшен")
                else:
                    print("Такого предмета нет")

    def sorts(self):
        operand = input("Введите операцию: a-сортировать, b-реверсировать: ")
        if operand == "a":
            self.subjects.sort(key=lambda subjects: subjects.name)
        elif operand == "b":
            self.subjects.reverse()

    def finds(self):
        operand = input("Введите операцию: a-проверка наличия предмета в инвентаре, b-найти номер предмета: ")
        for i in range(len(all_subjects)):
            print(f"{i + 1} - {all_subjects[i].name}")
        number = input("Какой предмет ищем (номер): ")
        if not (number.isdigit() and 1 <= int(number) <= len(all_subjects)):
            print("Неверный номер!")
            return
        item = all_subjects[int(number) - 1]
        if operand == "a":
            print(item in self.subjects)
        elif operand == "b":
            if item in self.subjects:
                print(f"Предмет найден: {item.name} : {self.subjects.index(item) + 1}")
            else:
                print("Предмет не найден")

    def use(self):
        number = input("Укажите номер предмета, который хотите использовать: ")
        if number.isdigit() and 1 <= int(number) <= len(self.subjects):
            print("Предмет найден")
            return self.subjects[int(number) - 1]
        print("Предмет не найден!")
        return None

    def copies(self, a, b):
        return self.subjects[a:b]
        # sliced_A = A[slice(x, y, z)]

    def list_comp(self, A):
        pass

    def interface(self):
        print(f"Предметы существующие в игре: {weapon.name}, {key_chest.name}, {key_secret.name}, {key_exit.name}")
        while True:
            active = input("0-для выхода из инвентаря, 1-для продолжения: ")
            if active == "0": 
                break
            print("Список доступных действий: ")
            funcs = [self.finds, self.sorts, self.throw, self.use] # пояснить функционал
            print("1 - найти предмет, 2 - сортировать инвентарь, 3 - выбросить предмет, 4 - использовать предмет")
            choice = input(f"Выберите действие: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(funcs):
                result = funcs[int(choice) - 1]()
                if result != None:
                    return result
            else:
                print("Неверный выбор операции!")

inventar = Inventar([weapon, key_chest])

class Room:

    def __init__(self, name):
        self.temp_sub = []
        self.name = name
        self.done = False

    def info(self):
        print(f"Комната: {self.name}")

    def invent_ap(self, obj):
        self.temp_sub.append(obj)

    def interaction(self):
        pass

class Chest(Room):

    def interaction(self):
        print("Чтобы открыть сундук вам нужен ключ.")
        item = inventar.interface()
        if item == key_chest:
            print("Сундук открыт!")
            inventar.subjects.remove(key_chest)
            self.invent_ap(key_secret)
            self.done = True
        else:
            print("Выбран не тот предмет.")
        return self.temp_sub

class Cache(Room):

    def interaction(self):
        print("Чтобы открыть тайник вам нужен ключ.")
        item = inventar.interface()
        if item == key_secret:
            print("Тайник вскрыт!")
            inventar.subjects.remove(key_secret)
            self.invent_ap(key_exit)
            self.done = True
        else:
            print("Выбран не тот предмет.")
        return self.temp_sub

class Monster(Room):

    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def interaction(self):
        print("Вам предстоит сразиться с монстром! Для этого выберите оружие, если оно недостаточного уровня, монстр вас одолеет")
        item = inventar.interface()
        if item != None and self.level == item.value:
            print("Монстр повержен!")
            self.invent_ap(key_chest)
            self.done = True
        else:
            print("Вы не справились с монстром. Вы теряете одну жизнь!")
            lifes.value -= 1
        return self.temp_sub

class Trap(Room):

    def interaction(self):
        print("Вы попали в ловушку. Вы теряете одну жизнь!")
        lifes.value -= 1
        return self.temp_sub

class Portal(Room):

    def interaction(self):
        print("Это финальная комната, которая ведет на выход. Если вы собрали все три ключа, вы сможете пройти!")
        inventar.interface()
        if inventar.subjects.count(key_exit) >= 3:
            print("ВЫ ПОБЕДИЛИ! ИГРА ОКОНЧЕНА")
            input("Введите любой символ для выхода: ")
            sys.exit()
        else:
            print("Скорее всего, у вас есть не все необходимые ключи!")
            return self.temp_sub

N = Room("Пустая")
S = Chest("Сундук")
T = Cache("Тайник")
M = Monster("Монстр", 1)
L = Trap("Ловушка")
P = Portal("Портал")

# игровое поле
game = [
    [N, S, T, M],
    [N, M, L, T],
    [N, M, S, L],
    [S, T, M, P],
]

def action():
    global game, pos
    current_pos = game[pos[0]][pos[1]]
    new_items = []
    if current_pos == N:
        current_pos.info()
    else:
        current_pos.info()
        new_items = current_pos.interaction()
    if current_pos.done:
        game[pos[0]][pos[1]] = N
        current_pos.done = False
    if new_items != None and len(new_items) > 0:
        print("Вы можете положить новые предметы в инвентарь!")
        inventar.catch(new_items)
    current_pos.temp_sub = []
    inventar.interface()

    
def main():
    global pos
    while lifes.value > 0:
        print("exit-для выхода")
        print(move())
        pos = new_pos()
        action()
        clear_screen()
    print("Жизни закончились. ИГРА ОКОНЧЕНА")

if __name__ == "__main__":
    main()