from PyQt5 import QtWidgets
from keypad2 import Ui_MainWindow
import sys


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Controller, self).__init__()
        self.uif = Ui_MainWindow()
        self.uif.setupUi(self)
        self.uif.Button1.pressed.connect(self.btn_one)
        self.uif.Button2.pressed.connect(self.btn_two)
        self.uif.Button3.pressed.connect(self.btn_three)
        self.uif.Button4.pressed.connect(self.btn_four)
        self.uif.Button5.pressed.connect(self.btn_five)
        self.uif.Button6.pressed.connect(self.btn_six)
        self.uif.Button7.pressed.connect(self.btn_seven)
        self.uif.Button8.pressed.connect(self.btn_eight)
        self.uif.Button9.pressed.connect(self.btn_nine)
        self.uif.Button0.pressed.connect(self.btn_zero)
        self.uif.ButtonEnter.pressed.connect(self.btn_enter)
        self.uif.ButtonClear.pressed.connect(self.btn_clear)

    def btn_one(self):
        str = self.uif.SetTemp.text()
        str += '1'
        self.uif.SetTemp.setText(str)

    def btn_two(self):
        str = self.uif.SetTemp.text()
        str += '2'
        self.uif.SetTemp.setText(str)

    def btn_three(self):
        str = self.uif.SetTemp.text()
        str += '3'
        self.uif.SetTemp.setText(str)

    def btn_four(self):
        str = self.uif.SetTemp.text()
        str += '4'
        self.uif.SetTemp.setText(str)

    def btn_five(self):
        str = self.uif.SetTemp.text()
        str += '5'
        self.uif.SetTemp.setText(str)

    def btn_six(self):
        str = self.uif.SetTemp.text()
        str += '6'
        self.uif.SetTemp.setText(str)

    def btn_seven(self):
        str = self.uif.SetTemp.text()
        str += '7'
        self.uif.SetTemp.setText(str)

    def btn_eight(self):
        str = self.uif.SetTemp.text()
        str += '8'
        self.uif.SetTemp.setText(str)

    def btn_nine(self):
        str = self.uif.SetTemp.text()
        str += '9'
        self.uif.SetTemp.setText(str)

    def btn_zero(self):
        str = self.uif.SetTemp.text()
        str += '0'
        self.uif.SetTemp.setText(str)

    def btn_clear(self):
        str = ''
        self.uif.SetTemp.setText(str)

    def btn_enter(self):
        str = self.uif.SetTemp.text()

app = QtWidgets.QApplication(sys.argv)
Cont = Controller()
Cont.show()
app.exec_()
