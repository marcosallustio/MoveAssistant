import os
import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets

from AStar import findLocationsPath
from LocationUtilities import Location, loadLocations
ROOT_DIR = os.path.dirname(os.path.dirname((os.path.abspath("amtab"))))
sys.path.append(ROOT_DIR + '\\amtab\\app')
MAP_FILE_PATH = ROOT_DIR + "\\utilities\\fermate.csv"

class Ui_Dialog_FindUs(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(820, 550)
        Dialog.setStyleSheet("background-color: rgb(255,184,17);")

        self.comboBoxStart = QtWidgets.QComboBox(Dialog)
        self.comboBoxStart.setGeometry(QtCore.QRect(130, 90, 250, 31))
        self.comboBoxStart.setStyleSheet("background-color: rgb(255,255,255);")
        self.comboBoxStart.setObjectName("comboBoxStart")
        self.comboBoxGoal = QtWidgets.QComboBox(Dialog)
        self.comboBoxGoal.setGeometry(QtCore.QRect(530, 90, 281, 31))
        self.comboBoxGoal.setStyleSheet("background-color: rgb(255,255,255);")
        self.comboBoxGoal.setObjectName("comboBoxGoal")

        for p in self.pointsSet:
            self.comboBoxStart.addItem(p)

        self.comboBoxGoal.addItem("Stazione Bari Centrale-Via Giuseppe Capruzzi(2)")
        self.comboBoxGoal.addItem("Bari Policlinico")
        self.comboBoxGoal.addItem("Bari Marconi")
        self.comboBoxGoal.addItem("Brigata Bari")
        self.comboBoxGoal.addItem("Bari Sud Est")
        self.comboBoxGoal.addItem("Bari Parco Sud")
        self.comboBoxGoal.addItem("Bari Quintino Sella")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(280, 30, 341, 31))
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")

        font.setPointSize(12)
        self.labelStart = QtWidgets.QLabel(Dialog)
        self.labelStart.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.labelStart.setFont(font)
        self.labelStart.setObjectName("labelStart")
        self.labelGoal = QtWidgets.QLabel(Dialog)
        self.labelGoal.setGeometry(QtCore.QRect(400, 90, 121, 31))
        self.labelGoal.setFont(font)
        self.labelGoal.setObjectName("labelGoal")

        self.pushButtonSearch = QtWidgets.QPushButton(Dialog)
        self.pushButtonSearch.setGeometry(QtCore.QRect(280, 160, 281, 31))
        self.pushButtonSearch.setAutoDefault(False)
        self.pushButtonSearch.setStyleSheet("background-color: white")
        self.pushButtonSearch.setObjectName("pushButton")

        font.setPointSize(10)
        self.commandLinkButtonViewBrowser = QtWidgets.QPushButton(Dialog)
        self.commandLinkButtonViewBrowser.setGeometry(QtCore.QRect(260, 500, 341, 41))
        self.commandLinkButtonViewBrowser.setAutoDefault(False)
        self.commandLinkButtonViewBrowser.setFont(font)
        self.commandLinkButtonViewBrowser.setStyleSheet("background-color: white")
        self.commandLinkButtonViewBrowser.setObjectName("commandLinkButtonViewBrowser")

        font.setPointSize(12)
        self.labelCost = QtWidgets.QLabel(Dialog)
        self.labelCost.setGeometry(QtCore.QRect(240, 460, 491, 41))
        self.labelCost.setFont(font)
        self.labelCost.setObjectName("labelCost")

        self.pushButtonMapView = QtWidgets.QPushButton(Dialog)
        self.pushButtonMapView.setGeometry(QtCore.QRect(280, 210, 291, 221))
        self.pushButtonMapView.setText("")
        self.pushButtonMapView.setObjectName("pushButtonMapView")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ROOT_DIR + "\\utilities\\map.png"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.pushButtonMapView.setIcon(icon)
        self.pushButtonMapView.setIconSize(QtCore.QSize(291, 221))
        self.pushButtonMapView.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButtonMapView.setToolTip("Clicca qui per visualizzare la mappa completa da browser")
        self.pushButtonMapView.setAutoDefault(False)


        self.pushButtonSearch.clicked.connect(self.searchPath)
        self.pushButtonMapView.clicked.connect(self.viewMap)
        #self.pushButtonGoBack.clicked.connect(Dialog.close)
        self.commandLinkButtonViewBrowser.hide()  # Viene mostrato solo dopo aver premuto il tasto di ricerca

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.commandLinkButtonViewBrowser.clicked.connect(self.openTab)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Come raggiungere una stazione"))

        # Agguiunta combo box di partenza
        i = 0
        for p in self.pointsSet:
            self.comboBoxStart.setItemText(i, _translate("Dialog", p))
            i = i + 1
            # Aggiunta combo box di destinazione
        self.comboBoxGoal.setItemText(0, _translate("Dialog", "Bari Centrale"))
        self.comboBoxGoal.setItemText(1, _translate("Dialog", "Bari Policlinico"))
        self.comboBoxGoal.setItemText(2, _translate("Dialog", "Bari Marconi"))
        self.comboBoxGoal.setItemText(3, _translate("Dialog", "Brigata Bari"))
        self.comboBoxGoal.setItemText(4, _translate("Dialog", "Bari Sud Est"))
        self.comboBoxGoal.setItemText(5, _translate("Dialog", "Bari Parco Sud"))
        self.comboBoxGoal.setItemText(6, _translate("Dialog", "Bari Quintino Sella"))

        self.labelTitle.setText(_translate("Dialog", "Come raggiungere una stazione:"))
        self.labelStart.setText(_translate("Dialog", "Partenza:"))
        self.labelGoal.setText(_translate("Dialog", "Destinazione:"))
        self.pushButtonSearch.setText(_translate("Dialog", "Calcola il percorso migliore"))
        self.commandLinkButtonViewBrowser.setText(_translate("Dialog", "Visualizza il percorso"))


    def __init__(self):
        self.pointsSet = set()
        self.points = []
        self.streets = []
        self.points, self.streets = loadLocations(MAP_FILE_PATH)

        for p in self.points:
            self.pointsSet.add(p.getValue().getName())

        self.pointsSet = list(self.pointsSet)
        self.pointsSet.sort()

    def searchPath(self):

        for p in self.points:
            if p.getValue().getName() == self.comboBoxStart.currentText():
                start = p
            if p.getValue().getName() == self.comboBoxGoal.currentText():
                dest = p
        cost = findLocationsPath(Location(start.getValue().getX(), start.getValue().getY(), start.getValue().getName()),
                                 Location(dest.getValue().getX(), dest.getValue().getY(), dest.getValue().getName()),
                                 MAP_FILE_PATH)
        self.labelCost.setText("La lunghezza del percorso è di " + str(cost) + " metri.")
        self.commandLinkButtonViewBrowser.show()



    def viewMap(self):
        webbrowser.open_new_tab("mymap.html")

    def openTab(self):
        webbrowser.open_new_tab("resultmap.html")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog_FindUs()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
