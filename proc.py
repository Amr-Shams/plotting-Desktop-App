from PySide2.QtWidgets import QApplication, QWidget,QPushButton
import sys
from firstpage import inputing

app=QApplication(sys.argv)
w=inputing()
w.show()
sys.exit(app.exec_())