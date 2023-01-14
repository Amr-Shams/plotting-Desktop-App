from PySide2.QtWidgets import (QApplication,QLabel,QMessageBox,
    QPushButton,QWidget,QDoubleSpinBox,QVBoxLayout,QHBoxLayout, QLineEdit,QDesktopWidget,QMainWindow)
from PySide2.QtGui import QFont
from PySide2 import QtGui
from PySide2 import QtCore
from error import Error_handler
import numpy as np
import re
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.view = FigureCanvas(Figure(figsize=(7, 7)))
        # adjust the height based on the parent height to be blow it 
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

    def plotting(self,x,y):
            self.axes.plot(x,y)
            self.view.draw()