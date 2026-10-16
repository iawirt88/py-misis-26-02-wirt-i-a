import abc

class Calculator(abc.ABC): # ШАБЛОН АБСТРАКТНОГО КАЛЬКУЛЯТОРА

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @abc.abstractmethod 
    def calc(self):
        pass


class Finance(Calculator): # РАСЧЕТ РАЗМЕРА ЕЖЕМЕСЯЧНОГО ПЛАТЕЖА ДЛЯ АННУИТЕНТНОГО И ДИФФЕРЕНЦИРОВАННОГО ВИДА КРЕДИТОВАНИЯ
    def __init__(self, a, b, c, vid, m=1):
        super().__init__(a, b, c)
        self.vid = vid
        self.m = m

    def calc(self):
        prcnt_mnth = self.c / 1200
        if self.vid == "ann":
            return self.a * prcnt_mnth * (1 + prcnt_mnth) ** self.b / ((1 + prcnt_mnth) ** self.b - 1)
        elif self.vid == "dif":
            return self.a / self.b + (self.a - self.a / self.b * (self.m - 1)) * prcnt_mnth

    def print_result(self):
        print(f"Результат: {self.calc()}")
    

fin = Finance(100000, 6, 12, "ann")
fin.print_result()
fin = Finance(100000, 6, 12, "dif", 4)
fin.print_result()