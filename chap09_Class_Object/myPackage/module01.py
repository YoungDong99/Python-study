# -*- coding: utf-8 -*-
"""
chap09 > myPackage > module01.py

현재 모듈 : 함수 또는 클래스
"""



# 함수 정의 
def adder(x, y) :
    return x + y


# 클래스 정의 
class Mul :
    def __init__(self, x, y) :
        self.x = x 
        self.y = y 
        
    def mul(self) :
        return self.x * self.y

# 모듈 이름 확인 명령어 : __name__
print('모듈 이름 : ', __name__)
'''
현재 모듈에서 호출 시 : '__main__'
다른 모듈에서 호출 시 : 'module01'
'''


