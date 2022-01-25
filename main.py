import os
import shutil
import this
import time
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from ui_main import Ui_Mainwindow

import sys


class MainWindow(QMainWindow, Ui_Mainwindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.file = None
        self.setupUi(self)
        self.setWindowTitle("Logic Control")
        app_icon = QIcon("/home/jaydev/Desktop/order_send/lci.png")
        self.setWindowIcon(app_icon)

        self.file = ''
        self.btn_folder_select.clicked.connect(self.open_path)
        self.btn_open.clicked.connect(self.select_order)
        self.send_order.clicked.connect(self.send_order_xml)

    def select_order(self):
        self.file = QFileDialog.getOpenFileName(self, str("Select Order Xml"),
                                                '/home/jaydev/kdsServer',
                                                "", "(*.xml)")
        global file_xml
        # print(str(self.file))
        # print(str(self.file).split(",")[0])
        # print(str(self.file)[25:39])
        self.file = (str(self.file)[2:39])
        self.order_path.setText(self.file)
        self.file = str(self.file)
        file_xml = self.file

        # orderXML = ET.parse(file_xml)
        #
        # root = orderXML.getroot()
        # filtro = "*"
        # for child in root.iter(filtro):
        #     print(child.tag, child.text)
        #     if child.tag == "KDSStation":
        #         print(child.text)
        #         kdsId = child.text
        #         self.kds_station_select.setSpecialValueText(kdsId)
        #         continue
        #     if child.tag == "ID":
        #         print(child.text)
        #         orderId = child.text
        #         self.id_select.setSpecialValueText(orderId)
        #         continue
        #     if child.tag == "TransType":
        #         print(child.text)
        #         kdsId = child.text
        #         self.transtype_select.setSpecialValueText(kdsId)
        #         continue
        #     if child.tag == "OrderStatus":
        #         print(child.text)
        #         kdsId = child.text
        #         self.order_status_select.setSpecialValueText(kdsId)
        #         break

        return file_xml

    def open_path(self):
        self.file = QFileDialog.getExistingDirectory(self, str("Select Remote Folder"),
                                                     '/home/jaydev/kdsServer',
                                                     QFileDialog.ShowDirsOnly |
                                                     QFileDialog.DontResolveSymlinks)
        global path_remote_folder
        self.remote_folder_path.setText(self.file)
        self.file = str(self.file)
        path_remote_folder = self.file
        print(path_remote_folder)
        return path_remote_folder

    def send_order_xml(self):
        serverFolder = path_remote_folder + "/"
        print("serverFolder: " + serverFolder)
        orderDefaultFileName = file_xml
        print("orderDefaultFileName: " + orderDefaultFileName)

        orderIdStart = 1
        orderIdEnds = 1

        for orderIdActual in range(orderIdStart, orderIdEnds + 1):
            newOrderFileName = "order_" + str(orderIdActual) + ".xml"

            print("Loading Order: " + newOrderFileName)

            orderXML = ET.parse(orderDefaultFileName)

            orderObj = orderXML.find('Order')

            orderIdObj = orderObj.find('ID')

            orderIdObj.text = str(orderIdActual)

            # Save the new order
            orderXML.write(newOrderFileName)
            print("Save the new order")

            # Move the new order to Server folder
            shutil.move(newOrderFileName, serverFolder + newOrderFileName)
            print("SMove the new order to Server folder")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
