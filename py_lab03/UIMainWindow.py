# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(350, 60, 88, 28))
        self.calculateButton.setObjectName("calculateButton")
        self.inputIntervalLeft = QtWidgets.QLineEdit(self.centralwidget)
        self.inputIntervalLeft.setGeometry(QtCore.QRect(180, 20, 161, 28))
        self.inputIntervalLeft.setInputMask("")
        self.inputIntervalLeft.setObjectName("inputIntervalLeft")
        self.inputIntervalRight = QtWidgets.QLineEdit(self.centralwidget)
        self.inputIntervalRight.setGeometry(QtCore.QRect(180, 50, 161, 28))
        self.inputIntervalRight.setInputMask("")
        self.inputIntervalRight.setText("")
        self.inputIntervalRight.setObjectName("inputIntervalRight")
        self.inputStep = QtWidgets.QLineEdit(self.centralwidget)
        self.inputStep.setGeometry(QtCore.QRect(180, 80, 161, 28))
        self.inputStep.setInputMask("")
        self.inputStep.setText("")
        self.inputStep.setMaxLength(32767)
        self.inputStep.setFrame(True)
        self.inputStep.setObjectName("inputStep")
        self.inputAccuracity = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAccuracity.setGeometry(QtCore.QRect(180, 110, 161, 28))
        self.inputAccuracity.setInputMask("")
        self.inputAccuracity.setText("")
        self.inputAccuracity.setMaxLength(32767)
        self.inputAccuracity.setFrame(True)
        self.inputAccuracity.setObjectName("inputAccuracity")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 161, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 161, 20))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 151, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.outputTable = QtWidgets.QTableWidget(self.centralwidget)
        self.outputTable.setGeometry(QtCore.QRect(10, 140, 771, 411))
        self.outputTable.setMinimumSize(QtCore.QSize(771, 411))
        self.outputTable.setMaximumSize(QtCore.QSize(771, 16777215))
        self.outputTable.setRowCount(0)
        self.outputTable.setColumnCount(6)
        self.outputTable.setObjectName("outputTable")
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(5, item)
        self.outputTable.horizontalHeader().setVisible(True)
        self.outputTable.horizontalHeader().setCascadingSectionResizes(False)
        self.outputTable.horizontalHeader().setDefaultSectionSize(125)
        self.outputTable.horizontalHeader().setHighlightSections(True)
        self.outputTable.horizontalHeader().setSortIndicatorShown(False)
        self.outputTable.horizontalHeader().setStretchLastSection(True)
        self.outputTable.verticalHeader().setVisible(False)
        self.buildGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.buildGraphButton.setGeometry(QtCore.QRect(637, 60, 131, 28))
        self.buildGraphButton.setObjectName("buildGraphButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(450, 10, 171, 121))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculateButton.setText(_translate("MainWindow", "Рассчитать"))
        self.label.setText(_translate("MainWindow", "Левая граница отрезка"))
        self.label_2.setText(_translate("MainWindow", "Правая граница отрезка"))
        self.label_3.setText(_translate("MainWindow", "Шаг"))
        self.label_4.setText(_translate("MainWindow", "Точность"))
        item = self.outputTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер корня"))
        item = self.outputTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Интервал"))
        item = self.outputTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Корень"))
        item = self.outputTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Функция в корне"))
        item = self.outputTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Итерации"))
        item = self.outputTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Код ошибки"))
        self.buildGraphButton.setText(_translate("MainWindow", "Построить график"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Тексты ошибок:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 - успешное завершение</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 - корень не найден</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 - превышено максимальное число итераций</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 - деление на ноль</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
