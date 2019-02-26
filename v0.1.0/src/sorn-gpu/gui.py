import sys
from PyQt4 import QtGui


class SORNWindow(QtGui.QMainWindow):
    def __init__(self):
        super(SORNWindow,self).__init__()

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PySORN")
        self.setWindowIcon(QtGui.QIcon(logo.png))
        self.show()


app = QtGui.QApplication(sys.argv)
GUI = SORNWindow()
sys.exit(app.exec_())


