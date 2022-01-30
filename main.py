import json
import shutil
import xml.etree.ElementTree as ET
import requests
import xmltodict as xmltodict
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from ui_main import Ui_Mainwindow
from requests.exceptions import ConnectionError

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
        self.reset_order.clicked.connect(self.edit_order)
        self.send_order_api.clicked.connect(self.sendOrderApi)

    def select_order(self):

        self.file = QFileDialog.getOpenFileName(self, str("Select Order Xml"),
                                                '/home/jaydev/kdsServer',
                                                "", "(*.xml)")

        global file_xml, orderId, transtype, orderStatus, kdsStation
        self.file = (str(self.file)[2:39])
        self.order_path.setText(self.file)
        self.file = str(self.file)
        file_xml = self.file

        orderXML = ET.parse(file_xml)
        root = orderXML.getroot()
        filtro = "*"
        for child in root.iter(filtro):

            if child.tag == "ID":
                print(child.text)
                orderId = child.text
                print(child.text)
                self.id_select.setSpecialValueText(orderId)
                child.text = str(orderId)
                continue
            if child.tag == "TransType":
                print(child.text)
                transtype = child.text
                self.transtype_select.setSpecialValueText(transtype)
                # child.text = str(orderId)
                continue
            if child.tag == "OrderStatus":
                print(child.text)
                orderStatus = child.text
                self.order_status_select.setSpecialValueText(orderStatus)
                break

        for child in root.iter(filtro):
            if child.tag == "KDSStation":
                print(child.text)
                kdsStation = child.text
                self.kds_station_select.setSpecialValueText(kdsStation)
                break

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

    def edit_order(self):

        global newOrderFileName, orderIdObj
        serverFolder = path_remote_folder + "/"
        print("serverFolder: " + serverFolder)
        orderDefaultFileName = file_xml
        print("orderDefaultFileName: " + orderDefaultFileName)

        orderIdStart = 1
        orderIdEnds = 1

        for orderIdActual in range(orderIdStart, orderIdEnds + 1):
            newOrderFileName = "Jay_" + str(orderIdActual) + ".xml"

            print("Loading Order: " + newOrderFileName)

            orderXML = ET.parse(orderDefaultFileName)

            orderObj = orderXML.find('Order')

            orderId = orderObj.find('ID')
            print(orderId.text)
            a1 = self.id_select.value()
            print(str(a1))
            if (a1 != 0):
                orderId.text = str(a1)

            transtype = orderObj.find('TransType')
            a2 = self.transtype_select.value()
            if (a2 != 0):
                transtype.text = str(a2)

            orderItem = orderObj.find('Item')
            kdsstation = orderItem.find('KDSStation')
            listhastation = list(map(lambda x: [kdsstation] * len(orderObj), orderObj))
            print(str(listhastation))
            a3 = self.kds_station_select.value()
            if (a3 != 0):
                for orderItem in orderObj:
                    for kdsstation in orderItem:
                        kdsstation.text = str(a3)

            OrderStatus = orderObj.find('OrderStatus')
            a4 = self.order_status_select.value()
            if (a4 != 0):
                OrderStatus.text = str(a4)

            # Save the new orderset
            orderXML.write(newOrderFileName)
            print("Save the new order")

    def send_order_xml(self):
        serverFolder = path_remote_folder + "/"
        print("serverFolder: " + serverFolder)
        orderDefaultFileName = file_xml
        print("orderDefaultFileName: " + orderDefaultFileName)

        orderIdStart = 1
        orderIdEnds = 1

        for orderIdActual in range(orderIdStart, orderIdEnds + 1):
            global remoteFolder
            newOrderFileName = "Jay_" + str(orderIdActual) + ".xml"

            # Move the new order to Server folder
            shutil.move(newOrderFileName, serverFolder + newOrderFileName)
            remoteFolder = serverFolder + newOrderFileName
            print("SMove the new order to Server folder")

    def sendOrderApi(self):
        print("SEND ORDER API")
        try:
            api_url = "https://dev.kdsgo.com/api/orders/new"

            tok = {
                'token': "9097f2ee3cd45a766ab43bb1db501e09a96a3281646d8a92ff89a8a578b0113b"
                }

            print(str(remoteFolder))
            with open(remoteFolder) as xml_file:
                data = xmltodict.parse(xml_file.read())
                json_data = json.dumps(data)

            with open("data.json", "r+") as json_file:
                json_file.write(json_data)

                print(api_url, json_file, tok)
                r = requests.post(api_url, json_file, tok)
                print(r)
        except ConnectionError as e:  # This is the correct syntax
                print("Request Error: "+e)

        return requests


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
