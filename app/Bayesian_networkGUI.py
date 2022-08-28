
from PyQt5 import QtCore, QtGui, QtWidgets


from bayesian_network import gradeBayesianInference
from PathGUI import ROOT_DIR


class Ui_Dialog_predMark(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(701, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(701, 530))
        Dialog.setMaximumSize(QtCore.QSize(701, 530))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setStyleSheet("background-color: rgb(255,184,17);")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(18)
        font.setBold(True)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(30, 69, 681, 441))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")

        font.setPointSize(12)
        self.stackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget_7)
        self.stackedWidget.setObjectName("stackedWidget")

        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)

        self.pushButtonCalculate = QtWidgets.QPushButton(Dialog)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(140, 400, 421, 71))
        self.pushButtonCalculate.setFont(font)
        self.pushButtonCalculate.setAutoDefault(False)
        self.pushButtonCalculate.setStyleSheet("background-color: rgb(255,255,255);")
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 10, 701, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayoutTitle = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayoutTitle.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutTitle.setObjectName("horizontalLayoutTitle")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.labelTitlePredCrowding = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.labelTitlePredCrowding.setFont(font)
        self.labelTitlePredCrowding.setObjectName("labelTitlePredCrowding")
        self.horizontalLayoutTitle.addItem(spacerItem)
        self.horizontalLayoutTitle.addWidget(self.labelTitlePredCrowding)
        self.horizontalLayoutTitle.addItem(spacerItem1)

        font.setBold(False)
        self.groupBoxQuestions = QtWidgets.QGroupBox(self.page_1)
        self.groupBoxQuestions.setGeometry(QtCore.QRect(0, 10, 601, 300))
        self.groupBoxQuestions.setFont(font)
        self.groupBoxQuestions.setTitle("")
        self.groupBoxQuestions.setObjectName("groupBoxQuestions")

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 390, 541, 31))
        self.horizontalLayoutWidget_5.setFont(font)
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addItem(spacerItem2)

        # Creazione label domande
        font.setPointSize(11)
        self.labelHour = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelHour.setGeometry(QtCore.QRect(10, 5, 561, 31))
        self.labelHour.setFont(font)
        self.labelHour.setObjectName("labelHour")
        self.labelDay = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelDay.setGeometry(QtCore.QRect(10, 90, 561, 41))
        self.labelDay.setFont(font)
        self.labelDay.setObjectName("labelDay")
        self.labelLocation = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelLocation.setGeometry(QtCore.QRect(10, 190, 561, 21))
        self.labelLocation.setFont(font)
        self.labelLocation.setObjectName("labelLocation")


        # Creazione pulsanti domande
        font.setPointSize(11)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 541, 31))
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.rbHour0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbHour0.setFont(font)
        self.rbHour0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbHour0.setObjectName("rbHour0")
        self.rbHour1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbHour1.setFont(font)
        self.rbHour1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbHour1.setObjectName("rbHour1")
        self.rbHour2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbHour2.setFont(font)
        self.rbHour2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbHour2.setObjectName("rbHour2")


        # Raggruppanento radio buttons
        self.groupRBhour = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.groupRBhour.setContentsMargins(0, 0, 0, 0)
        self.groupRBhour.setObjectName("groupRBhour")
        self.groupRBhour.addWidget(self.rbHour0)
        self.groupRBhour.addWidget(self.rbHour1)
        self.groupRBhour.addWidget(self.rbHour2)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 130, 541, 31))
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.rbDay0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbDay0.setFont(font)
        self.rbDay0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbDay0.setObjectName("rbDay0")
        self.rbDay1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbDay1.setFont(font)
        self.rbDay1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbDay1.setObjectName("rbDay1")
        self.rbDay2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbDay2.setFont(font)
        self.rbDay2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbDay2.setObjectName("rbDay2")

        # Raggruppamento radio buttons
        self.groupRBday = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.groupRBday.setContentsMargins(0, 0, 0, 0)
        self.groupRBday.setObjectName("groupRBday")
        self.groupRBday.addWidget(self.rbDay0)
        self.groupRBday.addWidget(self.rbDay1)
        self.groupRBday.addWidget(self.rbDay2)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 220, 541, 31))
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.rbLocation0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbLocation0.setFont(font)
        self.rbLocation0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbLocation0.setObjectName("rbLocation0")
        self.rbLocation1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbLocation1.setFont(font)
        self.rbLocation1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbLocation1.setObjectName("rbLocation1")
        self.rbLocation2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbLocation2.setFont(font)
        self.rbLocation2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbLocation2.setObjectName("rbLocation2")
        self.rbLocation3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbLocation3.setFont(font)
        self.rbLocation3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbLocation3.setObjectName("rbLocation3")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 310, 541, 31))
        self.horizontalLayoutWidget_4.setFont(font)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")

        # Raggruppamento radio buttons
        self.groupRBLocation = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.groupRBLocation.setContentsMargins(0, 0, 0, 0)
        self.groupRBLocation.setObjectName("groupRBLocation")
        self.groupRBLocation.addWidget(self.rbLocation0)
        self.groupRBLocation.addWidget(self.rbLocation1)
        self.groupRBLocation.addWidget(self.rbLocation2)
        self.groupRBLocation.addWidget(self.rbLocation3)

        self.rbHour0.setChecked(True)
        self.rbDay0.setChecked(True)
        self.rbLocation0.setChecked(True)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.showResults = QtWidgets.QPlainTextEdit(self.page_2)
        self.showResults.setGeometry(QtCore.QRect(20, 10, 547, 321))
        self.showResults.setStyleSheet("background-color: rgb(255,255,255);")
        font.setFamily('Consolas')
        font.setPointSize(16)
        self.showResults.setFont(font)
        self.showResults.setReadOnly(True)
        self.showResults.setObjectName("showResults")
        self.labelLegendTitle = QtWidgets.QLabel(self.page_2)
        self.labelLegendTitle.setGeometry(QtCore.QRect(30, 340, 191, 21))
        font.setFamily('Leelawadee UI Semilight')
        font.setPointSize(13)
        self.labelLegendTitle.setFont(font)
        self.labelLegendTitle.setObjectName("labelLegendTitle")
        self.labelLegend = QtWidgets.QLabel(self.page_2)
        self.labelLegend.setGeometry(QtCore.QRect(30, 360, 500, 80))
        font.setPointSize(11)
        self.labelLegend.setFont(font)
        self.labelLegend.setObjectName("labelLegend")

        self.pushButtonGoBack = QtWidgets.QPushButton(Dialog)
        self.pushButtonGoBack.setGeometry(QtCore.QRect(15, 15, 50, 50))
        self.pushButtonGoBack.setMaximumSize(QtCore.QSize(49, 49))
        self.pushButtonGoBack.setObjectName("pushButtonGoBack")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ROOT_DIR+"\\utilities\\left-arrow.png"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.pushButtonGoBack.setStyleSheet("background-color: rgb(255,255,255);")
        self.pushButtonGoBack.setIcon(icon)
        self.pushButtonGoBack.setIconSize(QtCore.QSize(49, 49))
        self.pushButtonGoBack.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

        font.setFamily('Leelawadee UI Semilight')
        font.setPointSize(12)
        font.setBold(True)
        self.pushButtonBackToPage1 = QtWidgets.QPushButton(Dialog)
        self.pushButtonBackToPage1.hide()
        self.pushButtonBackToPage1.setGeometry(QtCore.QRect(90, 530, 421, 71))
        self.pushButtonBackToPage1.setFont(font)
        self.pushButtonBackToPage1.setAutoDefault(False)
        self.pushButtonBackToPage1.setObjectName("pushButtonGoBack")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.stackedWidget.setCurrentIndex(0)  # Seleziona la prima pagina da mostrare
        self.pushButtonGoBack.clicked.connect(self.goBack)  # commenta se effettui il run da questo file
        self.pushButtonCalculate.clicked.connect(self.predCrowding)
        self.pushButtonBackToPage1.clicked.connect(self.goBack)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Predizione affollamento Pullman"))
        self.pushButtonCalculate.setText(_translate("Dialog", "Calcola"))
        self.labelTitlePredCrowding.setText(_translate("Dialog", "Predizione affollamento Pullman"))
        self.labelHour.setText(_translate("Dialog", "In quale ora del giorno vuoi viaggiare?"))
        self.rbHour0.setText(_translate("Dialog", "non specificato"))
        self.rbHour1.setText(_translate("Dialog", "Diurna"))
        self.rbHour2.setText(_translate("Dialog", "Notturna"))
        self.labelDay.setText(_translate("Dialog", "In quale tipo di giornata vuoi viaggiare?"))
        self.rbDay0.setText(_translate("Dialog", "non specificato"))
        self.rbDay1.setText(_translate("Dialog", "Festiva"))
        self.rbDay2.setText(_translate("Dialog", "Feriale"))
        self.labelLocation.setText(_translate("Dialog", "In quale parte della città vuoi iniziare la tua corsa?"))
        self.rbLocation0.setText(_translate("Dialog", "non specificato"))
        self.rbLocation1.setText(_translate("Dialog", "Centro"))
        self.rbLocation2.setText(_translate("Dialog", "Periferia"))
        self.rbLocation3.setText(_translate("Dialog", "Z.Industriale"))
        self.showResults.setPlainText(_translate("Dialog", ""))
        self.labelLegendTitle.setText(_translate("Dialog", " "))
        self.pushButtonBackToPage1.setText(_translate("Dialog", "Torna indietro "))
        self.labelLegend.setText(_translate("Dialog",
                                            "- Crowding(0): Poco affollato\n"
                                            "- Crowding(1): Mediamente affollato\n"
                                            "- Crowding(2): Molto affollato"))

    def predCrowding(self):
        self.labelTitlePredCrowding.setText("Predizione affollamento Pullman - Risultati ")
        self.stackedWidget.setCurrentIndex(1)  # Mostra la pagina dei risultati
        self.pushButtonCalculate.hide()
        self.pushButtonBackToPage1.show()

        d_hour = {self.rbHour1: 0,
                  self.rbHour2: 1}

        d_day = {self.rbDay1: 0,
                 self.rbDay2: 1}

        d_location = {self.rbLocation1: 0,
                      self.rbLocation2: 1,
                      self.rbLocation3: 2}

        evidences = {}

        # in base alle scelte, aggiorna evidences
        for i in d_hour:
            if i.isChecked():
                evidences.update({'Hour': d_hour[i]})

        for i in d_day:
            if i.isChecked():
                evidences.update({'Day': d_day[i]})

        for i in d_location:
            if i.isChecked():
                evidences.update({'Location': d_location[i]})

        if bool(evidences) == False:
            self.showResults.setPlainText(
                'Errore.\nNon abbiamo abbastanza dati a disposizione per effettuare la predizione.Selezionare almeno uno dei parametri')
        else:
            self.res = gradeBayesianInference(evidences)
            self.showResults.setPlainText(str(gradeBayesianInference(evidences)))



    def goBack(self):
        self.labelTitlePredCrowding.setText("Predizione affollamento Pullman")
        self.pushButtonCalculate.show()
        self.pushButtonGoBack.show()
        self.pushButtonBackToPage1.hide()
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog_predMark()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
