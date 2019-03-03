import sys
from PyQt4 import QtGui, QtCore

class SORNModelWindow(QtGui.QMainWindow):

    # Init
    def __init__(self):

        super(SORNModelWindow,self).__init__()

        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("PySORN")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
        self.model_home()


    def model_home(self):

        # Logo
        logo = QtGui.QLabel(self)
        logo.setPixmap(QtGui.QPixmap("logo2.png"))
        logo.setScaledContents(True)
        logo.resize(logo.sizeHint())
        logo.move(0,10)

        # SORN Model 1 Checkbox
        self.sorn1CheckBox = QtGui.QCheckBox('SORN Network Alpha', self)
        self.sorn1CheckBox.move(75,250)
        self.sorn1CheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.sorn1CheckBox.resize(self.sorn1CheckBox.sizeHint())
        self.sorn1CheckBox.stateChanged.connect(self.sorn1_action_menu)
        
        # SORN Model 2 CheckBox
        self.sorn2CheckBox = QtGui.QCheckBox('SORN Network Beta', self)
        self.sorn2CheckBox.move(75,300)
        self.sorn2CheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.sorn2CheckBox.resize(self.sorn2CheckBox.sizeHint())
        self.sorn2CheckBox.stateChanged.connect(self.sorn2_action_menu)

        self.setStyleSheet("background-color: gray;")
        self.show()


    # Event Handlers
    def sorn1_action_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('SORN Alpha Menu')

            self.sorn2CheckBox.setChecked(False)

            self.sorn1ActionMenu = SORN1ActionWindow()

            self.sorn1ActionMenu.show()

        elif state != QtCore.Qt.Checked:

            self.sorn1ActionMenu.close()

        else:
            pass

    def sorn2_action_menu(self,state):
        
        if state == QtCore.Qt.Checked:

            print('SORN Beta Menu')

            self.sorn1CheckBox.setChecked(False)


            self.sorn2ActionMenu = SORN2ActionWindow()

            self.sorn2ActionMenu.show()

        elif state != QtCore.Qt.Checked:

            self.sorn2ActionMenu.close()

        else:
            pass


class SORN1ActionWindow(QtGui.QMainWindow):

    # Init
    def __init__(self):
        super(SORN1ActionWindow,self).__init__()

        self.setGeometry(550, 50, 500, 500)
        self.setWindowTitle("SORN Alpha", )
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
        self.home()

    # Views
    def home(self):

        # Logo
        logo = QtGui.QLabel(self)
        logo.setPixmap(QtGui.QPixmap("logo2.png"))
        logo.setScaledContents(True)
        logo.resize(logo.sizeHint())
        logo.move(0,10)

        # Simulation Checkbox
        self.simulateCheckBox = QtGui.QCheckBox('Network Simulation', self)
        self.simulateCheckBox.move(75,250)
        self.simulateCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.simulateCheckBox.resize(self.simulateCheckBox.sizeHint())
        self.simulateCheckBox.stateChanged.connect(self.simulate_menu)
        
        # Training CheckBox
        self.trainCheckBox = QtGui.QCheckBox('Network Training', self)
        self.trainCheckBox.move(75,300)
        self.trainCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.trainCheckBox.resize(self.trainCheckBox.sizeHint())
        self.trainCheckBox.stateChanged.connect(self.train_menu)

        # Analysis CheckBox
        self.analysisCheckBox = QtGui.QCheckBox('Network Analysis', self)
        self.analysisCheckBox.move(75,350)
        self.analysisCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.analysisCheckBox.resize(self.analysisCheckBox.sizeHint())
        self.analysisCheckBox.stateChanged.connect(self.analysis_menu)


        # Exit Button
        self.btn2 = QtGui.QPushButton('Exit', self)
        self.btn2.setStyleSheet('font-size: 15pt; font-family: Courier;')
        self.btn2.clicked.connect(self.exit_question)
        self.btn2.setStyleSheet('background-color: green; color:white; font-size: 15pt; font-family: Courier;')
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(375, 425)


        # Toolbar in main menu home

        # extractAction = QtGui.QAction(QtGui.QIcon("logo.png"), 'Simulate the Network', self)
        # extractAction.triggered.connect(self.simulate_menu)
        # self.toolBar = self.addToolBar(" Simulation")
        # self.toolBar.addAction(extractAction)

        self.setStyleSheet("background-color: gray;")
        self.show()

    # Event handlers

    def create_project(self):

        # Initiate SORNWindow in new window
        #TODO: Add Menu tool bars  
        pass


    def choose_model(self):

        pass


    def exit_question(self):

            self.setStyleSheet("background-color: gray;")
            choice = QtGui.QMessageBox.question(self,' QUIT ',
                                                "Are you sure, you want to quit", 
                 
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

            if choice == QtGui.QMessageBox.Yes:

                self.close_application()   # sys.exit()
            
            else: self.setStyleSheet("background-color: gray;")

    def close_application(self):
        
        sys.exit()

    def create_project(self):

        # Trigger the same class to pop in new window
        pass

    def simulate_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('Initiating Simulation')

            self.trainCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)

            self.simulateHome.show()

        else: pass


    def train_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('Initiating Training Phase')

            self.simulateCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)

            self.trainHome.show()

        else: pass


    def analysis_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('Initiatialized SORN Analysis API')

            self.simulateCheckBox.setChecked(False)
            self.trainCheckBox.setChecked(False)
            

            self.analysisHome.show()

        else: pass

    def train(self):
        pass

    def update_config(self):
        pass

