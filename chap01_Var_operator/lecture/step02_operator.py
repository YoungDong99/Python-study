
'''
연산자(Operator)
 1. 할당연산자(=)
 2. 패킹(packing) 할당
 3. 연산자 : 산술, 비교, 논리
'''


# 1. 할당연산자(=)
i = tot = 10 # 변수 초기화 
print(i, tot) # 10 10

i += 1 # i = i + 1 
tot += i # tot = tot + i  
print(i, tot) # 11 21 

# 서로 다른값 할당 
v1, v2 = 100, 200
print(v1, v2)

# 변수 값 교체
v2, v1 = v1, v2
print(v1, v2)   # 200 100 (교체된 값)
'''
tmp = v1
v1 = v2
v2 = tmp
'''

# 2. 패킹(packing) 할당 (*)
lst = [1,2,3,4,5]  # 리스트 변수
print(lst) # [1, 2, 3, 4, 5]

v1, *v2 = lst
print(v1, v2) # 1 [2, 3, 4, 5]

*v1, v2 = lst
print(v1, v2) # [1, 2, 3, 4] 5


# 3. 연산자 : 산술,관계,논리 연산자 
num1 = 100 
num2 = 6

# 1) 산술연산자 
add = num1 + num2
print('add=', add) # add= 106

sub = num1 - num2
print('sub =', sub) # sub = 94

div = num1 / num2 
print('div =', div) # div = 16.666666

div = num1 // num2 
print('div =', div) # div = 16

div2 = num1 % num2
print('div2=', div2) # div2= 4

mul = num1 * num2
print('mul=', mul) # mul= 600

square = num1 ** 2
print('square=', square) # square= 10000


# 2) 관계 연산자 
# (1) 동등비교 
result = num1 == num2
print(result) # False

result = num1 != num2
print(result) # True

# (2) 크기비교 
result = num1 > num2
print(result) # True

result = num1 >= num2
print(result) # True

result = num1 < num2
print(result) # False

result = num1 <= num2
print(result) # False

# 3) 논리 연산자
result = num1 >= 50 and num2 <= 20 # 논리곱
print(result) # True

result = num1 < 50 or num2 <= 20 # 논리합
print(result) # True

result = not(num1 < 50) # 부정
print(result) # True








