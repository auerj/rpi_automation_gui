from PyQt5 import QtWidgets, uic
import paho.mqtt.client as mqtt
import json

import sys



class Ui(QtWidgets.QDialog):
    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect("krake")


        self.target_temp_value = 20.0
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('test.ui', self) # Load the .ui file
        

        self.target_temp_label = self.findChild(QtWidgets.QLCDNumber, "target_temp")

        button_plus = self.findChild(QtWidgets.QPushButton, "temp_plus")
        button_plus.clicked.connect(self.button_plus)


        button_minus = self.findChild(QtWidgets.QPushButton, "temp_minus")
        button_minus.clicked.connect(self.button_minus)

        self.update_target_temp()

        self.show() # Show the GUI

    def button_plus(self):
        self.target_temp_value += 0.5
        self.update_target_temp()

    def button_minus(self):
        self.target_temp_value -= 0.5
        self.update_target_temp()

    def update_target_temp(self):
        self.target_temp_label.display(self.target_temp_value)
        #self.target_temp_label.repaint()
        self.client.publish("rooms/12.7/panel", json.dumps({"target_temp": self.target_temp_value}))


app = QtWidgets.QApplication(sys.argv)
window = Ui()


app.exec_()