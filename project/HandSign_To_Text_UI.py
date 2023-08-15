from PyQt5 import QtCore, QtGui, QtWidgets

from Sign_to_text import hand_sign_predict

class HandSign_To_Text(object):
    def calc(self):
        img_path = self.textEdit.toPlainText()
        message = hand_sign_predict(img_path)
        self.textEdit_2.setText(message)

        
    def setupUi(self, HandSign_To_Text):
        HandSign_To_Text.setObjectName("HandSign_To_Text")
        HandSign_To_Text.resize(768, 615)
        HandSign_To_Text.setStyleSheet("Background-image:url('abc.jpg')")
        self.pushButton = QtWidgets.QPushButton(HandSign_To_Text)
        self.pushButton.setGeometry(QtCore.QRect(270, 450, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("Background-Color:rgba(61, 182, 226,1)")
        self.pushButton.setObjectName("pushButton")
        
        # connect the button to the function
        self.pushButton.clicked.connect(self.calc)
        
        self.textEdit = QtWidgets.QTextEdit(HandSign_To_Text)
        self.textEdit.setGeometry(QtCore.QRect(230, 180, 461, 91))
        self.textEdit.setStyleSheet("background:rgb(224, 226, 226)")
        
        self.textEdit.setObjectName("textEdit")
        
        self.label_3 = QtWidgets.QLabel(HandSign_To_Text)
        self.label_3.setGeometry(QtCore.QRect(140, 0, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(HandSign_To_Text)
        self.label.setGeometry(QtCore.QRect(70, 190, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(14)

        self.label_2 = QtWidgets.QLabel(HandSign_To_Text)
        self.label_2.setGeometry(QtCore.QRect(70, 310, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(HandSign_To_Text)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 300, 461, 91))
        self.textEdit_2.setStyleSheet("background:rgb(224, 226, 226)")
        
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.label_4 = QtWidgets.QLabel(HandSign_To_Text)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/E:/YOUR_PROJECT_DIRECTORY/im1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(HandSign_To_Text)
        QtCore.QMetaObject.connectSlotsByName(HandSign_To_Text)
        
        

    def retranslateUi(self, HandSign_To_Text):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("HandSign_To_Text", "Convert"))
        HandSign_To_Text.setWindowTitle(_translate("HandSign_To_Text", "Form"))
        self.label_3.setText(_translate("HandSign_To_Text", "Sign To Text"))
        self.label.setText(_translate("HandSign_To_Text", "Image Path"))
        self.textEdit.setHtml(_translate("HandSign_To_Text", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("HandSign_To_Text", "Text Output"))
        self.textEdit_2.setHtml(_translate("HandSign_To_Text", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HandSign_To_Text = QtWidgets.QWidget()
    ui = HandSign_To_Text()
    ui.setupUi(HandSign_To_Text)
    HandSign_To_Text.show()
    sys.exit(app.exec_())

