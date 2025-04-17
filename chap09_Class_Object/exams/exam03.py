'''
문3) 아래와 같은 중첩함수(ATM)를 클래스(ATM)로 변환하시오.
'''

def ATM_df(bal) : # 현금자동 입출금기 
    accBal = bal # 잔액
    
    # 잔액 조회 : 획득자(getter)
    def getBal() :
        return accBal
    
    # 입금하기 : 지정자(setter)
    def setDeposit(money) :
        nonlocal accBal
        accBal += money
        
    # 출금하기 : 지정자(setter)  
    def setWithdraw(money) :
        nonlocal accBal
        accBal -= money
        
    return getBal, setDeposit, setWithdraw


# 클래스 정의 
class ATM :
    
    def __init__(self, bal):
        self.__accBal = bal
    
    def getBal(self) :
        return self.__accBal
    
    def setDeposit(self, money) :
        self.__accBal += money
        print(f'{money:,}원이 입금되었습니다.')
        print(f'현재 잔액 : {self.__accBal:,}원')
        
    def setWithdraw(self, money) :
        if self.__accBal < money :
            print('잔액이 부족합니다.')
        else :
            self.__accBal -= money
            print(f'{money:,}원이 출금되었습니다.')
            print(f'현재 잔액 : {self.__accBal:,}원')
        


bank = ATM(50000)

bank.setDeposit(10000)

bank.setWithdraw(30000)










