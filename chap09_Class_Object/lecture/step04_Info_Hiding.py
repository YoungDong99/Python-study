'''
정보은닉(Information Hiding)
  - 객체를 통해서 필드로 직접 접근을 차단하고, 획득자(getter)나 지정자(setter) 
    메서드를 통해서만 접근하도록 클래스를 설계하는 기법   
  
예) 은행 계좌 클래스 
   멤버변수 : 잔액(balance)
   멤버메서드 : 잔액확인(획득자), 입금하기(지정자), 출금하기(지정자) 
'''

class Account :
    
    # 생성자 
    def __init__(self, bal, name, no):
        # 동적 멤버 변수 
        self.__balance = bal # 잔액(은닉 멤버변수)
        self.name = name
        self.no = no 
        
    # 잔액확인 : 획득자(getter) - return문 
    def getBalance(self): 
        return self.__balance 
    
    # 입금하기 : 지정자(setter) - 매개변수 
    def deposit(self, money):
        self.__balance += money
    
    # 출금하기 : 지정자(setter) - 매개변수  
    def withdraw(self, money): 
        self.__balance -= money


# object 생성 
acc1 = Account(1000, '홍길동', '12345') # 객체 생성 & 잔액 초기화 

dir(acc1)
'''
 'balance'      : 안보임
 'deposit'      : 입금
 'getBalance'   : 잔액 확인
 'name'         :
 'no'           :
 'withdraw'     : 출금
'''


acc1.balance

# 잔액 확인 
acc1.getBalance() # 1000
# 입급 : 20000원 
acc1.deposit(20000)
# 출금 : 10000원
acc1.withdraw(10000)
# 잔액 확인 
acc1.getBalance() # 11000


# 두번째 계좌 생성
acc2 = Account(name="이순신", bal=0, no="45678")

dir(acc2)
'''
'deposit'
'getBalance'
'name'
'no'
'withdraw'
'''





















