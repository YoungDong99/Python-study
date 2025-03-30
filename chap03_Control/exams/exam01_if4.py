'''
if 관련 문제

문4) 강의자료 '제3-1장 조건문'의 ppt.9쪽의 Solution 내용을 중첩 if~else 형식으로
      작성하시오.  
    
    <조건1> snow와 umbrella 변수는 1(있음) 또는 0(없음)만 입력할 수 있다.     
           만약 두 변수의 값이 1 또는 0이 아닌 경우 '다시 입력하세요.' 메시지를 출력한다.
    <조건2> 두 변수의 값이 정상적으로 입력된 경우 다음 3가지 상황에 맞게 메시지를 출력한다.
          상황1 : 눈이 오지않으면 '외출한다.'
          상황2 : 눈이 오고, 우산이 있으면 '외출한다.'
          상황3 : 눈이 오고, 우산이 없으면 '잠시 기다린다.'    
'''   

# 키보드 입력 : 1 또는 0만 입력 
snow = int(input('눈 여부(1 or 0) : ')) 

if snow != 0 and snow != 1 :
    print('다시 입력하세요.')
else :
    if snow == 1 :
        umbrella = int(input('우산 여부(1 or 0) : ')) 
        if umbrella != 0 and umbrella != 1 :
            print('다시 입력하세요.')
        elif umbrella == 1 :
            print('외출한다.')
        else :
            print('잠시 기다린다.')
            
    else :
        print('외출한다.')

