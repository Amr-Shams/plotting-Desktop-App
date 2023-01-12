from PySide2.QtWidgets import (QApplication,QLabel,QMessageBox,
    QPushButton,QWidget,QDoubleSpinBox,QVBoxLayout,QHBoxLayout, QLineEdit,QDesktopWidget)
from PySide2.QtGui import QFont
from PySide2 import QtGui
from PySide2 import QtCore
from error import Error_handler
import re
XRange=(-1000,1000)
class inputing(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.func=QVBoxLayout()
        self.e=Error_handler()
        self.rep={'^':'**','cos':'np.cos','sin':'np.sin','sqrt':'np.sqrt','exp':'np.exp','x':'x','+':'+','-':'-','/':'/'}
        self.setWindowTitle("Input function")
        self.name_label(50,"Function",self.func,100,100)
        self.line=QLineEdit(self)
        self.line.resize(100,100)
        self.line.adjustSize()
        self.line.setStyleSheet("color: red;""background-color: black;""selection-color: yellow;""selection-background-color: blue;")
        # the input to min and max
        self.value_layout=QHBoxLayout()
        self.define_MaxMin()
        self.value_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.func.addWidget(self.line)
        self.func.addLayout(self.value_layout)
       
        # add the button 
        plot_button=QPushButton("Plot")
        plot_button.clicked.connect(self.plot_clicked)
        self.mini.valueChanged.connect(self.min_changed)
        self.maxi.valueChanged.connect(self.max_changed)


        button_layout=QVBoxLayout()
        button_layout.addWidget(plot_button)
        self.func.addWidget(plot_button)
        #self.setLayout(button_layout
        self.setLayout(self.func)
        #cneter the windwo in anyscreen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setFixedSize(250,200)
    def set_font(self,data):
        font=QFont()
        font.setPointSize(data)
        font.setBold(True)
        font.capitalization()
        return font        
    def plot_clicked(self):
            # check the input func
            try:
                y=self.convert_string_to_Func(10)
            except ValueError as e:
                self.e.input_error()
                self.line.setText("")
    def define_MaxMin(self):
        self.mini=QDoubleSpinBox(self)
        self.maxi=QDoubleSpinBox(self)
        self.mini.setRange(*XRange)
        self.maxi.setRange(*XRange)
        self.mini.setPrefix("-X: ")
        self.mini.setFont(self.set_font(15))
        self.mini.setValue(-10)
        self.maxi.setValue(10)
        self.maxi.setPrefix("+X: ")
        self.maxi.setFont(self.set_font(15))
        self.value_layout.addWidget(self.mini)
        self.value_layout.addWidget(self.maxi)
  

    def name_label(self,font_size,text,widegt,posx,posy):
        self.namelabel=QLabel()
        self.namelabel.setText(text)
        self.namelabel.setFont(self.set_font(font_size))
        self.namelabel.move(posx,posy)
        self.namelabel.resize(self.namelabel.sizeHint())
        self.namelabel.adjustSize()
        self.namelabel.setAlignment(QtCore.Qt.AlignCenter)
        widegt.addWidget(self.namelabel)
    def convert_string_to_Func(self,xvalue):
        pattren='[a-zA-Z]+'
        self.line.setText(self.line.text().lower())
        temp_string=re.findall(pattren,self.line.text())
        #convert all the letters in the text to lower case
        for word in temp_string:
            if word not in self.rep.keys():
                raise ValueError( f"{word} is not allowed in the given value\n pleas follow the pattren for the func\n a*x^n+..+c")
        string=self.line.text()
        for value, key in self.rep.items():
            string = string.replace(value, key)

        if "x" not in string:
            string = f"{string}+0*x"
        x=xvalue
        return eval(string)
    def max_changed(self):
        mini=self.mini.value()
        maxi=self.maxi.value()
        if maxi<=mini:
            self.maxi.setValue(mini+1)
            self.e.max_min(45)
            return 
    def min_changed(self):
        mini=self.mini.value()
        maxi=self.maxi.value()
        if mini>=maxi:
            self.mini.setValue(maxi-1)
            self.e.max_min(46)
            return 

    