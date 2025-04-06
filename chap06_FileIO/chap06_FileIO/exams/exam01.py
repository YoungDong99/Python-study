"""
문1) 학생 3명의 이름과 점수를 키보드로 입력받아서 students 사전에 이름을 키로 성적을 값으로 저장합니다.
     이때 점수는 반드시 정수만 되어야 한다. 만약 다른 자료형이 입력되는 경우에는 사전에 저장하지 않고 
     정상 자료만 사전에 등록되도록 하시오.    
     
     <출력 예시 : 정상 입력된 경우>
     이름을 입력하세요: 홍길동
     점수를 입력하세요: 50
     이름을 입력하세요: 이순신
     점수를 입력하세요: 80
     이름을 입력하세요: 유관순
     점수를 입력하세요: 75
     {'홍길동': 50, '이순신': 80, '유관순': 75}
     
     <출력 예시 : 비정상 입력된 경우>
     이름을 입력하세요: 홍길동
     점수를 입력하세요: test
     유효한 점수를 입력하세요.
     이름을 입력하세요: 이순신
     점수를 입력하세요: 80
     이름을 입력하세요: 유관순
     점수를 입력하세요: 75
     {'이순신': 80, '유관순': 75}
"""

students = {} #  {'이름' : 점수} 

'''
힌트) dict에 원소 추가 예 : students[name] = score
'''


for i in range(3) :
    try :
        name = input("이름을 입력하세요: ")
        score = int(input("점수를 입력하세요: "))
        students[name] = score
        
    except Exception as e:
        print('유효한 점수를 입력하세요')
        print('예외정보 : ', e)
    
print(students)



'''
name 입력에서 Ctrl + c 가 발생해도 예외 처리하는 코드
'''
        
students = {}


for i in range(3):
    try:
        name = input("이름을 입력하세요: ")
        score = int(input("점수를 입력하세요: "))
        students[name] = score

    except ValueError as e:
        print(f"입력 오류: {e}. 올바른 값을 입력하세요.")
    
    except KeyboardInterrupt:
        print("\n입력이 중단되었습니다. 프로그램을 종료합니다.")
        break



print(students)


