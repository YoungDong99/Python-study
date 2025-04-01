# -*- coding: utf-8 -*-
"""
step01_list.py

list 특징 
 - 순서 있는 자료구조
 형식) 변수 = [값1, 값2, ...]
"""

# 1. 단일 list & 색인 
lst = [1,2,3,4,5]
print(lst) # [1, 2, 3, 4, 5]
len(lst) # 5
print(type(lst))

# 색인(index) : 값의 위치
# 색인 연산자 : 객체[n]
lst[:] # 전체 원소 
lst[0] # 첫번째 원소 
lst[-1] # 마지막 원소 

# 범위
lst[1:3] # [2, 3]
lst[:3] # [1, 2, 3]
lst[3:] # [4, 5]
lst[-3:] # [3, 4, 5]

# list + for 이용 
for i in lst : 
    print(i, end = ' ') # 한 줄 중복 출력 


# 2. 중첩 list & 색인 
y = [['a','b','c'], [1,2,3]] 
print(y)  # [['a', 'b', 'c'], [1, 2, 3]]
print(y[0])  # ['a', 'b', 'c']
print(y[0][1])  # b

for i in y :
    print('i =', i)
    for j in i :
        print('j =', j)

# 3. list 값 수정(추가, 삽입, 수정, 삭제)
num = ['one', 2, 'three', 4]  # 복합형 자료형
print(num) # ['one', 2, 'three', 4]


# list의 메서드 확인
dir(num)
'''
'append' : 원소 추가
'clear'  : 모든 원소 제거
'copy'   : 리스트 복사
'count'  : 특정 원소 개수 반환
'extend' : 다른 리스트의 원소를 확장해 추가
'index'  : 특정 원소의 첫 번째 인덱스 반환
'insert' : 원소 삽입
'pop'    : 마지막 또는 특정 인덱스 원소 제거 및 반환
'remove' : 원소 제거
'reverse': 리스트 순서 뒤집기
'sort'   : 리스트 정렬
'''

# 1) list 값 추가 
num.append('five') 
print(num) # ['one', 2, 'three', 4, 'five']

# 2) list 값 삭제 
num.remove('three')
print(num) # ['one', 2, 4, 'five']

# 3) list 값 수정 
num[1] = 'two' 
print(num) # ['one', 'two', 4, 'five']

# 4) list 값 삽입 
num.insert(0, 'zero')
print(num) # ['zero', 'one', 'two', 4, 'five']

num.clear() # 전체 원소 제거


# 4. list 연산 
x = [1, 2, 3, 4]
y = [1.5, 2.5]

# 1) list 결합(+)
z = x + y 
print(z) # [1, 2, 3, 4, 1.5, 2.5]
print(type(z)) # <class 'list'>


# 2) list 확장 : 단일 리스트
x.extend(y) 
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# 3) list 추가 
x.append(y) 
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# 4) list 반복(*)
result = y * 2
print(result) # [1.5, 2.5, 1.5, 2.5]
    


# 5. list 정렬 & 색인 반환  
num = [3,1,5,2]
print(num)

num.reverse() # 배열의 역순정렬(현재 객체 반영) 
print(num)


# 숫자 원소 정렬 
num.sort() #  [1, 2, 3, 5] : 오름차순
print(num)
num.sort(reverse=True) # [5, 3, 2, 1] : 내림차순
print(num)

# 값의 색인 반환 
num.index(3) # 2 
num.index(4) # ValueError: 4 is not in list



# 6. 빈 list에 값 추가와 원소 찾기 

num = [] # 빈 list : 숫자 저장 

# 임의 숫자 입력 
for i in range(5) : # 0~4
    num.append(int(input())) # 프롬프트 없음 

print(num)

# 숫자 원소 찾기 
if int(input()) in num :
    print('숫자 있음')
else :
    print('숫자 없음')


# 7. 리스트와 내장함수
import random
rand_nums = []

for i in range(10) :
    rand_nums.append(random.randint(1, 50))

print('최솟값 :', min(rand_nums))
print('최댓값 :', max(rand_nums))
print('합계 :', sum(rand_nums))
print('평균 :', sum(rand_nums) / len(rand_nums))


