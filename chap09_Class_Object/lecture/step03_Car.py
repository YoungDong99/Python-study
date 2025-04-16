'''
1. 동적 멤버변수 생성
  - 생성자 또는 메서드 호출 시 동적으로 만들어진 멤버 변수 
  
2. self : 자신(클래스)의 멤버를 호출 하는 객체 
   self.멤버변수 
   self.멤버메서드()
'''

class Car :
    # 정적 멤버변수 정의
    '''
    door = 0
    cc = 0
    name = None 
    '''
    
    # 생성자 : 객체 생성 & 동적 멤버변수 초기화
    def __init__(self, name, door, cc):
        # 동적 멤버변수 : self.변수
        self.name = name
        self.door = door
        self.cc = cc
        
    # 메서드 정의 : 자동차 정보 
    def display(self):             
        print("%s는 %d cc이고, 문짝은 %d개 이다."
              %(self.name, self.cc, self.door))
    
    def call(self):
        print('call 메서드')
        self.display()  # self.멤버메서드()

# 객체 생성 : 생성자
car1 = Car('소나타', 4, 2000)
car1.display()
car1.call()

car2 = Car('붕붕카', 2, 500)
car2.display()

'''
2. 기본 생성자(묵시적 생성자)
  - 생성자를 생략하면 기본 생성자가 만들어진다. 
'''

class default :     
    # 생성자 없음 : 기본 생성자 제공
    '''
    def __init__(self) :
        pass
    '''
    
    def data(self, x, y):
        # 동적 멤버변수
        self.x = x
        self.y = y
        
    def mul(self):
        return self.x * self.y



obj = default() # 기본 생성자

obj.data(10, 20) # 자료 생성
         
print(obj.mul()) # 200

