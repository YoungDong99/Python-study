"""
계수기(Counter) 클래스 만들기
    실세계 객체 : 상태(현재값) + 동작(초기화, 값증가, 값확인)
    클래스(설계) : 구성요소 : 멤버변수 1개, 멤버메서드 3개   
    컴퓨터 객체(구현) : 클래스 생성자
"""

# 1. 클래스 설계
class Counter:
    count = None # 멤버변수
    
    # 생성자 : 객체 생성
    def __init__(self) :
        self.count = 0 # 멤버변수 초기화
        
    def reset(self) :
        self.count = 0
        
    def increment(self):
        self.count += 1
        
    def get(self):
        return self.count

# 2. 객체 : 생성자 생성
counter1 = Counter() # 생성자

dir(counter1)
'''
 'count'     : 변수(현재값)
 'get'       : 값 확인       -> 직접만든 메서드
 'increment' : 값 증가
 'reset'     : 값 초기화
'''
counter1.count  # 0

# 값 증가
counter1.increment()
counter1.get()
counter1.increment() # 반복할때마다 증가
counter1.get()

# 값 초기화
counter1.reset()
counter1.get()   # 0

# 객체의 출처(클래스) 확인
print(type(counter1))  # <class '__main__.Counter'>

list = [1, 2, 3, 4, 5]
print(type(list))

dir(list)


# 두 번째 계수기
counter2 = Counter()  # 생성자

dir(counter2)
'''
 'count'
 'get'
 'increment'
 'reset'
'''

# 객체의 주소
print(id(counter1))  # 2143779829808

print(id(counter2))  # 2143779824048











