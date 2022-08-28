import os.path

from PyQt5 import QtCore, QtGui, QtWidgets
import learning as sl
from class2_GUI import Ui_Dialog_createFile
from os import path
from PathGUI import ROOT_DIR


class Learning():
    _X = None
    _y = None
    _enc = None
    _le = None

    def initDataset(path):
        dataset = sl.recoverDataset(path)
        Learning._X, Learning._enc = sl.splitX(dataset)
        Learning._y, Learning._le = sl.splity(dataset)

    def getKFoldScores(metric):
        if Learning._X is not None and Learning._y is not None:
            scores = sl.getKFoldScores(Learning._X, Learning._y, metric)
            return scores
        else:
            return "Dataset wasn't loaded correctly"

    def getPredForClassifier(option, testsize, i):
        path = ROOT_DIR+"\\app\\classification.txt"
        if option == 1:
            return sl.logisticRegressionPred(Learning._X, Learning._y, testsize, Learning._le, Learning._enc, i, path)
        elif option == 2:
            return sl.supportVectorMachinesPred(Learning._X, Learning._y, testsize, Learning._le, Learning._enc, i,
                                                path)
        elif option == 3:
            return sl.randomForestClassifierPred(Learning._X, Learning._y, testsize, Learning._le, Learning._enc, i,
                                                 path)
        elif option == 4:
            return sl.decisionTreeClassifierPred(Learning._X, Learning._y, testsize, Learning._le, Learning._enc, i,
                                                 path)
        else:
            return "Option wasn't selected correctly"

