'''
step04 

문2) 다음 벡터(emp)는 '입사년도 이름 급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 다음과 같은 출력결과가 나타나도록 함수를 정의하시오. 

# <출력 결과>
 전체 사원 급여 평균 : 260.0
'''

# 힌트) 공백으로 단어 분리 : 문자열객체.split(sep = ' ')


# list 자료 
emp = ["2014 홍길동 220", "2002 이순신 300", "2010 유관순 260"]

# 함수 정의
def pay_pro(emp):
    pays = [] # 급여 저장 
    '''
    for e in emp :
        pays.append(int(e[9:]))
    '''    
    for e in emp :
        pays.append(int(e.split(' ')[2]))
        
    return sum(pays)    
        

# 함수 호출 
pay_sum = pay_pro(emp)
print('전체 사원의 급여 평균 :', pay_sum / len(emp))



