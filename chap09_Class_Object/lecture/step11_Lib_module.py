# 유용한 모듈 : r"C:\Users\itwill\anaconda3\Lib"

# 1. COPY 모듈
import copy # 내용 복제 

colors = ["red", "blue", "green"]
clone = colors # 주소 복제(낮은복제) 
clone = copy.deepcopy(colors) # 내용 복제(깊은복제) 
clone[0] = "white"
print(colors) # ['red', 'blue', 'green']
print(clone) # ['white', 'blue', 'green']

# 2. KEYWORD 모듈
import keyword 

print(keyword.kwlist) # 명령어(예약어)

# 3. RANDOM 모듈 : 난수 생성 
import random

print(random.randint(1, 6)) # a ~ b 난수정수 
print(random.random()) # 0 ~ 1 난수 실수 

myList = [ "red", "green", "blue" ]
print(random.choice(myList)) # blue


# 4. TIME 모듈
import time

def fib(n): # 피보나치 수열 출력
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
        print()
        
start = time.time() # 시작시간 
fib(100000000000000000000000) # 함수 호출 
end = time.time() # 종료시간 
print('소요시간 :', end-start) # 소요시간 : 0.0009961128234863281

# 5. CALENDAR 모듈
import calendar

cal = calendar.month(2025, 4)
print(cal)
'''
     April 2025
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
'''

# 6. OS 모듈
import os # file 경로확인, 폴더이동, 폴더생성, 폴더삭제 

dir(os)
'''
chdir : 폴더이동 
getcwd : 경로확인
mkdir : 폴더생성
remove : 폴더삭제
rename : 폴더이름변경 
'''

print(os.getcwd()) # C:\ITWILL\2_Python\workspace\chap09_Class_Object

print(os.listdir(".")) # ['exams', 'lecture', 'myPackage']



































