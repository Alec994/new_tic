import sys
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    #
    # def draw_something(self):
    #     canvas = self.label.pixmap()
    #     painter = QtGui.QPainter(canvas)
    #     painter.drawLine(10, 10, 300, 200)
    #     painter.end()
    #     self.label.setPixmap(canvas)
    def draw_something(self):
        painter = QPainter()
        painter.begin()
        painter.setPen(QColor('red'))
        painter.setBrush(QColor('black'))
        # painter.drawLine(0, 0, 100, 250)
        painter.drawArc(100, 70, 300, 300, 0 * 16, 180 * 16)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
# window.draw_something()
window.show()
app.exec()