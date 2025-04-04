"""
1. 함수(function) : 어떤 기능을 정의해 놓은 것 


2. 사용자정의함수  
 형식)
 def 함수명(인수) :
     실행문
     실행문
     return 값(상수 or 변수 or 수식)
"""

# 1. 인수가 없는 함수 
def userFunc1() :
    print('userFunc1')
    print('인수가 없는 함수')


# 함수 호출 
userFunc1() # 함수명()

# 2. 인수가 있는 함수 
def userFunc2(x, y) :
    z = x + y
    print('z=', z)


# 함수 호출 
userFunc2(10, 20) # z= 30
userFunc2('홍길동', '강감찬') # z= 홍길동강감찬
#userFunc2(10, '홍길동') # 오류 


# 3. return 있는 함수 
def userFunc3(x, y) : # (가인수=매개변수)
    add = x + y
    sub = x - y     
    mul = x * y
    div = x / y
    return add, sub, mul, div # 여러개 값 반환 

# 함수 호출 
print(userFunc3(10, 20)) # (30, -10, 200, 0.5)

a, s, m, d = userFunc3(10, 20) # (실인수)
print(a, s, m, d) # 30 -10 200 0.5

result = userFunc3(y=20, x=10) # 이름으로 전달 : ppt.15
print(result) # (30, -10, 200, 0.5)


# 4. 수학 방정식 예
def fx(x) : 
    y = 2*x + 3 # 1차 방정식 : 직선(선형)    
    return y


# 함수 호출 
print(fx(2)) # 7
print(fx(4)) # 11
print(fx(6)) # 15


# 함수 호출 
x = range(1,11) # x변수 : 1~10 
y = [fx(i)  for  i  in  x] # list 내포 
print(y) # [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

# 차트 시각화 
import matplotlib.pyplot as plt # 별칭 

plt.plot(x, y) # 직선(선형)
plt.title('line')
plt.show()



