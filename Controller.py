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
        value = self.uif.SetTemp.text()
        value += '1'
        self.uif.SetTemp.setText(value)

    def btn_two(self):
        value = self.uif.SetTemp.text()
        value += '2'
        self.uif.SetTemp.setText(value)

    def btn_three(self):
        value = self.uif.SetTemp.text()
        value += '3'
        self.uif.SetTemp.setText(value)

    def btn_four(self):
        value = self.uif.SetTemp.text()
        value += '4'
        self.uif.SetTemp.setText(value)

    def btn_five(self):
        value = self.uif.SetTemp.text()
        value += '5'
        self.uif.SetTemp.setText(value)

    def btn_six(self):
        value = self.uif.SetTemp.text()
        value += '6'
        self.uif.SetTemp.setText(value)

    def btn_seven(self):
        value = self.uif.SetTemp.text()
        value += '7'
        self.uif.SetTemp.setText(value)

    def btn_eight(self):
        value = self.uif.SetTemp.text()
        value += '8'
        self.uif.SetTemp.setText(value)

    def btn_nine(self):
        value = self.uif.SetTemp.text()
        value += '9'
        self.uif.SetTemp.setText(value)

    def btn_zero(self):
        value = self.uif.SetTemp.text()
        value += '0'
        self.uif.SetTemp.setText(value)

    def btn_clear(self):
        value = ''
        self.uif.SetTemp.setText(value)

    def btn_enter(self):
        self.uif.SetTemp.text()

app = QtWidgets.QApplication(sys.argv)
Cont = Controller()
Cont.show()
app.exec_()
# this is the new last line.  This file had an _
