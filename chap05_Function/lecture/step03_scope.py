'''
scope : 변수의 사용범위 

 - 전역변수 : 전 지역 사용 
 - 지역변수 : 함수 내에서 사용(매개변수)
   -> 함수가 종료되면 자동 소멸된다. 1
''' 

del x # 메모리에서 제거 

# 지역변수 : x
def local_func(x) :
    x += 50  # 매개변수=지역변수 
    print('local func(x) =', x) # local func(x) = 100
    result = x + 100 # 지역변수
    print(result) # 200


# 함수호출 
local_func(50) # 값으로 호출 
# 지역변수 : x, result
'''
print(x) # 오류 : 함수가 종료되면 자동 소멸
print(result) # 오류 : 함수가 종료되면 자동 소멸
'''
print(x)
x = 10
# 전역변수 : x
def global_func() :
    global x  # x를 전역변수로 사용 
    x += 50
    print('global_func(x) =', x)  # global_func(x) = 100
    
x = 50 # 전역변수     

# 함수 호출 
global_func()
# 전역변수 : x   
print(x) # 100  
    
   
