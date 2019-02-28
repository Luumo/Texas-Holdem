from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import *
from PyQt5.QtWidgets import *
import sys
from cardlib import *


class MainWindow(QGroupBox):
    def __init__(self):
        super().__init__("Main window")  # Call the QWidget initialization as well!

        # creates widgets
        cv = ControlView()
        pv1 = PlayerView()
        pv2 = PlayerView()
        tv = TableView()

        # add horizontal widgets
        hbox = QHBoxLayout()
        hbox.addWidget(pv1)
        hbox.addWidget(pv2)
        hbox.addWidget(cv)
        # add vertical widgets
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(tv)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(500, 300, 1000, 500)
        self.setWindowTitle('Poker Game')


class ControlView(QGroupBox):
    def __init__(self):
        super().__init__("Control View")  # Call the QWidget initialization as well!

        #Create buttons
        betButton = QPushButton("Bet")
        foldButton = QPushButton("Fold")
        raiseButton = QPushButton("Raise")
        checkButton = QPushButton("Check")
        betAmmount = QLineEdit()

        # arrange widgets vertically
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        # add widgets
        vbox.addWidget(betAmmount)
        vbox.addWidget(betButton)
        vbox.addWidget(foldButton)
        vbox.addWidget(raiseButton)
        vbox.addWidget(checkButton)

        # Arrange horizontally
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)

        self.setLayout(hbox)


class PlayerView(QGroupBox):
    def __init__(self):
        super().__init__("Player 1")  # Call the QWidget initialization as well!

        # widgets
        valueLabel = QLabel("Value")
        cardView = QLabel("Two Cards")
        # arrange vertically
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(valueLabel)
        vbox.addWidget(cardView)
        # arrange horizontally
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)

        self.setLayout(hbox)


class TableView(QGroupBox):
    def __init__(self):
        super().__init__("Table View")
        # widgets
        cardLabels = QLabel("Flop, River, Turn")
        # arrange horizontally
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(cardLabels)
        # arrange vertically
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


class GameState:
    def __init__(self):
        pass

    def cards_on_table(self):
        pass

    def the_pot(self):
        pass

    def fold(self):
        pass

    def call(self):
        pass

    def bet(self, bet_amount):
        pass


class Player:
    def __init__(self, name):
        self.name = name
        self.credits = 100
        self.cards = ['Qs', 'AD', '7C']
        self.folded = False

    def active(self):
        return self.credits > 0 and not self.folded




app = QApplication(sys.argv)
win = MainWindow()

win.show()
app.exec_()
