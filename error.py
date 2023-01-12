from PySide2.QtWidgets import (QApplication,QLabel,QMessageBox,
    QPushButton,QWidget,QDoubleSpinBox,QVBoxLayout,QHBoxLayout, QLineEdit)
from PySide2.QtGui import QFont
from PySide2.QtCore import Slot
class Error_handler:
	def	__init__(self) -> None:
		pass
	def input_error(self):
		message=QMessageBox()
		message.setMinimumSize(700,200)
		message.setWindowTitle("Errox044")
		message.setText("oops somthing wrong in the input\npleas follow the example.")
		message.setInformativeText("re-enter the function again")
		message.setIcon(QMessageBox.Warning)
		message.setDefaultButton(QMessageBox.Ok)
		return message.exec_()
	def max_min(self,value):
		message=QMessageBox()
		message.setMinimumSize(700,200)
		message.setWindowTitle(f"Errox0{value}")
		message.setText("oops somthing wrong in the max or min\npleas follow be sure Min<Max.")
		message.setInformativeText("re-enter the parameter again")
		message.setIcon(QMessageBox.Critical)
		message.setDefaultButton(QMessageBox.Ok)
		return message.exec_()