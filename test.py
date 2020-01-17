from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('test.ui', self) # Load the .ui file
        
        button_plus = self.findChild(QtWidgets.QPushButton, "temp_plus")
        button_plus.clicked.connect(self.button_pressed)


        button_minus = self.findChild(QtWidgets.QPushButton, "temp_minus")
        button_minus.clicked.connect(self.button_pressed)

        self.show() # Show the GUI

    def button_pressed(self):
        print("Button pressed")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()