'''
사람(Person) 클래스를 상속받아서 2명의 사람 만들기 
'''

# 부모 클래스(사람) 
class Person :    
    
    # 생성자 : 동적멤버변수   
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
        
    # 멤버메서드 
    def info(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}')
        
     
# 자식1 클래스(홍길동)
class Hong(Person): # 클래스 상속  
    # 자식 생성자      
    def __init__(self, name, age, gender, job) :
        super().__init__(name, age, gender) # 부모 생성자 호출(부모 멤버 초기화) 
        ''' 상속의미 없음 
        self.name = name # 부모멤버 
        self.age = age # 부모멤버 
        self.gender = gender # 부모멤버 
        '''
        self.job = job  # 자식멤버 1개
        
    def info(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}, 직업 : {self.job}')


hong = Hong("홍길동", 35, "남자", "회사원")  # 자식 생성자 
dir(hong)

hong.info()  # 이름 : 홍길동, 나이 : 35, 성별 : 남자, 직업 : 회사원


# 자식2 클래스(유관순)   
class Yoo(Person): # 클래스 상속       
    # 생성자 & job="공무원" 멤버 추가 & 메서드 재정의
    # 자식 생성자         
    def __init__(self, name, age, gender, job) :
        super().__init__(name, age, gender) # 부모 멤버 초기화        
        self.job = job  # 자식멤버 1개
        
    def info(self): # 메서드 재정의 
       print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}, 직업 : {self.job}')
    
    
    
yoo = Yoo("유관순", 25, "여자", "공무원")    

yoo.info() # 이름 : 유관순, 나이 : 25, 성별 : 여자, 직업 : 공무원  


























