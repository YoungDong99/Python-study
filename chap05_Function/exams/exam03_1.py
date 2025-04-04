'''
step04 

문1) 다음 벡터(emp)는 '입사년도 이름 급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 리스트 자료를 이용하여 사원의 이름만 추출하는 함수를 정의하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''


# 힌트) 공백으로 단어 분리 : 문자열객체.split(sep = ' ')


# list 자료 
emp = ["2014 홍길동 220", "2002 이순신 300", "2010 유관순 260"]

# 함수 정의
def name_pro(emp):
    names = []
    '''
    for e in emp :
        names.append(e[5:8])
    '''
    
    for e in emp :
        names.append(e.split(' ')[1])
    
    return names


# 함수 호출 
names = name_pro(emp)
print('names =', names)





