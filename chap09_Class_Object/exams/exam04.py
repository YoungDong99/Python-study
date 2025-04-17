'''
문4) 사원(Employee) 클래스에서 정의한 멤버(name, pay, info)를 정규직(Permanent) 클래스와
    임시직(Temporary) 클래스에 각각 상속하여 사원의 이름은 name에 저장하고, 지급액은 
    아래 <조건>에 맞게 정규직과 임시직의 급여 계산 방식으로 계산하여 pay에 저장한다.
    끝으로 info() 메서드를 이용하여 이름(name)과 지급액(pay)을 출력하시오.
     
     <조건1> 정규직(Permanent) 급여(pay) = 기본급 + 상여금 
     <조건2> 임시직(Temporary) 급여(pay) = 작업시간 * 시급 
          
    기타 사항은 <출력결과 예시>를 참고하세요.
     
     
     <정규직 실인수 & 출력결과 예시>
     이름(name) : 홍길동     
     기본급(sal) : 2000000  
     상여금(bonus) : 500000     
     
     name = 홍길동, pay = 2,500,000 

     <임시직 실인수 & 출력결과 예시>
     이름(name) : 강호동    
     작업시간(wtime) : 200    
     시급(tpay) : 9000      
     
     name = 강호동, pay = 1,800,000     
'''

# 사원 클래스(부모)  
class Employee : 
    name = None # 사원이름 
    pay = 0 # 지급액 
    
    def __init__(self, name, pay) :
        self.name = name
        self.pay = pay
    
    # 이름과 지급액 출력 
    def info(self) :
        print('이름 : {0}, 지급액 : {1:3,d}'.format(self.name,self.pay))
    
# 정규직 클래스(자식)  
class Permanent(Employee) :
    
    def __init__(self, name, sal, bonus) :
        super().__init__(name, sal + bonus)
        self.sal = sal
        self.bonus = bonus
   
    def info(self) :
        print(f'이름(name) : {self.name}')
        print(f'기본급(sal) : {self.sal:,}')
        print(f'상여금(bonus) : {self.bonus:,}')
        print(f'\nname = {self.name}, pay = {self.pay}')

# 임시직 클래스(자식)  
class Temporary(Employee) :
    
    def __init__(self, name, wtime, tpay) :
        # 부모클래스 생성자 없을 시
        self.name = name
        self.pay = wtime * tpay
        
        self.wtime = wtime
        self.tpay = tpay
        
    def info(self) :
        print(f'이름(name) : {self.name}')
        print(f'작업시간(wtime) : {self.wtime}')
        print(f'시급(tpay) : {self.tpay:,}')
        print(f'\nname = {self.name}, pay = {self.pay}')
    

hong = Permanent("홍길동", 2000000, 500000)
hong.info()

print('=================================')

kang = Temporary("강호동", 200, 9000)
kang.info()

