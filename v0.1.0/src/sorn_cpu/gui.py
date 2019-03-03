import sys
from configparser import ConfigParser
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

            # self.close()
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
        msg = QtGui.QLabel(self)
        msg.setText("Choose Task")
        msg.resize(1000,100)
        msg.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        msg.move(20,10)

        # Simulation Checkbox
        self.simulateCheckBox = QtGui.QCheckBox('Network Simulation', self)
        self.simulateCheckBox.move(75,150)
        self.simulateCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.simulateCheckBox.resize(self.simulateCheckBox.sizeHint())
        self.simulateCheckBox.stateChanged.connect(self.simulate_question)
        # Training CheckBox
        self.trainCheckBox = QtGui.QCheckBox('Network Training', self)
        self.trainCheckBox.move(75,200)
        self.trainCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.trainCheckBox.resize(self.trainCheckBox.sizeHint())
        self.trainCheckBox.stateChanged.connect(self.train_question)

        # Analysis CheckBox
        self.analysisCheckBox = QtGui.QCheckBox('Network Analysis', self)
        self.analysisCheckBox.move(75,250)
        self.analysisCheckBox.setStyleSheet('color:white; font-size: 15pt; font-family: Courier;')
        self.analysisCheckBox.resize(self.analysisCheckBox.sizeHint())
        self.analysisCheckBox.stateChanged.connect(self.analysis_question)

        # Toolbar in main menu home

        # extractAction = QtGui.QAction(QtGui.QIcon("logo.png"), 'Simulate the Network', self)
        # extractAction.triggered.connect(self.simulate_menu)
        # self.toolBar = self.addToolBar(" Simulation")
        # self.toolBar.addAction(extractAction)

        self.setStyleSheet("background-color: gray;")
        self.show()

    def simulate_question(self,state):

        if state == QtCore.Qt.Checked:
            self.trainCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)
            self.setStyleSheet("background-color: gray;")
            choice = QtGui.QMessageBox.question(self,' Choose Simulation Type ',
                                                "Do you already have Simulation matrix file (.pkl) \nYES - Resume Simulation \nNo - Intiate Fresh Network Simulation", 
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
            if choice == QtGui.QMessageBox.Yes:
                print('Success')
                self.simulateMenu = AlphaResumeSimulateWindow()   
                self.simulateMenu.show()    
            else: 
                self.simulateMenu = AlphaFreshSimulateWindow()
                self.simulateMenu.show()

        elif state != QtCore.Qt.Checked:

            self.simulateMenu.close()

        else:
            pass


    def train_question(self,state):

        if state == QtCore.Qt.Checked:
            self.simulateCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)
            self.setStyleSheet("background-color: gray;")
            choice = QtGui.QMessageBox.question(self,' Choose Training Type ',
                                                "Do you already have Simulation matrix file (.pkl) \nYES - Resume Training \nNo - Intiate Fresh Network Training", 
                     
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
            if choice == QtGui.QMessageBox.Yes:
                print('Success')
                self.trainMenu = AlphaResumeTrainingWindow()   
                self.trainMenu.show()    
            else: 
                self.trainMenu = AlphaFreshTrainingWindow()
                self.trainMenu.show()

        elif state != QtCore.Qt.Checked:

            self.trainMenu.close()
        else:
            pass

    def analysis_question(self,state):

        if state == QtCore.Qt.Checked:
            self.trainCheckBox.setChecked(False)
            self.simulateCheckBox.setChecked(False)
            self.setStyleSheet("background-color: gray;")
            
            self.analysisMenu = AlphaRealtimeAnalysisWindow()   
            self.analysisMenu.show()    
            

        elif state != QtCore.Qt.Checked:

            self.analysisMenu.close()

        else:

            pass

    def close_application(self):
        
        sys.exit()



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


        # Toolbar in main menu home

        # extractAction = QtGui.QAction(QtGui.QIcon("logo.png"), 'Simulate the Network', self)
        # extractAction.triggered.connect(self.simulate_menu)
        # self.toolBar = self.addToolBar(" Simulation")
        # self.toolBar.addAction(extractAction)

        self.setStyleSheet("background-color: gray;")
        self.show()

    # Event handlers

    def simulate_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('Alpha Simulation Parameters')

            self.trainCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)

            # Trigger the question; Do you have simulation matrix? :If yes; Navigate to Resume Simulatio else Fresh Simulation
            self.simulate_question()

        elif state != QtCore.Qt.Checked:

            self.SimulateMenu.close()

        else:
            pass


    def train_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('Alpha Training Pipeline')

            self.simulateCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)

            self.simulateMenu = AlphaTrainWindow()

            self.trainMenu.show()

        elif state != QtCore.Qt.Checked:

            self.TrainMenu.close()

        else:
            pass


    def analysis_menu(self,state):

        if state == QtCore.Qt.Checked:

            print('SORN Alpha Analysis')

            self.simulateCheckBox.setChecked(False)
            self.trainCheckBox.setChecked(False)

            self.simulateMenu = AlphaAnalysisWindow()

            self.analysisMenu.show()

        elif state != QtCore.Qt.Checked:

            self.AnalysisMenu.close()

        else:
            pass


    def simulate_question(self):

        self.setStyleSheet("background-color: gray;")
        choice = QtGui.QMessageBox.question(self,' Choose Simulation Type ',
                                            "Do you already have Simulation matrix file (.pkl)", 
                 
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            self.simulateMenu = AlphaResumeSimulateWindow()   
            
        else: 
            self.simulateMenu = AlphaFreshSimulateWindow() 

    def close_application(self):
        
        sys.exit()


    # TODO
    def create_project(self):

        # Trigger the same class to pop in new window
        pass

    
    def update_config(self):
        pass

###############################################################################################################################################
#                                       DO NOT DISTURB ABOVE WINDOW CLASSES
###############################################################################################################################################


class AlphaFreshSimulateWindow(QtGui.QMainWindow):

    # Init
    def __init__(self):
        super(AlphaSimulateWindow, self).__init__()

        self.setGeometry(1050, 50, 600, 1000)
        self.setWindowTitle("SORN Alpha Simulation", )
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
        self.home()

    # Views
    def home(self):

        self.setStyleSheet("background-color: gray;")
        self.show()


    # On checkbox rise a question

    def simulation_type_check(self):

        if state == QtCore.Qt.Checked:

            print('Fresh Simulation selected')

            self.resumeSimulateCheckBox.setChecked(False)
            self.simulate_question()


    def simulate_question(self):

        self.setStyleSheet("background-color: gray;")
        choice = QtGui.QMessageBox.question(self,' Choose Simulation Type ',
                                            "Do you already have Simulation matrix file (.pkl)", 
                 
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:

            self.resume_simulate_checkbox   # sys.exit()
            
        else: self.fresh_simulate_checkbox

    # Event Handlers
    def fresh_simulate_checkbox(self,state):

        if state == QtCore.Qt.Checked:

            print('Fresh Simulation selected')

            self.resumeSimulateCheckBox.setChecked(False)

            # Views
            self.btn1 = QtGui.QPushButton('Simulate', self)
            self.btn1.setStyleSheet('font-size: 15pt; font-family: Courier;')
            self.btn1.setStyleSheet(' color:white; font-size: 15pt; font-family: Courier;')
            self.btn1.clicked.connect(self.simulate)
            self.btn1.resize(self.btn1.sizeHint())
            self.btn1.move(50, 50)


            self.btn2 = QtGui.QPushButton('Exit', self)
            self.btn2.setStyleSheet('font-size: 15pt; font-family: Courier;')
            self.btn2.setStyleSheet(' color:white; font-size: 15pt; font-family: Courier;')
            self.btn2.clicked.connect(self.exit_question)
            self.btn2.resize(self.btn2.sizeHint())
            self.move(300, 500)

            self.setStyleSheet("background-color: gray;")
            self.show()
    
        else: pass


    def resume_simulate_checkbox(self,state):
            
        if state == QtCore.Qt.Checked:

            print('Resume Simulation Selected')

            self.simulateCheckBox.setChecked(False)
            self.analysisCheckBox.setChecked(False)

            self.simulateMenu = AlphaTrainWindow()

            self.trainMenu.show()

        elif state != QtCore.Qt.Checked:

            self.TrainMenu.close()

        else:
            pass

            # Views
            self.btn1 = QtGui.QPushButton('Load matrix file', self)

            self.btn1.setStyleSheet('font-size: 15pt; font-family: Courier;')
            self.btn1.setStyleSheet(' color:white; font-size: 15pt; font-family: Courier;')
            self.btn1.clicked.connect(self.simulate)
            self.resize(self.btn1.sizeHint())
            self.move(50, 150)


            self.btn1 = QtGui.QPushButton('Simulate', self)

            self.btn1.setStyleSheet('font-size: 15pt; font-family: Courier;')
            self.btn1.setStyleSheet(' color:white; font-size: 15pt; font-family: Courier;')
            self.btn1.clicked.connect(self.simulate)
            self.btn1.resize(self.btn1.sizeHint())
            self.btn1.move(50, 900)

            self.btn2 = QtGui.QPushButton('Exit', self)
            self.btn2.setStyleSheet('font-size: 15pt; font-family: Courier;')
            self.btn2.setStyleSheet(' color:white; font-size: 15pt; font-family: Courier;')
            self.btn2.clicked.connect(self.exit_question)
            self.btn2.resize(self.btn2.sizeHint())
            self.move(400, 900)

            self.setStyleSheet("background-color: gray;")
            self.show()


    def simulate(self):
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


class AlphaTrainWindow(QtGui.QMainWindow):

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