########################################################################################################################################


class SORN2ActionWindow(QtGui.QMainWindow):

    # Init
    def __init__(self):
        super(SORN2ActionWindow, self).__init__()

        self.setGeometry(550, 50, 500, 500)
        self.setWindowTitle("SORN Beta", )
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
        self.home()

    # Views
    def home(self):

        # Logo
        logo = QtGui.QLabel(self)
        logo.setPixmap(QtGui.QPixmap("logo2.png"))
        logo.setScaledContents(True)
        logo.resize(logo.sizeHint())
        logo.move(0,10)

        # Simulation Checkbox
        self.simulateCheckBox = QtGui.QCheckBox('Network Simulation', self)
        self.simulateCheckBox.move(75,250)
        self.simulateCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.simulateCheckBox.resize(self.simulateCheckBox.sizeHint())
        self.simulateCheckBox.stateChanged.connect(self.simulate_menu)
        
        # Training CheckBox
        self.trainCheckBox = QtGui.QCheckBox('Network Training', self)
        self.trainCheckBox.move(75,300)
        self.trainCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.trainCheckBox.resize(self.trainCheckBox.sizeHint())
        self.trainCheckBox.stateChanged.connect(self.train_menu)

        # Analysis CheckBox
        self.analysisCheckBox = QtGui.QCheckBox('Network Analysis', self)
        self.analysisCheckBox.move(75,350)
        self.analysisCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.analysisCheckBox.resize(self.analysisCheckBox.sizeHint())
        self.analysisCheckBox.stateChanged.connect(self.analysis_menu)


        # Exit Button
        self.btn2 = QtGui.QPushButton('Exit', self)
        self.btn2.setStyleSheet('font-size: 15pt; font-family: Courier;')
        self.btn2.clicked.connect(self.exit_question)
        self.btn2.setStyleSheet('background-color: green; color:white; font-size: 15pt; font-family: Courier;')
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(375, 425)


        # Toolbar in main menu home

        # extractAction = QtGui.QAction(QtGui.QIcon("logo.png"), 'Simulate the Network', self)
        # extractAction.triggered.connect(self.simulate_menu)
        # self.toolBar = self.addToolBar(" Simulation")
        # self.toolBar.addAction(extractAction)

        self.setStyleSheet("background-color: gray;")
        self.show()

    # Event handlers

    def create_project(self):

        # Initiate SORNWindow in new window
        #TODO: Add Menu tool bars  
        pass


    def choose_model(self):

        pass


    def exit_question(self):

            self.setStyleSheet("background-color: gray;")
            choice = QtGui.QMessageBox.question(self,' QUIT ',
                                                "Are you sure, you want to quit", 
                 
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

            if choice == QtGui.QMessageBox.Yes:

                self.close_application()   # sys.exit()
            
            else: self.setStyleSheet("background-color: gray;")

    def close_application(self):
        
        sys.exit()

    def create_project(self):

        # Trigger the same class to pop in new window
        pass

    def simulate_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('Initiating Simulation')

            self.trainCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)

            self.simulateHome.show()

        else: pass


    def train_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('Initiating Training Phase')

            self.simulateCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)

            self.trainHome.show()

        else: pass


    def analysis_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('Initiatialized SORN Analysis API')

            self.simulateCheckBox.setChecked(False)
            self.trainCheckBox.setChecked(False)
            

            self.analysisHome.show()

        else: pass

    def train(self):
        pass

    def update_config(self):
        pass

###############################################################################################################################################


class SimulateMenu(QtGui.QMainWindow):

    # Init
    def __init__(self):
        super(SimulateMenu, self).__init__()

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("SORN Simulation", )
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # Toolbars in the main menu

        self.home()

    # Views
    def home(self):
        btn1 = QtGui.QPushButton('Simulate', self)
        btn1.clicked.connect(self.simulate)
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 100)


        btn2 = QtGui.QPushButton('Train', self)
        btn2.clicked.connect(self.train)
        btn2.resize(btn2.sizeHint())
        btn2.move(200, 100)


        btn2 = QtGui.QPushButton('Exit', self)
        btn2.clicked.connect(self.exit_question)
        btn2.resize(btn2.sizeHint())
        btn2.move(400, 400)

        self.show()

    def simulate(self):
        pass


class TrainMenu(QtGui.QMainWindow):

    # Init
    def __init__(self):
        super(TrainMenu, self).__init__()

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("SORN Simulation", )
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # Toolbars in the main menu

        self.home()

    # Views
    def home(self):
        btn1 = QtGui.QPushButton('Simulate', self)
        btn1.clicked.connect(self.simulate)
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 100)


        btn2 = QtGui.QPushButton('Train', self)
        btn2.clicked.connect(self.train)
        btn2.resize(btn2.sizeHint())
        btn2.move(200, 100)


        btn2 = QtGui.QPushButton('Exit', self)
        btn2.clicked.connect(self.exit_question)
        btn2.resize(btn2.sizeHint())
        btn2.move(400, 400)

        self.show()

    def train(self):
        pass

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = SORNModelWindow()
    # GUI = SORN1ActionWindow()
    # GUI = SORN2ActionWindow()
    sys.exit(app.exec_())


if __name__== '__main__':

    run()

