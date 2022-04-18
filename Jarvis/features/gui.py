# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gui(object):
    def setupUi(self, gui):
        gui.setObjectName("gui")
        gui.resize(1339, 736)
        self.centralwidget = QtWidgets.QWidget(gui)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_1.setGeometry(QtCore.QRect(-120, 0, 1501, 761))
        self.bg_1.setText("")
        self.bg_1.setPixmap(QtGui.QPixmap("Jarvis/utils/images/Black_Template.jpg"))
        self.bg_1.setScaledContents(True)
        self.bg_1.setObjectName("bg_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, -10, 961, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Jarvis/utils/images/live_wallpaper.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -50, 381, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Jarvis/utils/images/initiating.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 381, 311))
        self.label_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Jarvis/utils/images/Earth.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 600, 91, 41))
        self.pushButton.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: rgb(85, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 600, 101, 41))
        self.pushButton_2.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: rgb(85, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 520, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border-color: rgb(85, 170, 255);\n"
"color: rgb(0, 170, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 450, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("border-color: rgb(85, 170, 255);\n"
"color: rgb(0, 170, 255);\n"
"background-color:transperant;\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.bg_1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        gui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(gui)
        self.statusbar.setObjectName("statusbar")
        gui.setStatusBar(self.statusbar)

        self.retranslateUi(gui)
        QtCore.QMetaObject.connectSlotsByName(gui)

    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "MainWindow"))
        self.pushButton.setText(_translate("gui", "START"))
        self.pushButton_2.setText(_translate("gui", "EXIT"))
        self.textBrowser.setHtml(_translate("gui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("gui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = QtWidgets.QMainWindow()
    ui = Ui_gui()
    ui.setupUi(gui)
    gui.show()
    sys.exit(app.exec_())

