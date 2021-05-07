from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        print("Kiwoom 클래스 입니다")

        ##### eventloop 모음
        self.login_event_loop = None
        ###############################################

        ##### 변수 모음
        self.account_num = None
        ###############################################

        self.get_ocx_insatance()
        self.event_slots()

        self.signal_login_commConnect()
        self.get_account_info()


    def get_ocx_insatance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slots)

    def signal_login_commConnect(self):
        self.dynamicCall('CommConnect()')

        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def login_slots(self, errCode):
        print(errCode)
        print(errors(errCode))

        self.login_event_loop.exit()

    def get_account_info(self):
        account_list = self.dynamicCall("GetLoginInfo(String)", "ACCNO")
        # account_list = self.dynamicCall("GetLoginInfo(String)", "USER_ID")

        self.account_num = account_list.split(';')[0]
        print("내 계좌번호 %s" % self.account_num)  #8166270411
