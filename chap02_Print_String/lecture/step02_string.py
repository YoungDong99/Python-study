
"""
2. 문자열과 문자열 처리 
"""


# 1. 문자열 유형 

# 1) 한 줄 문자열 
lineStr = "this is one line string" 
multiLine

print(lineStr, type(lineStr))
# <class, 'str'> : 자료형, 객체의출처

# 2) 여러줄 문자열 
multiLine = """This
is multi line
string"""

print(multiLine)

# 3) sql문 
deptno = int(input('조회부서번호 입력 : '))

query =f"""select * from emp
where deptno = {deptno}
order by sal desc"""

print(query)

# 2. indexing/slicing 가능 
'''
색인(index) : 값의 위치
색인 연산자 : 객체[n]
slicing : 자르기 & new 객체 생성
'''

# 1) indexing
# 왼쪽 기준 색인 
print('왼쪽의 첫번째 문자 : ', lineStr[0]) 
print(lineStr[0:4]) 

# 오른쪽 기준 색인 
print(lineStr[-1]) 
print(lineStr[-6:]) # 뒤에서 6번쨰~끝까지

# 2) slicing 
subStr = lineStr[:4]
print(subStr) # this
print(id(subStr), id(lineStr))

'''
색인연산자[start:stop:step]
'''
text = "우리나라 대한민국 만세"
print(text)
print(text[:4])   # 우리나라
print(text[:])    # 전체 문자열 선택
print(text[::2])  # 우나 한국만
print(text[::-1]) # (문자열 뒤집기)

# 3. 문자열 연산 
print('python' + ' program') # 결합연산자 

print('-'*50) # 반복연산자 


# 4. 문자열 처리 함수 

# 형식) 문자열객체.메서드()
'''
함수 vs 메서드
함수 : 단독 호출
메서드 : 객체를 통해서 호출 함수
'''

testStr = "my name is hong!!"  
print(type(testStr)) # 문자열객체

# 문자열객체의 메서드 확인
dir(testStr)

# 1) 문자 찾기 
testStr.find('z') # -1
testStr.find('m') # 0
testStr.find('h') # 11

# 2) 문자 개수 반환  
testStr.count('n') 

# 3) 문자 유형 여부  
testStr.isalpha() # False > 공백이 있으므로 순수 알파벳X
testStr.isascii() # True  > 한글이 있으면 false
testStr.islower() # True  > 전부 소문자로 구성O


testStr2 =" hello python!! " 

# 4) 공백제거 & 문자열 시작 대문자 변환 
result = testStr2.strip() # 앞뒤 공백제거 
print(result, type(result)) 

'''
문자열객체.strip() : 공백제거
문자열객체.split() : 공백 기준 단어 생성

'''
result_split = testStr2.split()
print(result_split, type(result_split)) # 리스트로 반환됨

result.capitalize() # 문자열 시작 대문자 변환 

# 5) 대소문 처리 
result.upper() 
result.lower() 


# 6) 접두어 판단 -> T/F
result.startswith('he') 
result.startswith('He') 


# 7) 단어 교체 
result.replace('!', '')
result.replace(' ', '')


# 5. 문자열 분리(split) & 결합(join)
'''
 split : 문장 -> 단어 분리   
 join : 단어 -> 문장 결합 
''' 

print(multiLine)
'''
This
is multi line
string
'''

# 1) split() : 문자열 분리
# 문단 -> 문장 분리
sents = multiLine.split(sep='\n')
print(sents)  # 줄단위로 구분된 원소로 리스트 생성
print('문장 길이 :', len(sents))

# 문단 -> 단어 분리
words = multiLine.split()
print(words)
print('단어 길이 :', len(words))


# 2) '구분자'join() : 문자열 결합
# 단어 -> 문장
new_sents = ' '.join(words)
print(new_sents)

# 문장 -> 문단
new_sents2 = '\n'.join(sents)
print(new_sents2)
'''
This
is multi line
string
'''


