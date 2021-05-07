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
        self. detail_account_info() # 예수금 가져오는 것!


    def get_ocx_insatance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")


    def event_slots(self):
        self.OnEventConnect.connect(self.login_slots)
        self.OnReceiveTrData.connect(self.trdata_slot)


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
        # account_id = self.dynamicCall("GetLoginInfo(String)", "USER_ID")

        self.account_num = account_list.split(';')[0]
        print("내 계좌번호 %s" % self.account_num)  #8166270411


    def detail_account_info(self):
        print("예수금을 요청하는 부분")

        self.dynamicCall("SetInputValue(string, sting)", "계좌번호", self.account_num)
        self.dynamicCall("SetInputValue(string, sting)", "비밀번호", "0000")
        self.dynamicCall("SetInputValue(string, sting)", "비밀번호입력매체구분", "00")
        self.dynamicCall("SetInputValue(string, sting)", "조회구분", "2")
        self.dynamicCall("CommRqData(String, String, int, String)", "예수금상세현황요청", "opw00001", "0", "2000")


    def trdata_slot(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):
        '''
        tr요청을 받는 구간, 슬롯
        sScrNo: 스크린번호
        sRQName: 내가 요청했을 때 지은 이름
        sTrCode: 요청id , tr코드
        sRecordName: 사용안함
        sPrevNext: 다음페이지가 있는지
        '''

        if sRQName == "예수금상세현황요청":
            deposit = self.dynamicCall("GetCommData(String, String, int, String)", sTrCode, sRQName, 0, "예수금")
            # print("예수금 %s" % deposit)
            print("예수금 %s" % int(deposit))

            ok_deposit = self.dynamicCall("GetCommData(String, String, int, String)", sTrCode, sRQName, 0, "출금가능금액")
            # print("출금가능금액 %s" % ok_deposit)
            print("출금가능금액 %s" % int(ok_deposit))