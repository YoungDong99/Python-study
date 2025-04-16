# -*- coding: utf-8 -*-
"""
chap09 > myPackage > module02.py 

현재 모듈 : Add, Sub, Mul, Div
"""

# 함수 정의 
def Add(x, y) :
    return x + y

def Sub(x, y) :
    return x - y

def Mul(x, y) :
    return x * y

def Div(x, y) :
    return x / y


if __name__ == '__main__' :  # 프로그램 시작점(다른 모듈에서 실행 안됨)      
    # 함수 호출     
    add = Add(10, 20)        
    print('덧셈=', add)
    # 클래스 객체 생성 
    div = Div(10, 20)
    print('나눗셈=', div)
else :
    print('dd')
    

    
print(__name__)


import myPackage.module01 as md

a = md.Mul(1, 2)

type(a)


    





