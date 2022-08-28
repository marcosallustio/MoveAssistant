from PyQt5 import QtCore, QtGui, QtWidgets
from PathGUI import ROOT_DIR


from bayesian_network import gradeBayesianInference

class Ui_Dialog_createFile(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(701, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(701, 750))
        Dialog.setMaximumSize(QtCore.QSize(701, 750))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setStyleSheet("background-color: rgb(255,255,255);")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(18)
        #font.setKerning(True)
        font.setBold(True)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(30, 69, 681, 650))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")

        font.setPointSize(12)
        # Creazione stackedWidget (che permette di cambiare pagina, passando a quella che mostra il contenuto)
        self.stackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget_7)
        self.stackedWidget.setObjectName("stackedWidget")
        # Creazione Pagina 1 - Calcolo
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)

        self.pushButtonCalculate = QtWidgets.QPushButton(Dialog)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(140, 640, 421, 71))
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
        self.labelTitleClass = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.labelTitleClass.setFont(font)
        self.labelTitleClass.setObjectName("labelTitleClass")
        self.horizontalLayoutTitle.addItem(spacerItem)
        self.horizontalLayoutTitle.addWidget(self.labelTitleClass)
        self.horizontalLayoutTitle.addItem(spacerItem1)

        font.setBold(False)
        self.groupBoxQuestions = QtWidgets.QGroupBox(self.page_1)
        self.groupBoxQuestions.setGeometry(QtCore.QRect(0, 10, 601, 800))
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

        # Creazione label relative alle domande
        font.setPointSize(11)
        self.labelValue = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelValue.setGeometry(QtCore.QRect(10, 5, 561, 31))
        self.labelValue.setFont(font)
        self.labelValue.setObjectName("labelValue")
        self.labelMaint = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelMaint.setGeometry(QtCore.QRect(10, 90, 561, 41))
        self.labelMaint.setFont(font)
        self.labelMaint.setObjectName("labelMaint")
        self.labelSeats = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelSeats.setGeometry(QtCore.QRect(10, 190, 561, 21))
        self.labelSeats.setFont(font)
        self.labelSeats.setObjectName("labelSeats")
        self.labelTicket = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelTicket.setGeometry(QtCore.QRect(10, 280, 561, 21))
        self.labelTicket.setFont(font)
        self.labelTicket.setObjectName("labelTicket")
        self.labelPort = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelPort.setGeometry(QtCore.QRect(10, 360, 561, 21))
        self.labelPort.setFont(font)
        self.labelPort.setObjectName("labelPort")
        self.labelSafety = QtWidgets.QLabel(self.groupBoxQuestions)
        self.labelSafety.setGeometry(QtCore.QRect(10, 450, 561, 21))
        self.labelSafety.setFont(font)
        self.labelSafety.setObjectName("labelSafety")

        # Creazione bottoni relativi alle domande
        font.setPointSize(11)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 541, 31))
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.rbValue0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbValue0.setFont(font)
        self.rbValue0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbValue0.setObjectName("rbValue0")
        self.rbValue1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbValue1.setFont(font)
        self.rbValue1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbValue1.setObjectName("rbValue1")
        self.rbValue2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbValue2.setFont(font)
        self.rbValue2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbValue2.setObjectName("rbValue2")
        self.rbValue3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbValue3.setFont(font)
        self.rbValue3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbValue3.setObjectName("rbValue3")


        # Raggruppanento radio buttons
        self.groupRBvalue = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.groupRBvalue.setContentsMargins(0, 0, 0, 0)
        self.groupRBvalue.setObjectName("groupRBvalue")
        self.groupRBvalue.addWidget(self.rbValue0)
        self.groupRBvalue.addWidget(self.rbValue1)
        self.groupRBvalue.addWidget(self.rbValue2)
        self.groupRBvalue.addWidget(self.rbValue3)


        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 130, 541, 31))
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.rbMaint0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbMaint0.setFont(font)
        self.rbMaint0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbMaint0.setObjectName("rbMaint0")
        self.rbMaint1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbMaint1.setFont(font)
        self.rbMaint1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbMaint1.setObjectName("rbMaint1")
        self.rbMaint2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbMaint2.setFont(font)
        self.rbMaint2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbMaint2.setObjectName("rbMaint2")
        self.rbMaint3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbMaint3.setFont(font)
        self.rbMaint3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbMaint3.setObjectName("rbMaint3")

        # Raggruppamento radio buttons
        self.groupRBmaint = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.groupRBmaint.setContentsMargins(0, 0, 0, 0)
        self.groupRBmaint.setObjectName("groupRBmaint")
        self.groupRBmaint.addWidget(self.rbMaint0)
        self.groupRBmaint.addWidget(self.rbMaint1)
        self.groupRBmaint.addWidget(self.rbMaint2)
        self.groupRBmaint.addWidget(self.rbMaint3)


        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 220, 541, 31))
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.rbSeats0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbSeats0.setFont(font)
        self.rbSeats0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbSeats0.setObjectName("rbSeats0")
        self.rbSeats1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbSeats1.setFont(font)
        self.rbSeats1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbSeats1.setObjectName("rbSeats1")
        self.rbSeats2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbSeats2.setFont(font)
        self.rbSeats2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbSeats2.setObjectName("rbSeats2")
        self.rbSeats3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.rbSeats3.setFont(font)
        self.rbSeats3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbSeats3.setObjectName("rbSeats3")
        # Raggruppamento radio buttons
        self.groupRBseats = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.groupRBseats.setContentsMargins(0, 0, 0, 0)
        self.groupRBseats.setObjectName("groupRBseats")
        self.groupRBseats.addWidget(self.rbSeats0)
        self.groupRBseats.addWidget(self.rbSeats1)
        self.groupRBseats.addWidget(self.rbSeats2)
        self.groupRBseats.addWidget(self.rbSeats3)

        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(30, 310, 541, 31))
        self.horizontalLayoutWidget_8.setFont(font)
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.rbTicket0= QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.rbTicket0.setFont(font)
        self.rbTicket0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbTicket0.setObjectName("rbTicket0")
        self.rbTicket1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.rbTicket1.setFont(font)
        self.rbTicket1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbTicket1.setObjectName("rbTicket1")
        self.rbTicket2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.rbTicket2.setFont(font)
        self.rbTicket2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbTicket2.setObjectName("rbTicket2")

        # Raggruppamento radio buttons
        self.groupRBticket = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.groupRBticket.setContentsMargins(0, 0, 0, 0)
        self.groupRBticket.setObjectName("groupRBticket")
        self.groupRBticket.addWidget(self.rbTicket0)
        self.groupRBticket.addWidget(self.rbTicket1)
        self.groupRBticket.addWidget(self.rbTicket2)

        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(30, 400, 541, 31))
        self.horizontalLayoutWidget_9.setFont(font)
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.rbPort0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.rbPort0.setFont(font)
        self.rbPort0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbPort0.setObjectName("rbPort0")
        self.rbPort1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.rbPort1.setFont(font)
        self.rbPort1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbPort1.setObjectName("rbPort1")
        self.rbPort2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.rbPort2.setFont(font)
        self.rbPort2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbPort2.setObjectName("rbPort2")

        # Raggruppamento radio buttons
        self.groupRBport = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.groupRBport.setContentsMargins(0, 0, 0, 0)
        self.groupRBport.setObjectName("groupRBport")
        self.groupRBport.addWidget(self.rbPort0)
        self.groupRBport.addWidget(self.rbPort1)
        self.groupRBport.addWidget(self.rbPort2)

        self.horizontalLayoutWidget_10= QtWidgets.QWidget(self.groupBoxQuestions)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(30, 490, 541, 31))
        self.horizontalLayoutWidget_10.setFont(font)
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.rbSafety0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.rbSafety0.setFont(font)
        self.rbSafety0.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbSafety0.setObjectName("rbSafety0")
        self.rbSafety1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.rbSafety1.setFont(font)
        self.rbSafety1.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbSafety1.setObjectName("rbSafety1")
        self.rbSafety2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.rbSafety2.setFont(font)
        self.rbSafety2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rbSafety2.setObjectName("rbSafety2")

        # Raggruppamento radio buttons
        self.groupRBsafety = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.groupRBsafety.setContentsMargins(0, 0, 0, 0)
        self.groupRBsafety.setObjectName("groupRBsafety")
        self.groupRBsafety.addWidget(self.rbSafety0)
        self.groupRBsafety.addWidget(self.rbSafety1)
        self.groupRBsafety.addWidget(self.rbSafety2)


        # Creazione Pagina 2 - Risultati
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
        self.labelLegendTitle.setGeometry(QtCore.QRect(30, 0, 191, 21))
        font.setFamily('Leelawadee UI Semilight')
        font.setPointSize(13)
        self.labelLegendTitle.setFont(font)
        self.labelLegendTitle.setObjectName("labelLegendTitle")
        self.labelLegend = QtWidgets.QLabel(self.page_2)
        self.labelLegend.setGeometry(QtCore.QRect(30, 0, 500, 80))
        font.setPointSize(11)
        self.labelLegend.setFont(font)
        self.labelLegend.setObjectName("labelLegend")



        # Tasto per tornare alla pagina del calcolo dei voti
        font.setFamily('Leelawadee UI Semilight')
        font.setPointSize(12)
        font.setBold(True)
        self.pushButtonBackToPage1 = QtWidgets.QPushButton(Dialog)
        self.pushButtonBackToPage1.hide()
        self.pushButtonBackToPage1.setGeometry(QtCore.QRect(90, 0, 421, 71))
        self.pushButtonBackToPage1.setFont(font)
        self.pushButtonBackToPage1.setAutoDefault(False)
        self.pushButtonBackToPage1.setObjectName("pushButtonGoBack")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Azioni
        self.pushButtonCalculate.clicked.connect(self.create_file)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Classificazione"))
        self.pushButtonCalculate.setText(_translate("Dialog", "Invia"))
        self.labelTitleClass.setText(_translate("Dialog", "CLASSIFICATION"))
        self.labelValue.setText(_translate("Dialog", "Inserisci il costo del Pullman"))
        self.rbValue0.setText(_translate("Dialog", "vhigh"))
        self.rbValue1.setText(_translate("Dialog", "high"))
        self.rbValue2.setText(_translate("Dialog", "med"))
        self.rbValue3.setText(_translate("Dialog", "low"))
        self.labelMaint.setText(_translate("Dialog", "Inserisci il costo di manutenzione del Pullman"))
        self.rbMaint0.setText(_translate("Dialog", "vhigh"))
        self.rbMaint1.setText(_translate("Dialog", "high"))
        self.rbMaint2.setText(_translate("Dialog", "med"))
        self.rbMaint3.setText(_translate("Dialog", "low"))
        self.labelSeats.setText(_translate("Dialog", "Inserisci il numero di posti del Pullman"))
        self.rbSeats0.setText(_translate("Dialog", "40"))
        self.rbSeats1.setText(_translate("Dialog", "48"))
        self.rbSeats2.setText(_translate("Dialog", "62"))
        self.rbSeats3.setText(_translate("Dialog", "65more"))
        self.labelTicket.setText(_translate("Dialog", "Inserisci la possibilità di comprare il biglietto sul Pullman"))
        self.rbTicket0.setText(_translate("Dialog", "no"))
        self.rbTicket1.setText(_translate("Dialog", "yesadd"))
        self.rbTicket2.setText(_translate("Dialog", "yes"))
        self.labelPort.setText(_translate("Dialog", "Inserisci il numero di porte del Pullman"))
        self.rbPort0.setText(_translate("Dialog", "2"))
        self.rbPort1.setText(_translate("Dialog", "3"))
        self.rbPort2.setText(_translate("Dialog", "more"))
        self.labelSafety.setText(_translate("Dialog", "Inserisci il livello di sicurezza dei dispositivi per disabili"))
        self.rbSafety0.setText(_translate("Dialog", "low"))
        self.rbSafety1.setText(_translate("Dialog", "med"))
        self.rbSafety2.setText(_translate("Dialog", "high"))





    def create_file(self):
        with open("classification.txt", "w") as f:
            if self.rbValue0.isChecked() is True:
                text1 = self.rbValue0.text()
                f.write(text1)
                f.write(",")
            elif self.rbValue1.isChecked() is True:
                text1 = self.rbValue1.text()
                f.write(text1)
                f.write(",")
            elif self.rbValue2.isChecked() is True:
                text1 = self.rbValue2.text()
                f.write(text1)
                f.write(",")
            elif self.rbValue3.isChecked() is True:
                text1 = self.rbValue3.text()
                f.write(text1)
                f.write(",")

        with open("classification.txt", "a") as f:
            if self.rbMaint0.isChecked() is True:
                text2 = self.rbMaint0.text()
                f.write(text2)
                f.write(",")
            elif self.rbMaint1.isChecked() is True:
                text2 = self.rbMaint1.text()
                f.write(text2)
                f.write(",")
            elif self.rbMaint2.isChecked() is True:
                text2 = self.rbMaint2.text()
                f.write(text2)
                f.write(",")
            elif self.rbMaint3.isChecked() is True:
                text2 = self.rbMaint3.text()
                f.write(text2)
                f.write(",")

        with open("classification.txt", "a") as f:
            if self.rbSeats0.isChecked() is True:
                text3 = self.rbSeats0.text()
                f.write(text3)
                f.write(",")
            elif self.rbSeats1.isChecked() is True:
                text3 = self.rbSeats1.text()
                f.write(text3)
                f.write(",")
            elif self.rbSeats2.isChecked() is True:
                text3 = self.rbSeats2.text()
                f.write(text3)
                f.write(",")
            elif self.rbSeats3.isChecked() is True:
                text3 = self.rbSeats3.text()
                f.write(text3)
                f.write(",")

        with open("classification.txt", "a") as f:
            if self.rbTicket0.isChecked() is True:
                text4 = self.rbTicket0.text()
                f.write(text4)
                f.write(",")
            elif self.rbTicket1.isChecked() is True:
                text4 = self.rbTicket1.text()
                f.write(text4)
                f.write(",")
            elif self.rbTicket2.isChecked() is True:
                text4 = self.rbTicket2.text()
                f.write(text4)
                f.write(",")

        with open("classification.txt", "a") as f:
            if self.rbPort0.isChecked() is True:
                text5 = self.rbPort0.text()
                f.write(text5)
                f.write(",")
            elif self.rbPort1.isChecked() is True:
                text5 = self.rbPort1.text()
                f.write(text5)
                f.write(",")
            elif self.rbPort2.isChecked() is True:
                text5 = self.rbPort2.text()
                f.write(text5)
                f.write(",")

        with open("classification.txt", "a") as f:
            if self.rbSafety0.isChecked() is True:
                text6 = self.rbSafety0.text()
                f.write(text6)
            elif self.rbSafety1.isChecked() is True:
                text6 = self.rbSafety1.text()
                f.write(text6)
            elif self.rbSafety2.isChecked() is True:
                text6 = self.rbSafety2.text()
                f.write(text6)

        if (self.rbValue0.isChecked() is True or self.rbValue1.isChecked() is True or self.rbValue2.isChecked() is True or self.rbValue3.isChecked() is True) and (self.rbMaint0.isChecked() is True or self.rbMaint1.isChecked() is True or self.rbMaint2.isChecked() is True or self.rbMaint3.isChecked() is True) and (self.rbSeats0.isChecked() is True or self.rbSeats1.isChecked() is True or self.rbSeats2.isChecked() is True or self.rbSeats3.isChecked() is True) and (self.rbTicket0.isChecked() is True or self.rbTicket1.isChecked() is True or self.rbTicket2.isChecked() is True ) and (self.rbPort0.isChecked() is True or self.rbPort1.isChecked() is True or self.rbPort2.isChecked() is True) and (self.rbSafety0.isChecked() is True or self.rbSafety1.isChecked() is True or self.rbSafety2.isChecked() is True):
            print("Ora puoi chiudere la finestra!")
        else:
            print("Selezionare almeno una delle opzioni per ogni domanda")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog1 = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog_createFile()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())
