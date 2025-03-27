# -*- coding: utf-8 -*-
"""
3. escape 문자와 기능차단  
  - escape 문자 (예외문자) : 특수기능으로 사용되는 문자(\, \n, \t, \b, \r, '', "")
"""

print('escape 문자')
print('\n') # 줄바꿈 기능

print('\\n출력') # escape 기능 차단 방법1 : \ 
print(r'\n출력') # escape 기능 차단 방법2 : r 

# 경로 표현 
print('c:\python\test') # c:\python   est
print('c:\\python\\test') 
print(r'c:\python\test')

print('ab\rcd')

# 따옴표로 문자열 강조 : c:\'aa'\"abc.txt"   
print("c:\\\'aa\'\\\"abc.txt\"")


