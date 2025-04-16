'''
클래스(class)?
 - 여러 개의 함수와 자료를 묶어서 객체 생성 역할
 - 구성요소 : 멤버변수(자료) + 멤버메서드(처리)

 형식)
class 클래스 :
     멤버변수=값
     def 생성자(self) :
          멤버변수 초기화  
     def 멤버메서드(self) :
          명령문       
'''

# 중첩함수 vs 클래스 

# 1. 중첩 함수
def calc_func(a, b): # 외부함수 : 자료 저장 
    x = a 
    y = b 
    
    # 내부함수 : 자료 처리 
    def plus():
        p = x + y
        return p
    
    def minus():
        m = x - y
        return m
    
    return plus, minus 
    

# 외부함수 호출 
plus, minus = calc_func(10, 20) # 내부함수 반환 
print(plus())
print(minus())



# 2. 클래스 
class calc_class :
    # 멤버변수 : 자료 저장
    x = 0
    y = 0
    
    # 생성자 : 객체 생성 & 멤버변수 초기화
    def __init__(self, x, y):
        # self.멤버변수 = 매개변수 / self > 매개체 역할
        self.x = x
        self.y = y
        
        # 생성자 내에서 변수 선언과 동시에 초기화 가능
    
    # 멤버메서드 : 자료처리
    def plus(self): 
        p = self.x + self.y
        return p 
    
    def minus(self):
        m = self.x - self.y
        return m
    

# 클래스(설계도) -> 객체(결과물)
calc1 = calc_class(10, 20) # 클래스(x, y) : 객체 생성 & 멤버변수 초기화 
'''
생성자 호출 : 클래스명(실인수)
'''

# 객체.변수, 객체.메서드()
calc1.x  # 10
calc1.y  # 20

# 값 변경
calc1.x = 1
calc1.y = 2

print('plus =', calc1.plus())
print('minus =', calc1.minus())

# 두번째 객체
calc2 = calc_class(5, 6)  # 생성자 -> 객체 생성

# 객체 구성요소 확인
dir(calc2)
'''
 'minus' : 메서드(처리)
 'plus' : 메서드(처리)
 'x' : 변수(자료)
 'y' : 변수(자료)
'''

calc2.x = 1000
calc2.y = 500

print('plus =', calc2.plus())
print('minus =', calc2.minus())



















