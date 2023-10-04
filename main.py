import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtGui import QPainter, QBrush, QPen, QColor



from NewTicUI import Ui_MainWindow


set_x = 'x'
set_0 = '0'
counter = 0


def change_player(button_number):
    global counter
    print(counter)
    if button_number % 2 == 0:
        counter += 1
        return set_x
    else:
        counter += 1
        return set_0


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.all_buttons_list = [self.ui.btn_0,
                                 self.ui.btn_1, self.ui.btn_2,
                                 self.ui.btn_3, self.ui.btn_4,
                                 self.ui.btn_5, self.ui.btn_6,
                                 self.ui.btn_7, self.ui.btn_8]

        self.ui.btn_0.clicked.connect(lambda: window.ui.btn_0.setText(change_player(button_number=counter)))
        self.ui.btn_0.clicked.connect(lambda: window.ui.btn_0.setEnabled(False))
        self.ui.btn_1.clicked.connect(lambda: window.ui.btn_1.setText(change_player(button_number=counter)))
        self.ui.btn_1.clicked.connect(lambda: window.ui.btn_1.setEnabled(False))
        self.ui.btn_2.clicked.connect(lambda: window.ui.btn_2.setText(change_player(button_number=counter)))
        self.ui.btn_2.clicked.connect(lambda: window.ui.btn_2.setEnabled(False))
        self.ui.btn_3.clicked.connect(lambda: window.ui.btn_3.setText(change_player(button_number=counter)))
        self.ui.btn_3.clicked.connect(lambda: window.ui.btn_3.setEnabled(False))
        self.ui.btn_4.clicked.connect(lambda: window.ui.btn_4.setText(change_player(button_number=counter)))
        self.ui.btn_4.clicked.connect(lambda: window.ui.btn_4.setEnabled(False))
        self.ui.btn_5.clicked.connect(lambda: window.ui.btn_5.setText(change_player(button_number=counter)))
        self.ui.btn_5.clicked.connect(lambda: window.ui.btn_5.setEnabled(False))
        self.ui.btn_6.clicked.connect(lambda: window.ui.btn_6.setText(change_player(button_number=counter)))
        self.ui.btn_6.clicked.connect(lambda: window.ui.btn_6.setEnabled(False))
        self.ui.btn_7.clicked.connect(lambda: window.ui.btn_7.setText(change_player(button_number=counter)))
        self.ui.btn_7.clicked.connect(lambda: window.ui.btn_7.setEnabled(False))
        self.ui.btn_8.clicked.connect(lambda: window.ui.btn_8.setText(change_player(button_number=counter)))
        self.ui.btn_8.clicked.connect(lambda: window.ui.btn_8.setEnabled(False))
        self.ui.reset_btn.clicked.connect(lambda: self.reset_game())

        self.painter = QPainter()

    # def draw_something(self):
    #     painter = QPainter(self)
    #     pen = QPen()
    #     pen.setWidth(100)
    #     pen.setColor(QColor('red'))
    #     painter.setPen(pen)
    #     painter.drawPoint(200, 150)





    def reset_game(self):
        global counter
        counter = 0
        for btn in self.all_buttons_list:
            btn.setText('')
            btn.setEnabled(True)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    change_player(counter)
    window.show()
    sys.exit(app.exec())
