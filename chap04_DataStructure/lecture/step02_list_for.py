"""
step02_list_for.py

리스트 내포(comprehension) 
 - list안에서 for와 if문을 한 줄로 표현한 문법

 형식1) 변수 = [실행문  for 변수 in 열거형객체]
        실행순서 : 1.for문 > 2.실행문 > 3.변수저장
        
 형식2) 변수 = [실행문  for 변수 in 열거형객체 if 조건식]
        실행순서 : 1.for문 > 2.if문 > [3.실행문 > 4.변수저장]
"""

# 형식1) 변수 = [실행문  for 변수 in 열거형객체]

# x변량에 제곱(**) 계산 예
x = [2, 4, 1, 5, 8]

print(x ** 2) # TypeError:
    
x = [2, 4, 1, 5, 8] # 5개 원소 

x * 2 # [2, 4, 1, 5, 8, 2, 4, 1, 5, 8] : 반복 

calc = [] # 빈리스트 : 산술연산 저장 

for i in x :
    #print(i * 2) # 각 변량 산술연산 
    calc.append(i * 2)
    
print(calc) # [4, 8, 2, 10, 16]

# 형식1) 변수 = [실행문  for 변수 in 열거형객체] 
calc = [i * 2  for i in x] # 리스트 내포 
   
print(calc) # [4, 8, 2, 10, 16]
    

print(x ** 2) # TypeError: 리스트 ** 2 

# list + for 예   
lst = [] # 계산결과 저장 
for i in x :
    lst.append(i**2)

lst # [4, 16, 1, 25, 64]

# list 내포 
lst = [i ** 2 for i in x]
print(lst)



# 형식2) 변수 = [실행문  for 변수 in 열거형객체 if 조건식]
dataset = list(range(1, 101)) # range(start, stop)
print(dataset)

#  list+for : 10배수 값 저장  
result = [] # 10배수 저장 

for data in dataset :
    if data % 10 == 0 : # 10배수 여부 
        result.append(data)
        
print(result) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 형식2) 리스트 내포 
result = [data  for data in dataset if data % 10 == 0]

print(result) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# 형식1) 1~100 : 짝수 or 홀수 : [실행문 for문 ]
result2 = ['짝수' if data % 2 == 0 else '홀수' for data in dataset]
# 한줄 if문 : 참 if 조건 else 거짓 

print(result2)


# 결측치(NAN) 대체 or 제거 
data = ['1','', '2','','3']
print(data)

# 결측치(NAN) 대체 : 형식1)
na_data = ['nan' if d == '' else d for d in data]
print(na_data) # ['1', 'nan', '2', 'nan', '3']

# 결측치(NAN) 제거 : 형식2) 
na_data2 = [d for d in data  if d != '']
print(na_data2) # ['1', '2', '3']






















    