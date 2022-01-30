
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mainwindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.order_path = QtWidgets.QLineEdit(self.frame)
        self.order_path.setMinimumSize(QtCore.QSize(0, 25))
        self.order_path.setObjectName("order_path")
        self.horizontalLayout_5.addWidget(self.order_path)
        self.btn_open = QtWidgets.QPushButton(self.frame)
        self.btn_open.setEnabled(True)
        self.btn_open.setMinimumSize(QtCore.QSize(120, 25))
        self.btn_open.setStyleSheet("QPushButton{border-radius:15px; background-color: rgb(154, 153, 150)}\n"
                                    "QPushButton:hover{color:#fff; background-color: rgb(53, 132, 228)}\n"
                                    "")
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout_5.addWidget(self.btn_open)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.remote_folder_path = QtWidgets.QLineEdit(self.frame)
        self.remote_folder_path.setMinimumSize(QtCore.QSize(0, 25))
        self.remote_folder_path.setObjectName("remote_folder_path")
        self.horizontalLayout_6.addWidget(self.remote_folder_path)
        self.btn_folder_select = QtWidgets.QPushButton(self.frame)
        self.btn_folder_select.setMinimumSize(QtCore.QSize(120, 25))
        self.btn_folder_select.setStyleSheet("QPushButton{border-radius:20px; background-color: rgb(154, 153, 150)}\n"
                                             "QPushButton:hover{color:#fff; background-color: rgb(53, 132, 228)}")
        self.btn_folder_select.setObjectName("btn_folder_select")
        self.horizontalLayout_6.addWidget(self.btn_folder_select)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.order_id = QtWidgets.QTextEdit(self.frame)
        self.order_id.setMinimumSize(QtCore.QSize(0, 30))
        self.order_id.setMaximumSize(QtCore.QSize(265, 30))
        self.order_id.setObjectName("order_id")
        self.horizontalLayout.addWidget(self.order_id)
        self.id_select = QtWidgets.QSpinBox(self.frame)
        self.id_select.setMaximum(9999)
        self.id_select.setMinimumSize(QtCore.QSize(60, 0))
        self.id_select.setMaximumSize(QtCore.QSize(50, 30))
        self.id_select.setObjectName("id_select")
        self.horizontalLayout.addWidget(self.id_select)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.kds_station = QtWidgets.QTextEdit(self.frame)
        self.kds_station.setMinimumSize(QtCore.QSize(0, 25))
        self.kds_station.setMaximumSize(QtCore.QSize(260, 30))
        self.kds_station.setObjectName("kds_station")
        self.horizontalLayout_2.addWidget(self.kds_station)
        self.kds_station_select = QtWidgets.QSpinBox(self.frame)
        self.kds_station_select.setMaximum(9999)
        self.kds_station_select.setMinimumSize(QtCore.QSize(60, 0))
        self.kds_station_select.setMaximumSize(QtCore.QSize(100, 30))
        self.kds_station_select.setObjectName("kds_station_select")
        self.horizontalLayout_2.addWidget(self.kds_station_select)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.transtype = QtWidgets.QTextEdit(self.frame)
        self.transtype.setMinimumSize(QtCore.QSize(0, 30))
        self.transtype.setMaximumSize(QtCore.QSize(260, 30))
        self.transtype.setObjectName("transtype")
        self.horizontalLayout_3.addWidget(self.transtype)
        self.transtype_select = QtWidgets.QSpinBox(self.frame)
        self.transtype_select.setMaximum(9999)
        self.transtype_select.setMinimumSize(QtCore.QSize(60, 0))
        self.transtype_select.setMaximumSize(QtCore.QSize(50, 30))
        self.transtype_select.setObjectName("transtype_select")
        self.horizontalLayout_3.addWidget(self.transtype_select)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.textEdit_4.setMaximumSize(QtCore.QSize(260, 30))
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_4.addWidget(self.textEdit_4)
        self.order_status_select = QtWidgets.QSpinBox(self.frame)
        self.order_status_select.setMaximum(9999)
        self.order_status_select.setMinimumSize(QtCore.QSize(60, 0))
        self.order_status_select.setMaximumSize(QtCore.QSize(50, 30))
        self.order_status_select.setObjectName("order_status_select")
        self.horizontalLayout_4.addWidget(self.order_status_select)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.reset_order = QtWidgets.QPushButton(self.frame)
        self.reset_order.setMinimumSize(QtCore.QSize(120, 25))
        self.reset_order.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.reset_order.setStyleSheet("QPushButton{border-radius:20px; background-color: rgb(154, 153, 150)}\n"
                                       "QPushButton:hover{color:#fff; background-color: rgb(53, 132, 228)}")
        self.reset_order.setObjectName("save_order")
        self.verticalLayout.addWidget(self.reset_order)

        # Btn Send Order
        self.send_order = QtWidgets.QPushButton(self.frame)
        self.send_order.setMinimumSize(QtCore.QSize(120, 25))
        self.send_order.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.send_order.setStyleSheet("QPushButton{border-radius:20px; background-color: rgb(154, 153, 150)}\n"
                                      "QPushButton:hover{color:#fff; background-color: rgb(53, 132, 228)}")
        self.send_order.setObjectName("send_order")
        self.verticalLayout.addWidget(self.send_order)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7.addWidget(self.frame)

        # Btn Send Order Api
        self.send_order_api = QtWidgets.QPushButton(self.frame)
        self.send_order_api.setMinimumSize(QtCore.QSize(120, 25))
        self.send_order_api.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.send_order_api.setStyleSheet("QPushButton{border-radius:20px; background-color: rgb(154, 153, 150)}\n"
                                      "QPushButton:hover{color:#fff; background-color: rgb(53, 132, 228)}")
        self.send_order_api.setObjectName("send_order_api")
        self.verticalLayout.addWidget(self.send_order_api)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><img src=\"/home/jaydev/Desktop/order_send/lci.png\"/></p><p align=\"center\">ORDER SEND</p></body></html>"))
        self.order_path.setPlaceholderText(_translate("MainWindow", "Select Order.xml"))
        self.btn_open.setText(_translate("MainWindow", "Open Order.xml"))
        self.remote_folder_path.setPlaceholderText(_translate("MainWindow", "Select Remote Folder"))
        self.btn_folder_select.setText(_translate("MainWindow", "Remote Folder"))
        self.label_2.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">EDIT ORDER</p></body></html>"))
        self.order_id.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ORDER ID</p></body></html>"))
        self.kds_station.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">KDS STATION</p></body></html>"))
        self.transtype.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TRANSTYPE</p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ORDER STATUS</p></body></html>"))
        self.reset_order.setText(_translate("MainWindow", "Save Order"))
        self.send_order.setText(_translate("MainWindow", "Send Order remote folder"))
        self.send_order_api.setText(_translate("MainWindow", "Send Order Api"))
