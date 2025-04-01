# -*- coding: utf-8 -*-
"""
step03_tuple.py

tuple 특징 
 - 순서 있는 자료구조 
 - 형식) 변수 = (값1, 값2,...)
 - 색인 사용
 - 수정 불가(리스트와 차이점)
"""

# tuple
tp = (10,) # 원소 한개 
print(tp) # (10,) 콤마를 한개는 넣어야 제대로 만들어진다
# (10)으로 입력하면 정수로 인식하므로 콤마 , 필요

tp2 = (1,2,3,4,5)
print(tp2)

print(len(tp2), max(tp2), min(tp2), sum(tp2), type(tp2)) # 5 <class 'tuple'>

# indexing
print(tp2[0], tp2[1:4]) # 1 (2, 3, 4)
print(tp2[-1], tp2[-3:]) # 5 (3, 4, 5)

# 원소 수정 불가
tp2[0] = 100 # TypeError:

# 객체 제거  
del tp2
#print(tp2) # name 'tp2' is not defined


# for + tuple
datas = (10, 23.4, 6, 8)

for d in datas :
    print(d*2, end = ' ')

# 20 46.8 12 16
 

 
    
    
    
    
    
    




