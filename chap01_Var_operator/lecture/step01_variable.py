
# 1. 변수와 자료형 
# 형식) 변수명 = 값 or 수식 or 변수

var1 = "Hello python"
var2 = 'Hello python'
print(var1)
print(var2)

# 변수 자료형 확인  
print(type(var1), type(var2)) 

var1 = 100 # 변수 수정  
print(var1, type(var1)) 

var3 = 123.2345
print(var3, type(var3)) 

var4 = True
print(var4, type(var4)) 


# 2. 변수명 작성 규칙(ppt.21 참고)
'''
- 첫자 : 영문자 or _ 사용가능 
- 두번째 : 숫자 사용 가능 
- 대소문자 구분(Score, score)
- 낙타체 : 두 단어 결합(korScore)
- 명령어, 클래스명, 함수명 사용불가, 한글명 비권장
- 점(.) 사용 불가  
'''

_num = 10
_Num = 20
print(_num, _Num)   # 대소문자 구분


# 낙타체
korScore = 89
matScore = 75
engScore = 55

tot = korScore + matScore + engScore
print('tot =', tot) # tot = 219


# 명령어(예약어) 사용 불가
# True = 10 : 오류

# python 명령어 확인
import keyword # 모듈 가져오기

kword = keyword.kwlist
print(kword)

# len(변수 or 값) : 길이(size) 반환
print(kword, len(kword))

# 3. 참조변수 : 객체가 저장된 메모리 주소 저장
x = 150 # x는 150 객체의 주소 저장 
x2 = x # x의 주소 복사 
y = 150

# 변수의 값을 출력
print(x, x2) #150 150
print(x) # x의 내용 출력 

# id(변수) : 해당 변수의 주소 확인
print(id(x)) # x의 주소 출력
print(id(x2)) 
print(id(y))   
# >> 변수명이 서로 달라도 같은 주소를 가짐






