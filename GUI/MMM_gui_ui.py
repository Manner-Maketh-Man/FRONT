from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 310)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 0, 441, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.largestLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.largestLayout.setContentsMargins(0, 0, 0, 0)
        self.largestLayout.setObjectName("largestLayout")
        self.instructionLayout = QtWidgets.QVBoxLayout()
        self.instructionLayout.setObjectName("instructionLayout")
        self.instruction1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.instruction1.setObjectName("instruction1")
        self.instructionLayout.addWidget(self.instruction1, 0, QtCore.Qt.AlignHCenter)
        self.instruction3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.instruction3.setObjectName("instruction3")
        self.instructionLayout.addWidget(self.instruction3)
        self.instruction2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.instruction2.setObjectName("instruction2")
        self.instructionLayout.addWidget(self.instruction2)
        self.largestLayout.addLayout(self.instructionLayout)
        self.executeLayout = QtWidgets.QVBoxLayout()
        self.executeLayout.setObjectName("executeLayout")
        self.executeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.executeLabel.setObjectName("executeLabel")
        self.executeLayout.addWidget(self.executeLabel, 0, QtCore.Qt.AlignVCenter)
        self.button = QtWidgets.QHBoxLayout()
        self.button.setObjectName("button")
        self.executeButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.executeButton.setObjectName("executeButton")
        self.button.addWidget(self.executeButton, 0, QtCore.Qt.AlignTop)
        self.stopButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stopButton.setObjectName("stopButton")
        self.button.addWidget(self.stopButton, 0, QtCore.Qt.AlignTop)
        self.executeLayout.addLayout(self.button)
        self.largestLayout.addLayout(self.executeLayout)
        
        ###########################################################################################################
        ############## 버튼 설정 ####################################################################################
        ###########################################################################################################
        
        self.executeButton.clicked.connect(self.btnClick)   # 'executeButton'이 클릭되면 'btnClick'이 실행되게 설정합니다.
        # executionButton 색상 설정
        self.executeButton.setStyleSheet("""
            QPushButton {
                color: black;
                background-color: white;
                border-radius: 5px;
            }
            QPushButton:pressed {
                color: black;
                background-color: grey;
                border-radius: 5px;
            }
        """)
        
        self.stopButton.clicked.connect(self.btnClick)   # 'stopButton'이 클릭되면 'btnClick'이 실행되게 설정합니다.
        # stopButton 색상 설정
        self.stopButton.setStyleSheet("""
            QPushButton {
                color: black;
                background-color: white;
                border-radius: 5px;
            }
            QPushButton:pressed {
                color: black;
                background-color: grey;
                border-radius: 5px;
            }
        """)
        
        ############# 버튼설정 완료 ##################################################################################
        ###########################################################################################################
        ###########################################################################################################
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.instruction1.setText(_translate("Dialog", "Manners Maketh Man"))
        self.instruction3.setText(_translate("Dialog", "1. 분석을 수행할 카카오톡 화면을 전체화면으로 변경한다."))
        self.instruction2.setText(_translate("Dialog", "2. 아래 감정분석 실행 버튼을 누른다."))
        self.executeLabel.setText(_translate("Dialog", "감정분석 실행"))
        self.executeButton.setText(_translate("Dialog", "실행"))
        self.stopButton.setText(_translate("Dialog", "멈춤"))
        
        
    def btnClick(self):
        print("버튼이 클릭되었습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # QDialog 객체를 생성하고 Ui_Dialog 클래스를 사용하여 UI를 설정합니다.
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    # QDialog를 표시하고 애플리케이션을 실행합니다.
    Dialog.show()
    sys.exit(app.exec_())
