# напиши здесь код основного приложения и первого экрана
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from final_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apear()#установка
        #характ. окна
        self.UI()#создание интерфейса
        self.connect()#подкл. кнопок
        self.show()#показать окно

    def set_apear(self):
        self.setWindowTitle("Тест руфье")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def UI(self):
        #интерфейс первого окна
        #создание виджетов
        self.label1 = QLabel(txt_hello)
        self.label2 = QLabel(txt_instruction)
        self.button = QPushButton("Начать")
        #создание линий и установка виджетов
        main_line = QVBoxLayout()
        main_line.addWidget(self.label1, alignment = Qt.AlignLeft)
        main_line.addWidget(self.label2, alignment = Qt.AlignLeft)
        main_line.addWidget(self.button, alignment = Qt.AlignCenter)
        #установить линию на экран
        self.setLayout(main_line)
    
    #подкл. кнопок (в будущем)
    def connect(self):
        pass
app = QApplication([])
main_win = MainWin()
final_win = FinalWin()
app.exec()
