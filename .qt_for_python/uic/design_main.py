# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sohyeon/다운로드/lpoint/design_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 671)
        self.pushButton_cust_id = QtWidgets.QPushButton(Dialog)
        self.pushButton_cust_id.setGeometry(QtCore.QRect(530, 10, 101, 71))
        self.pushButton_cust_id.setObjectName("pushButton_cust_id")
        self.lineEdit_cust_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_cust_id.setGeometry(QtCore.QRect(10, 10, 511, 71))
        self.lineEdit_cust_id.setObjectName("lineEdit_cust_id")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 621, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_gender = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_gender.setText("")
        self.label_gender.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_gender.setObjectName("label_gender")
        self.horizontalLayout.addWidget(self.label_gender)
        self.label_age = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_age.setText("")
        self.label_age.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_age.setObjectName("label_age")
        self.horizontalLayout.addWidget(self.label_age)
        self.label_zon = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_zon.setText("")
        self.label_zon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_zon.setObjectName("label_zon")
        self.horizontalLayout.addWidget(self.label_zon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 621, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.pushButton_recom = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_recom.setObjectName("pushButton_recom")
        self.verticalLayout.addWidget(self.pushButton_recom)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 131, 20))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 200, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.radioButton_count = QtWidgets.QRadioButton(Dialog)
        self.radioButton_count.setGeometry(QtCore.QRect(100, 220, 95, 21))
        self.radioButton_count.setObjectName("radioButton_count")
        self.radioButton_price = QtWidgets.QRadioButton(Dialog)
        self.radioButton_price.setGeometry(QtCore.QRect(210, 220, 95, 21))
        self.radioButton_price.setObjectName("radioButton_price")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_cust_id.setText(_translate("Dialog", "Enter"))
        self.lineEdit_cust_id.setText(_translate("Dialog", "회원번호를 입력해주세요"))
        self.pushButton_recom.setText(_translate("Dialog", "오늘의추천"))
        self.label.setText(_translate("Dialog", "고객정보"))
        self.label_2.setText(_translate("Dialog", "구매이력조회"))
        self.radioButton_count.setText(_translate("Dialog", "횟수"))
        self.radioButton_price.setText(_translate("Dialog", "금액"))
