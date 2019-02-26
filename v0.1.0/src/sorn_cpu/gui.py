import sys
from PyQt4 import QtGui, QtCore


class SORNWindow(QtGui.QMainWindow):

    # Init
    def __init__(self):
        super(SORNWindow,self).__init__()

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PySORN",)
        self.setWindowIcon(QtGui.QIcon('logo.png'))


        # Toolbars in the main menu
        extractAction = QtGui.QAction("&New Project", self)
        extractAction.setShortcut("Ctrl+N")
        extractAction.setStatusTip(" Navigate to simulation main menu")
        extractAction.triggered.connect(self.close_application)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    # Views
    def home(self):

        btn1 = QtGui.QPushButton('Simulate',self)
        # btn1.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn1.clicked.connect(self.close_application)
        btn1.resize(btn1.sizeHint())
        btn1.move(50,100)
        btn2 = QtGui.QPushButton('Train',self)
        btn2.clicked.connect(self.close_application)
        btn2.resize(btn2.sizeHint())
        btn2.move(200, 100)

        # Toolbar in main menu home

        extractAction = QtGui.QAction(QtGui.QIcon("logo.png",'Simulate the Network',self))
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar(" Simulation")
        self.toolBar.addAction(extractAction)

        self.show()

    # Event handlers
    def close_application(self):
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = SORNWindow()
    sys.exit(app.exec_())


run()