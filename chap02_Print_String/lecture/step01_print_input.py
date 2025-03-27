"""
1. 표준 입출력 함수  
"""

# 1. print() 
# - 콘솔 출력 함수 

help(print)
# 도움말(함수명) : 내장함수(built-in function) 확인


# 1) 기본 인수 : sep = ' '
print("value =",10,10+20)  # 생략하면 공백
print('010','1234','1111', sep='-') # 사용자 지정

# end 속성 
print('value =', 10, end=',' )
print('value =', 20) # value = 10,value = 20

# file 속성 : file=None
f = open('output.txt', mode='w') # 출력파일 생성
print('Hello python !!', file=f)
f.close()



# 2) % 양식문자 
# 형식) print('%양식문자' %값) - ppt.3

num1 = 10; num2 = 20  # 한줄에 작성가능
tot = num1 + num2 
print('%d + %d = %d' %(num1, num2, tot)) 

print('이름은 %s이고, 나이는 %d 이다.' %('홍길동', 35))

print('원주율 = %8.3f' %3.14159) 

# 50%
print('전체 찬성률은 %d%%이다.'%50) 

# 분류정확도 출력 : 포맷팅
title = "분류정확도는 %.2f 이다."
acc = 145/150
print(title %acc)

# 3) format()함수 이용 
'''
- 문자열 포멧팅
print('%양식문자' %값)
print('{}'.format(값))
'''
# [1] 위치 기반 포멧
print('이름은 {}이고, 나이는 {}이다.'.format('홍길동', 35))

# [2] 색인과 양식 포멧
print('정수형 = {0}, {1:5d}, 연봉 : {2:3,d}'.format(123, 1234, 2500))
print('원주율 = {0:.3f}, {1:8.3f}'.format(3.14159, 3.14159))


# [3] format(값, '양식')
print('원주율 = ', format(3.14159, '5.3f'))

# SQL문 작성
ename = "홍길동"; deptno = 20
sql = "SELECT * FROM emp WHERE ename='{}' AND deptno={}".format(ename, deptno)

# 축약형 format
sql = f"SELECT * FROM emp WHERE ename='{ename}' AND deptno={deptno}"
print(sql)



# 2. input()
# - 키보드로 입력받는 함수 
help(input)

# 키보드 입력 -> 정수형 변환 
inp = input('키보드 입력: ')
print(inp)

# input() : 문자로 입력되므로 숫자로 사용시 형변환 필요
a = int(input('첫번째 숫자 입력 : ')) # 10
b = int(input('두번째 숫자 입력 : ')) # 20


c = a + b
print('c=', c) # c= 30


# 3. 자료형 변환 
# - 현재 자료형을 다른 자료형으로 변환 
'''
 int() : 문자형 -> 정수형 변환
 float() : 문자형 -> 실수형 변환
 str() : 숫자형 -> 문자형 변환
 bool() : 숫자형 -> 논리형 변환
'''






