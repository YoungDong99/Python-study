"""
함수 호출 방식
1. call by value : 값으로 호출(실인수=값) 
2. call by reference : 주소로 호출(실인수=주소) 
"""

# 1. call by value  
def modify1(value) :
    lst = [100, 200]  # 리스트 객체 생성 
    lst.append(value) # 리스트 추가 
    print(lst) # [100, 200, 5]


# 함수 호출 
modify1(5)  # 값 전달(값으로 호출)  
# 함수 종료 후 : 함수에서 생성된 객체 메모리에서 소멸 
#print(lst) # NameError: name 'lst' is not defined



# 2. call by reference 
def modify2(lst):    
    lst += [100, 200] # 리스트 주소 + [100, 200]  
    print(lst) # [1, 2, 3, 4, 5, 100, 200]


# lst : 참조변수(객체의 주소)  
lst = [1, 2, 3, 4, 5] # 리스트 객체 생성 

# 함수 호출 
modify2(lst) # 주소 전달(주소로 호출) 
print(lst) # [1, 2, 3, 4, 5, 100, 200]



# 주소 전달 예) 리스트 원소의 평균 구하기    
def avg_fn(lst) :
    tot = sum(lst)
    avg = tot / len(lst)
    return avg


my_list = [10, 25, 13, 40, 5] # 값 

avg = avg_fn(my_list) # 주소 호출 
print('원소의 평균 =', avg) # 원소의 평균 = 18.6

'''
리스트 연산 vs 문자열 연산
리스트 연산 : 같은 주소 저장(동일 객체) 
문자열 연산 : 다른 주소 저장(새 객체) 
'''
lst = [1,2,3]
print(id(lst)) # 1997842667008

lst += [4,5] # 리스트 결합(연산) 
print(id(lst)) # 1997842667008
print(lst) # [1, 2, 3, 4, 5]

st = "abc"
print(id(st)) # 140728919130856

st += "de" # 문자열 결합(연산)
print(id(st)) # 1997842325136


# 3. 문자열 주소 호출  
def modify3(msg) :
    print(id(msg)) # msg 주소 : 연산 전 : 1997842578224
    msg += 'to you' # 문자열 연산  
    print(id(msg)) # msg 주소 : 연산 후 : 1997842578416
                   

msg = 'Happy Birthday' # 문자열 객체 
print(id(msg)) # 1997842578224

# 함수 호출 
modify3(msg) # 주소 전달(주소로 호출) 


