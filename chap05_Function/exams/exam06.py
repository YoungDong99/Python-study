"""
문6) 다음 blood 변수는 8명의 혈액형 정보를 갖는 범주형 변수이다. lambda 함수를 이용하여 
    이 변수의 값을 10진수로 인코딩하는데 만약 map_data에 없는 혈액형은 -1값으로 표시하시오.
   (혈액형과 10진수 관계 : A : 0, B : 1, O : 2 AB : 3 )   
    
    <출력 결과>
    digit = [2, 1, 0, 3, -1, 2, 0, -1]
"""

# mapping table : 혈액형과 10진수 관계 
map_data = {'A':0, 'B':1, 'O':2, 'AB':3} # dict table 


# 혈액형 입력 자료  
blood = ['O','B','A','AB','C','O','A','BA']



# 일반 함수
def digit(data) :
    result = []
    for i in data :
        if i not in map_data.keys() :
            result.append(-1)
        else :
            result.append(map_data[i])
            
    return result

print('digit = ', digit(blood))


# lambda 함수

digit = lambda data : [ map_data[i] if i in map_data.keys() else -1 for i in data ]

print('digit = ', digit(blood))


# lambda 함수 정의&호출
(lambda data : [ map_data[i] if i in map_data.keys() else -1 for i in data ])(blood)


