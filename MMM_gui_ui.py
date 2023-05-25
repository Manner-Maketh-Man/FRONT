from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
import json
import sys
import time
from Request import serverRequest
import Functions.AutoScreenShot as AutoScreenShot
import Functions.Sticker as STICKER

class Ui_Dialog(object):
    
    def __init__(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.exeBtnClick)
        self.sticker_instance = None
        # self.forDebug = 0
        
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
        ############## 버튼 설정 start ##############################################################################
        ###########################################################################################################
        self.executeButton.clicked.connect(self.start)   # 'executeButton'이 클릭되면 'btnClick'이 실행되게 설정합니다.
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
        
        self.stopButton.clicked.connect(self.stop)   # 'stopButton'이 클릭되면 'btnClick'이 실행되게 설정합니다.
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
        
        ############# 버튼설정 end ##################################################################################
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
        
    ###########################################################################################################
    ###########################################################################################################
    ############# 버튼클릭 함수 선언 ###############################################################################
    
    def start(self):
        print("Starting")
        interval = 10    # OCR 수행 간격 (현재 5초)
        self.timer.start(interval*1000)
        
        ## for Debug
        # self.forDebug = 0

    def stop(self):
        print("Stopping")
        self.timer.stop()
        self.sticker_instance.remove_sticker()
    
    # 반복 동작할 함수 선언
    def exeBtnClick(self):
        print("exe버튼이 클릭되었습니다.")
        print("ScreenShot 실행")
        AutoScreenShot.capture_screenshot()
        print("ScreenShot 완료")
        print("Request 전송")
        response = serverRequest.send_request()  ## returns json
        ## for Debug
        # response = {'response_data':0+self.forDebug}
        # self.forDebug=self.forDebug+1
        # print("Response: ", response['response_data'])
        
    # gif.별 파일 경로 설정
        sticker_map = {
            # 0: sadness,
            # 1: fear,
            # 2: disgust,
            # 3: neutral,
            # 4: happiness,
            # 5: angry,
            # 6: surprise
            0: 'gif/project/sadness.gif',
            1: 'gif/project/fear.gif',
            2: 'gif/project/disgust.gif',
            3: 'gif/project/neutral.gif',
            4: 'gif/project/happiness.gif',
            5: 'gif/project/angry.gif',
            6: 'gif/project/surprise.gif',
        }
        sticker_path = sticker_map[response['response_data']]
        
    # gif.별 출력 위치 설정
        sticker_xy_map = {
            # 0: 'gif/project/sadness.gif',
            # 1: 'gif/project/fear.gif',
            # 2: 'gif/project/disgust.gif',
            # 3: 'gif/project/neutral.gif',
            # 4: 'gif/project/happiness.gif',
            # 5: 'gif/project/angry.gif',
            # 6: 'gif/project/surprise.gif',
            0: [600, 500],
            1: [600, 500],
            2: [600, 500],
            3: [630, 530],
            4: [600, 500],
            5: [600, 400],
            6: [600, 500],
        }
        sticker_xy_val = sticker_xy_map[response['response_data']]
        
    # gif.별 출력 위치 설정
        sticker_size_map = {
            # 0: 'gif/project/sadness.gif',
            # 1: 'gif/project/fear.gif',
            # 2: 'gif/project/disgust.gif',
            # 3: 'gif/project/neutral.gif',
            # 4: 'gif/project/happiness.gif',
            # 5: 'gif/project/angry.gif',
            # 6: 'gif/project/surprise.gif',
            0: 0.65,
            1: 0.75,
            2: 0.75,
            3: 0.5,
            4: 0.75,
            5: 1.5,
            6: 0.65,
        }
        sticker_size_val = sticker_size_map[response['response_data']]

# TODO: 사이즈 별 mapping 및 스티커별 동작 커스터마이징
    # Sticker 출력
        sticker = STICKER.Sticker(img_path = sticker_path, xy=sticker_xy_val, size=sticker_size_val, on_top=True)
        self.sticker_instance = sticker

    ############# 버튼클릭 함수 선언 end ###########################################################################
    ###########################################################################################################
    ###########################################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # QDialog 객체를 생성하고 Ui_Dialog 클래스를 사용하여 UI를 설정합니다.
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    # QDialog를 표시하고 애플리케이션을 실행합니다.
    Dialog.show()
    sys.exit(app.exec_())
