'''
패키지(Package) = 폴더 
 - 유사한 모듈(python file)을 꾸러미로 묶어놓은 단위
 - __init__.py : 패키지 초기화 

모듈(Module) = 파일 
 - 함수와 클래스로 구성된 python file(*.py)
'''

# 주의 : 임포트할 패키지의 상위 경로 변경 

import os # os 관련 함수 : file 경로 확인, 변경
#os.getcwd() # 경로 확인 

os.chdir(r'C:\ITWILL\2_Python\workspace\chap09_Class_Object')# 디렉터리 변경 


# 형식1) from 패키지명.모듈명 import 함수명 
from myPackage.module01 import adder, Mul # 함수 or 클래스

#모듈 이름 :  myPackage.module01

add = adder(10, 20) # 함수명 
print('add = ', add) # add =  30

m = Mul(10, 20) # 클래스명() : 생성자  
print('mul =', m.mul()) # 객체.메서드() : mul = 200


# 형식2) import 패키지명.모듈명 as 별칭 
import myPackage.module01 as md

add = md.adder(10, 20)
print('add = ', add) # add =  30

m = md.Mul(10, 20) 
print('mul =', m.mul()) # mul = 200

type(m) # __main__.Mul


