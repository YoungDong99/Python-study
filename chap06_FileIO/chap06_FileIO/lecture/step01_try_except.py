'''
예외처리 예 
  - file/DB 입출력 시 문제 발생  
  - 반복 수행 과정에서 계산이 불가능한 자료 포함
  - url을 이용하여 웹문서를 수집할 경우 해당 url이 없는 경우 

예외처리 형식)  
try :
    예외발생 코드 
except 예외처리클래스 as 변수: 
    예외처리 코드 
finally :
    항상 실행 코드

 
'''
# 1. 반복 수행 과정에서 계산이 불가능한 자료 포함

print('프로그램 시작 !!!')
x = [10, 20, 5, 30, 'num', 7 ]

for i in x :
    try :
        # 예외발생 가능성이 있는 코드
        print(i)    
        y = i**2  
        print('y =', y)
    except Exception as e:  # 예외정보 제공
        # 예외를 처리하는 코드(메세지, 명령어)
        print('e : ', e)
        print('숫자 아님')
    finally :  # 무조건 실행
        print('프로그램 종료')

print('프로그램 종료')


    
# 2. 유형별 예외처리 
try:
    num = int(input("정수를 입력하세요: "))
    result = 10 / num
    print("결과:", result)
    open('test.txt', mode='r')
except ValueError : 
    print("유효한 숫자를 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception :
    print("기타 오류 발생:")   
    


# 3. 예외처리 : 응용
texts = ["홍길동 사원 10", "이순신 관리자 20", "을지문덕", "강감찬 이사 30", "유관순 과장 20"]
type(texts[0])

positions = []
for st in texts :
    try :
        tokens = st.split(' ')
        positions.append(tokens[1])  # 예외발생
    except Exception as e :
        print('예외발생 : ', e)

print('positions : ',positions) # positions :  ['사원', '관리자', '이사', '과장']



















    
    
    
    
    
    
    