class Ui_Dialog_Class(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(1220, 709)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)


        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(350, 50, 591, 401))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.pushButtonClassify = QtWidgets.QPushButton(Dialog)
        self.pushButtonClassify.setGeometry(QtCore.QRect(140, 590, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.pushButtonClassify.setFont(font)
        self.pushButtonClassify.setObjectName("pushButtonClassify")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cboxAlg = QtWidgets.QComboBox(Dialog)
        self.cboxAlg.setGeometry(QtCore.QRect(40, 530, 191, 20))
        self.cboxAlg.setObjectName("cboxAlg")
        self.cboxAlg.addItem("")
        self.cboxAlg.addItem("")
        self.cboxAlg.addItem("")
        self.cboxAlg.addItem("")


        self.cboxType = QtWidgets.QComboBox(Dialog)
        self.cboxType.setGeometry(QtCore.QRect(240, 530, 191, 20))
        self.cboxType.setObjectName("cboxType")
        self.cboxType.addItem("")
        self.cboxType.addItem("")


        self.pushButtonCalculate = QtWidgets.QPushButton(Dialog)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(950, 590, 93, 71))
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.pushButtonCreateFile = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateFile.setGeometry(QtCore.QRect(540, 520, 93, 51))
        self.pushButtonCreateFile.setObjectName("pushButtonCreate")
        self.pushButtonDeleteFile = QtWidgets.QPushButton(Dialog)
        self.pushButtonDeleteFile.setGeometry(QtCore.QRect(540, 580, 93, 51))
        self.pushButtonDeleteFile.setObjectName("pushButtonDelete")
        self.cboxMetric = QtWidgets.QComboBox(Dialog)
        self.cboxMetric.setGeometry(QtCore.QRect(900, 510, 181, 41))
        self.cboxMetric.setObjectName("cboxMetric")
        self.cboxMetric.addItem("")
        self.cboxMetric.addItem("")
        self.cboxMetric.addItem("")
        self.cboxMetric.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButtonClassify.clicked.connect(self.buttonPred)
        self.pushButtonCalculate.clicked.connect(self.buttonKF)
        self.pushButtonCreateFile.clicked.connect(self.openclass2)
        self.pushButtonDeleteFile.clicked.connect(self.deleteFile)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Classificazione"))
        self.pushButtonClassify.setText(_translate("Dialog", "CLASSIFY"))
        self.cboxAlg.setItemText(0,_translate("Dialog","Logistic Regression"))
        self.cboxAlg.setItemText(1,_translate("Dialog","Support Vector Machines"))
        self.cboxAlg.setItemText(2,_translate("Dialog","Random Forest Classifier"))
        self.cboxAlg.setItemText(3,_translate("Dialog","Decision Tree Classifier"))


        self.cboxType.setItemText(0, _translate("Dialog", "Classification Report"))
        self.cboxType.setItemText(1, _translate("Dialog", "Classification from File"))
        self.pushButtonCalculate.setText(_translate("Dialog", "CALCULATE"))
        self.pushButtonCreateFile.setText(_translate("Dialog", "CREATE FILE"))
        self.pushButtonDeleteFile.setText(_translate("Dialog", "DELETE FILE"))
        self.cboxMetric.setItemText(0, _translate("Dialog", "Balanced accuracy"))
        self.cboxMetric.setItemText(3, _translate("Dialog", "Negative Mean Squared Error"))
        self.cboxMetric.setItemText(2, _translate("Dialog", "F1"))
        self.cboxMetric.setItemText(1, _translate("Dialog", "Accuracy"))


    def __init__(self):
        filename = ROOT_DIR + "\\utilities\\dataset.csv"
        Learning.initDataset(filename)

    def buttonPred(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        if self.cboxAlg.currentText() == "Logistic Regression" and self.cboxType.currentText() == "Classification Report":
            self.plainTextEdit.clear()
            action = 0
            option = 1
            self.plainTextEdit.insertPlainText("Logistic Regression Table:"+"\n")
        elif self.cboxAlg.currentText() == "Support Vector Machines" and self.cboxType.currentText() == "Classification Report":
            self.plainTextEdit.clear()
            action = 0
            option = 2
            self.plainTextEdit.insertPlainText("Support Vector Machines Table:"+"\n")
        elif self.cboxAlg.currentText() == "Random Forest Classifier" and self.cboxType.currentText() == "Classification Report":
            self.plainTextEdit.clear()
            action = 0
            option = 3
            self.plainTextEdit.insertPlainText("Random Forest Classifier Table:"+"\n")
        elif self.cboxAlg.currentText() == "Decision Tree Classifier" and self.cboxType.currentText() == "Classification Report":
            self.plainTextEdit.clear()
            action = 0
            option = 4
            self.plainTextEdit.insertPlainText("Decision Tree Classifier Table:"+"\n")
        elif self.cboxAlg.currentText() == "Logistic Regression" and self.cboxType.currentText() == "Classification from File":
            self.plainTextEdit.clear()
            action = 1
            option = 1
            self.plainTextEdit.insertPlainText("Logistic Regression Prediction:"+"\n")
        elif self.cboxAlg.currentText() == "Support Vector Machines" and self.cboxType.currentText() == "Classification from File":
            self.plainTextEdit.clear()
            action = 1
            option = 2
            self.plainTextEdit.insertPlainText("Support Vector Machines Prediction:"+"\n")
        elif self.cboxAlg.currentText() == "Random Forest Classifier" and self.cboxType.currentText() == "Classification from File":
            self.plainTextEdit.clear()
            action = 1
            option = 3
            self.plainTextEdit.insertPlainText("Random Forest Classifier Prediction:"+"\n")
        elif self.cboxAlg.currentText() == "Decision Tree Classifier" and self.cboxType.currentText() == "Classification from File":
            self.plainTextEdit.clear()
            action = 1
            option = 4
            self.plainTextEdit.insertPlainText("Decision Tree Classifier Prediction:"+"\n")
        if action == 1:
            path1 = ROOT_DIR + "\\app\\classification.txt"
            if path.exists(path1) is True:
                resultList = Learning.getPredForClassifier(option,0.2,action)
                for result in resultList:
                    self.plainTextEdit.insertPlainText("La classe predetta è: " + result + "\n")
            else:
                self.plainTextEdit.insertPlainText("File inesistente. Creare il file dal pulsante 'CREATE FILE'")


        elif action == 0:
            self.plainTextEdit.insertPlainText(Learning.getPredForClassifier(option,0.2,action))

    def buttonKF(self):
        if self.cboxMetric.currentText() == "Balanced accuracy":
            metric = "balanced_accuracy"
            self.plainTextEdit.setPlainText("E' possibile vedere i risultati direttamente dal terminale")
        elif self.cboxMetric.currentText() == "Negative Mean Squared Error":
            metric = "neg_mean_squared_error"
            self.plainTextEdit.setPlainText("E' possibile vedere i risultati direttamente dal terminale")
        elif self.cboxMetric.currentText() == "F1":
            metric = "f1_macro"
            self.plainTextEdit.setPlainText("E' possibile vedere i risultati direttamente dal terminale")
        elif self.cboxMetric.currentText() == "Accuracy":
            metric = "accuracy"
            self.plainTextEdit.setPlainText("E' possibile vedere i risultati direttamente dal terminale")
        scores = Learning.getKFoldScores(metric)
        print(metric.upper())
        for classifier in scores.keys():
            print(classifier + ":" )
            print(scores[classifier])
        print("---------------------------------------------------")
            #self.plainTextEdit.insertPlainText(classifier + ":")
            #self.plainTextEdit.insertPlainText(scores[classifier])
            #self.plainTextEdit.insertPlainText("\n")
        #self.plainTextEdit.insertPlainText("---------------------------------------------------\n")

    def openclass2(self):
        self.window = QtWidgets.QMainWindow(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
        self.ui = Ui_Dialog_createFile()
        self.ui.setupUi(self.window)
        self.window.show()

    def deleteFile(self):
        path1 = ROOT_DIR + "\\app\\classification.txt"
        if path.exists(path1) is True:
            os.remove(path1)
        else:
            self.plainTextEdit.insertPlainText("Non esiste nessun file. Crearne uno nuovo dal pulsante 'CREATE FILE'")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog_Class()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

