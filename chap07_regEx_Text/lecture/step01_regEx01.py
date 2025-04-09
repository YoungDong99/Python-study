"""
정규 표현식(Regular Expressions)  
 - 특정한 규칙을 가진 메타문자를 이용하여 패턴을 지정하는 문자열  

[주요 메타문자]
.x : 임의의 한 문자 뒤에 x가 오는 문자열(예 : .bc -> abc, mbc) 
x. : x 다음에 임의의 한 문자가 오는 문자열(예 : t. -> t1, t2, ta) 
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x* : x가 0번 이상 반복
x+ : x가 1회 이상 반복
x? : x가 0 또는 1회 포함 
x{n} : x가 n 연속
x{m, } : x가 m 이상 연속 
x{,n} : x가 n 이하 연속
x{m, n} : x가 m~n 사이 연속 
[x] : x문자 한 개 일치
[^x] : x문자 제외 
| : or 조건식(예 : [a-z|A-Z]) 
\ : 이스케이프 문자 또는 일반문자를 메타문자로 변환(예: '\d', '\w', '\s')
() : 그룹핑[예 : '([a-z]{3}|\d{3})' ] 
"""


import re # 정규표현식 관련 모듈  

dir(re)
'''
findall('패턴', 문자열) : 패턴과 일치하는 모든 문자열 찾기
match('패턴', 문자열) : 패턴과 문자열의 일치 여부
search('패턴', 문자열) : 패턴과 일치하는 문자열 찾기
split() : 문자열 분리
sub() : 문자열 교체
'''


### 1. re.findall('pattern', string) 
# - 패턴과 일치하는 모든 문자열을 찾아서 list 반환  

st1 = '1234 abc홍길동 ABC_555_6 이사도시' 

# 1) 숫자 찾기 : 메타문자([], {}) 이용   
print(re.findall('1234', st1))  # ['1234']
print(re.findall('[0-9]', st1))  # ['1', '2', '3', '4', '5', '5', '5', '6']

# d : digit 모든 숫자를 찾아서 반환
print(re.findall('\d', st1))  # ['1', '2', '3', '4', '5', '5', '5', '6']
print(re.findall('[0-9]{3}', st1))  # ['123', '555']

print(re.findall('[가-힣]{3,}', st1))  # ['홍길동', '이사도시']
print(re.findall('[a-z]{3}', st1))  # ['abc']

# 2) 문자열 찾기 : 메타문자(|) 이용 
print(re.findall('[가-힣]{3,}', st1)) # 한글 음절 3개 이상 : ['홍길동', '이사도시']
print(re.findall('[a-z]{3}', st1)) # 영문 소문자 3개 : ['abc']
print(re.findall('[a-z|A-Z]{3}', st1)) # 영문자 소.대문자 : ['abc', 'ABC']

    
# 3) 접두어/접미어, 중간 문자열 찾기 : 메타문자(^, $, .)
st2 = 'test1abcABC 123mbc abbc,ac 45text'  

print(re.findall('^test', st2))  # ['test']
print(re.findall('^text', st2))  # [] : 패턴과 일치하는 문자열이 없음
print(re.findall('text$', st2))  # ['test']

# 문자열 중간에서 문자 찾기 : 메타문자(.) 
re.findall('.bc', st2) # ['abc', 'mbc', 'bbc']
re.findall('b.', st2) # ['bc', 'bc', 'bb']


# 4) 단어(word) : 메타문자(\w) : 영문자, 숫자, 한글(제외 : 특수문자, 공백)  
st3 = 'test^홍길동 abc 대한 민국 123$tbc'

words = re.findall('\w{3,}', st3)
print(words)  # ['test', '홍길동', 'abc', '123', 'tbc'] 


# 5) 문자열 제외 : 메타문자([^제외문자])
print(re.findall('[^t]+', st3)) # t제외한 나머지 문자 1개 이상(+) 
# ['es', '^홍길동 abc 대한 민국 123$', 'bc']

# 불용어(특수문자 or 공백)
print(re.findall('[^^$\s]+', st3))
## ['test', '홍길동', 'abc', '대한', '민국', '123', 'tbc']

st4 = 'abcABC 123mbc abbc ac 45text'

# 6) 문자 반복 : 메타문자(*, +, ?)
print(re.findall('ab*c', st4)) # ['abc', 'abbc', 'ac'] : b가 0번 이상 

print(re.findall('ab+c', st4)) # ['abc', 'abbc'] : b가 1번 이상 

print(re.findall('ab?c', st4)) # ['abc', 'ac'] : b가 0번 또는 1번 


'''
html = ["<h1>내용</h1>", "<h2>제목</h2>", "<h3></h3>"]

result = []
for tag in html :
    result.append(re.findall("<h.>.+</h.>", tag))

print(result) # [['<h1>내용</h1>'], ['<h2>제목</h2>'], []]
'''

# 2. re.match(pattern, string) 
# - 패턴과 일치하는 문자열 이면 객체 반환(불일치 NULL 반환) 
# 유의성 검증 : 주민번호, 이메일 형식

jumin = '123456-3234567'

result = re.match(r'\d{6}-[1-4]\d{6}', jumin) 
# 패턴 일치 여부 반환 : 일치 -> object 반환, 불일치 -> NULL(None) 반환 

print(result) # <re.Match object; span=(0, 14), match='123456-3234567'>
'''
span : 일치된 문자열 범위(색인)
match : 일치된 문자열
'''


# 매칭된 텍스트 반환 
result.group() # '123456-3234567'


if result : # object 반환 : True,  None : False 
    print('주민번호 양식')
else :
    print('잘못된 양식')

