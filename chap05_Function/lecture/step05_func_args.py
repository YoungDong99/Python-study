"""
함수의 가변인수 
 - 한 개 가인수로 여러 개의 실인수를 받는 인수
"""

# 1. tuple형 가변인수 
def func1(name, *names) :
    print(name) # 홍길동
    print(names) # ('이순신', '유관순') : tuple 

# 함수 호출 
func1("홍길동", "이순신", "유관순")


# 2. dict형 가변인수 
def person(w, h, **other) :
    print('몸무게 :', w) # 몸무게 : 65
    print('키 : ', h) # 키 :  175
    print('기타 : ', other) # {'name': '홍길동', 'addr': '서울시'}

# 함수 호출
person(65, 175, name='홍길동', addr = '서울시')


# 3. 함수를 인수로 넘기기  
def square(x) : # x^2
    return x**2

square(10) # 100

def my_func(func, datas) : # (함수명, 데이터셋)

    calc = []
    for x in datas :
        #calc.append(square(x)) # 함수 -> 외부 함수 호출
        calc.append(func(x)) # 자체 함수 처리(처리 속도 향상) 
    return calc    

# 함수 호출 
my_func(square, [1,2,3,4,5]) # [1, 4, 9, 16, 25]



