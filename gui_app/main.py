
import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QFileDialog,
)

class CardWindow(QWidget):
    def __init__(self, dict, name): #получаем словарь с данными карточки
        super().__init__()
        self.number = dict["num"]
        self.name = name
        self.setWindowTitle(f"Карточка №{self.number}")
        layout = QVBoxLayout()

        self.stack_title = QLabel(self.name) #название сборника
        layout.addWidget(self.stack_title)

        self.card_text = QLineEdit("Текст карточки")  #текст в карточке
        self.stack_title.setText(dict["card_text"])
        layout.addWidget(self.card_text)

        self.add_image = QPushButton("Выбрать картинку") #картинка
        self.add_image.clicked.connect(self.open_img)
        layout.addWidget(self.add_image)

        self.img_label = QLabel()
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        if dict["image"] == "":
            self.img_label.setText("Изображение еще не выбрано")
        else:
            self.img_label.setPixmap(dict["image"])
        self.img_label.setScaledContents(True)
        layout.addWidget(self.img_label)

        self.card_answ = QLineEdit("Текст карточки") #правильный ответ
        self.card_answ.setText(dict["true_answ"])
        layout.addWidget(self.card_text)

        self.save_but = QPushButton("Сохранить") #кнопка сохранить
        self.save_but.clicked.connect(self.save_card, self.close)
        layout.addWidget(self.save_but)

        self.setLayout(layout)

    def open_img(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Выбрать изображение',
            '',
            'Изображения (*.png *.jpg *.jpeg *.bmp *.gif)'
        )
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_path = file_path
            self.img_label.setPixmap(pixmap)

    def save_card(self):
        dict = {
            "num" : self.number,
            "card_text" : self.card_text.text(),
            "image" : self.image_path,
            "true_answ" : self.card_answ

        }
        return dict

class StackWindow(QWidget): #переписать елси окрывается для изменения
    def __init__(self, df):
        super().__init__()
        self.setWindowTitle("Новый набор")
        self.df = df
        layout = QVBoxLayout()
        self.n = 0

        self.stack_title.setText()
        self.stack_name = QLineEdit("Название набора")
        layout.addWidget(self.stack_name)

        self.button_add = QPushButton("+")
        layout.addWidget(self.button_add)
        self.button_add.clicked.connect(self.add_new_card())

        cards = QVBoxLayout()
        for card in self.df:
            temp = QPushButton(card["num"])
            temp.clicked.connect(self.open_card(card))
            cards.addWidget(temp)
        layout.addLayout(cards)

        self.ex_but = QPushButton("Сохранить")
        self.ex_but.clicked.connect(self.save_stack)
        
        self.setLayout(layout)

    def add_new_card(self):
        self.n += 1
        self.open_card(edit_card={"num" : self.n})

    def open_card(self, edit_card):
        opened_card = CardWindow(dict=edit_card, name=self.stack_name.text())
        opened_card.show()
        opened_card_df = pd.DataFrame(opened_card.save_card())
        self.df = pd.concat([self.df, opened_card_df], ignore_index=True)

    def save_stack(self):
        return pd.MultiIndex.from_product([[self.stack_name], self.df.columns])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        df = pd.read_csv("./data.csv") #открываем csv с данными
        self.setWindowTitle("Cards")
        layout = QVBoxLayout()

        self.new_object_but = QPushButton("+")
        self.new_object_but.clicked.connect(self.open_stack)
        layout.addWidget(self.new_object_but)

        objects_title = QLabel("Наборы карточек:")
        objects_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(objects_title)

        stacks = QVBoxLayout()

        for st in df:
            temp = QPushButton(st.columns.get_level_values(0)[0])
            temp.clicked.connect(self.open_stack(st.columns.columns.get_level_values(1)[:]))
            stacks.addWidget(temp)

        layout.addLayout(stacks)

        self.setCentralWidget(layout)

    def open_stack(self, df=pd.DataFrame()):
        opened_stack = StackWindow(df)
        df = pd.concat([df, pd.DataFrame(opened_stack.save_stack())])

app = QApplication()
window = MainWindow()
window.show()

app.exec()