# -*- coding: utf-8 -*-
"""
step02

문) 주소 호출 방식(call by reference)으로 my_list의 각 원소에 거듭제곱 연산하여 
    호출자에게 반환하고 출력하기  
   
 <출력결과>
 입력 : [13, 27, 15, 36, 27, 16, 12, 34, 44, 45]
 출력 : [169, 729, 225, 1296, 729, 256, 144, 1156, 1936, 2025]   
"""


# 1. 거듭제곱 함수 정의 
def power_fn(lst):
    power_result = []
    
    '''
    for i in lst :
        power_result.append(i**2)
    '''
    # 리스트 내포 방식
    power_result = [i**2 for i in lst]
    
    return power_result

    



# 2. 난수로 데이터 생성 
import random

random.seed(123) # 난수 시드값 

my_list = [random.randint(10, 50)   for i in range(10)] 

# 입력   
print('입력 :', my_list)  # [13, 27, 15, 36, 27, 16, 12, 34, 44, 45]


# 3. 함수 호출 & 결과 출력 

print('출력 :', power_fn(my_list))









