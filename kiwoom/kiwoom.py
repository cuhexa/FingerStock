from PyQt5.QAxContainer import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        print("Kiwoom 클래스 입니다")

        self.get_ocx_insatance()
        self.event_slots()

        self.signal_login_commConnect()


    def get_ocx_insatance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slots)

    def login_slots(self, errCode):
        print(errCode)

    def signal_login_commConnect(self):
        self.dynamicCall('CommConnect()')