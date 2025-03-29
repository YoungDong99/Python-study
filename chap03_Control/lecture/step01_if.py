'''
형식1)
if 조건 :
    실행문
'''

var = 10 # 초기화 
if var >= 5 :
    print('var=', var)
    print('var는 5보다 크다.')

print('항상 실행하는 명령문')


'''
형식2) 
if 조건 :
    실행문1 : 조건 True
else :
    실행문2 : 조건 False 
'''

var = int(input('var 변수에 값 입력 : ')) # 키보드 입력 

if var >= 5 :
    print('var는 5이상')
else :
    print('var는 5미만')


'''
형식3) if ~ elif ~ else 
if 조건식1 :
    실행문1 -> 조건식1 True
elif 조건식2 :
    실행문2 -> 조건식2 True
else :
    실행문3 -> 모든 조건 False
'''


'''
예) 성적에 대한 등급 구하기
      점수 : 100~90 : 'A학점', 89~80 : 'B학점', 79~70 : 'C학점', 69미만 : '재수강'
''' 

score = 85 # 점수 

# 중첩 if ~ else 
if score < 0 or score > 100 : 
      print('점수 잘못 입력')
else :
    if score >= 90 :
        print('A학점')
    elif score >= 80 :
        print('B학점')
    elif score >= 70 :
        print('C학점')
    else :
        print('재수강')


# 블록 if vs 한 줄 if 

# 블록 if
num = 9

if num >= 5 :
    result = num + 5
else :
    result = num * 5
    
print('result =', result) # result = 14


# 한 줄 if
# 형식) 변수 = 참 if 조건식 else 거짓
result = num+5 if num >= 5 else num * 5
print('result =', result)


# 목록에서 값 찾기
# 형식) if 값 in 목록 :

names = ['홍길동', '이순신', '유관순']

if '이순신' in names :
    print('찾는 이름 있음')
else :
    print('찾는 이름 없음')


# 조건식 : 함수를 이용
text = '서울시 강남구 대치동'
text2 = '수원시 장안구 파장동'

if text2.startswith('서울시') :
    print('서울시 주소')
else :
    print('기타 주소')

