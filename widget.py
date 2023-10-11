from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from ui_widget import Ui_Widget


class Widget(QMainWindow, Ui_Widget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.setWindowTitle('Tic-Tac')
        self.setWindowIcon(QIcon('tic_icon.png'))

        self.counter = 0
        self.is_x = ''

        button_1 = self.ui.btn_0
        button_2 = self.ui.btn_1
        button_3 = self.ui.btn_2
        button_4 = self.ui.btn_3
        button_5 = self.ui.btn_4
        button_6 = self.ui.btn_5
        button_7 = self.ui.btn_6
        button_8 = self.ui.btn_7
        button_9 = self.ui.btn_8

        button_1.clicked.connect(self.button_1_clicked)
        button_2.clicked.connect(self.button_2_clicked)
        button_3.clicked.connect(self.button_3_clicked)
        button_4.clicked.connect(self.button_4_clicked)
        button_5.clicked.connect(self.button_5_clicked)
        button_6.clicked.connect(self.button_6_clicked)
        button_7.clicked.connect(self.button_7_clicked)
        button_8.clicked.connect(self.button_8_clicked)
        button_9.clicked.connect(self.button_9_clicked)

        self.posision_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.posision_list1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        self.ui.reset_btn.clicked.connect(self.restart_game)

    def button_1_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_0.setText('x')
            self.counter += 1
            self.ui.btn_0.setEnabled(False)
            self.posision_list[0][0] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_0.setText('0')
            self.counter += 1
            self.ui.btn_0.setEnabled(False)
            self.posision_list[0][0] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def button_2_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_1.setText('x')
            self.counter += 1
            self.ui.btn_1.setEnabled(False)
            self.posision_list[0][1] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_1.setText('0')
            self.counter += 1
            self.ui.btn_1.setEnabled(False)
            self.posision_list[0][1] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def button_3_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_2.setText('x')
            self.counter += 1
            self.ui.btn_2.setEnabled(False)
            self.posision_list[0][2] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_2.setText('0')
            self.counter += 1
            self.ui.btn_2.setEnabled(False)
            self.posision_list[0][2] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def button_4_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_3.setText('x')
            self.counter += 1
            self.ui.btn_3.setEnabled(False)
            self.posision_list[1][0] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_3.setText('0')
            self.counter += 1
            self.ui.btn_3.setEnabled(False)
            self.posision_list[1][0] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def button_5_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_4.setText('x')
            self.counter += 1
            self.ui.btn_4.setEnabled(False)
            self.posision_list[1][1] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_4.setText('0')
            self.counter += 1
            self.ui.btn_4.setEnabled(False)
            self.posision_list[1][1] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def button_6_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_5.setText('x')
            self.counter += 1
            self.ui.btn_5.setEnabled(False)
            self.posision_list[1][2] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_5.setText('0')
            self.counter += 1
            self.ui.btn_5.setEnabled(False)
            self.posision_list[1][2] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def button_7_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_6.setText('x')
            self.counter += 1
            self.ui.btn_6.setEnabled(False)
            self.posision_list[2][0] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_6.setText('0')
            self.counter += 1
            self.ui.btn_6.setEnabled(False)
            self.posision_list[2][0] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def button_8_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_7.setText('x')
            self.counter += 1
            self.ui.btn_7.setEnabled(False)
            self.posision_list[2][1] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_7.setText('0')
            self.counter += 1
            self.ui.btn_7.setEnabled(False)
            self.posision_list[2][1] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def button_9_clicked(self):
        clicked = True
        if clicked and self.counter % 2 == 0:
            self.ui.btn_8.setText('x')
            self.counter += 1
            self.ui.btn_8.setEnabled(False)
            self.posision_list[2][2] = 'x'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()
        else:
            self.ui.btn_8.setText('0')
            self.counter += 1
            self.ui.btn_8.setEnabled(False)
            self.posision_list[2][2] = '0'
            self.forward_diag_search()
            self.backward_diag_search()
            self.column_row_search()

    def restart_game(self):
        self.counter = 0
        self.posision_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(self.posision_list)
        bt_list = [self.ui.btn_0, self.ui.btn_1, self.ui.btn_2,
                   self.ui.btn_3, self.ui.btn_4, self.ui.btn_5,
                   self.ui.btn_6, self.ui.btn_7, self.ui.btn_8]

        for i in range(len(bt_list)):
            bt_list[i].setText('')
            bt_list[i].setEnabled(True)

    def forward_diag_search(self):
        diag_check_forward_x = ''
        diag_check_forward_0 = ''
        for i in range(3):
            if self.posision_list[i][i] == 'x':
                diag_check_forward_x += 'x'
            elif self.posision_list[i][i] == '0':
                diag_check_forward_0 += '0'
        if 'xxx' in diag_check_forward_x:
            self.posision_list = self.posision_list1
            print('Player x wins')
        elif '000' in diag_check_forward_0:
            self.posision_list = self.posision_list1
            print('Player 0 wins')

    def backward_diag_search(self):
        diag_check_backward_x = ''
        diag_check_backward_0 = ''
        for i in range(3):
            if self.posision_list[i][3 - i - 1] == 'x':
                diag_check_backward_x += 'x'
            elif self.posision_list[i][3 - i - 1] == '0':
                diag_check_backward_0 += '0'
        if 'xxx' in diag_check_backward_x:
            self.posision_list = self.posision_list1
            print('Player X wins')
        elif '000' in diag_check_backward_0:
            self.posision_list = self.posision_list1
            print('Player 0 wins')

    def column_row_search(self):
        row_sum = ''
        column_sum = ''
        for i in range(3):
            for j in range(3):
                row_sum += self.posision_list[i][j]
                column_sum += self.posision_list[j][i]
            if 'xxx' in row_sum:
                print('Player X wins')
            elif '000' in row_sum:
                print('Player 0 wins')
            elif 'xxx' in column_sum:
                print('Player X wins')
            elif '000' in column_sum:
                print('Player 0 wins')


