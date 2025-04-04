"""
축약함수(Lambda) : 한 줄 함수, 무명 함수  
 형식) 변수 = lambda 인수 : 명령문 
"""

# 1. 일반함수
def Adder(x, y) :
    add = x + y
    return add

Adder(10, 30) # 40


# 2. 축약함수(Lambda) 
Adder2 = lambda x, y : x + y  # Adder2 : 변수이름 > 함수의 이름 역할

print('add =', Adder2(10, 30)) # add = 40


# 함수 정의 & 호출 
(lambda x, y : x + y)(10, 30)


'''
python의 한 줄 문법
1. 한 줄 if문
2. list + for + if 한 줄 : list 내포
3. 한 줄 함수 : lambda
'''


# 예1) x 변량에 제곱 : 일반함수 vs 람다함수  
dataset = [1,2,3,4,5] 


# 일반함수 
def result(data) :
    calc = []
    for x in data :
        calc.append(x**2)
    
    #calc = [x**2 for x in data]  # comprehension
    return calc

print('result :', result(dataset))
# result : [1, 4, 9, 16, 25]


# 람다함수 : 변수 = lambda 인수 : 명령문
result2 = lambda data : [x**3 for x in data]

print('result2 :', result2(dataset))  # 변수(실인수)
# result : [1, 8, 27, 64, 125]



# 예2) 혈액형 가변수(dummy) 만들기 
map_data = {'AB':1, 'A':0, 'B':0, 'O':0} # dict : 매핑테이블

input_data = ['B', 'A', 'O', 'AB', 'B']  # list : 입력 data

# 일반함수
def dummy(data) :
    result = [ map_data[i] for i in data ]  #[실행문 for 변수 in 데이터]
    return result  # 가변수

print(dummy(input_data))  # [0, 0, 0, 1, 0]


# 람다함수

dummy2 = lambda data : ['O' if map_data[i] == 1 else 'X' for i in data]

print(dummy2(input_data))  # ['X', 'X', 'X', 'O', 'X']


# 람다함수 정의 & 호출
(lambda data : [map_data[i] for i in data])(input_data) # (람다함수)(실인수)








