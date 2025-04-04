"""
문5) 다음 input_data는 A,B,C 세가지 값을 갖는 범주형 변수이다. lambda 함수를 이용하여 
   이 변수의 값을 2진수로 인코딩하시오.
    
    <출력 결과>
    encoding = [[1, 0, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
"""

# mapping table 
map_data = {'A': [1,0,0], 'B': [0,1,0], 'C' : [0,0,1]}


# 범주형 자료 입력 
input_data = ['A','C','A','B','C','B']


# 일반함수
def encoding(data) :
    result = []
    for i in data :
        result.append(map_data[i])
    return result

print('encoding = ', encoding(input_data))



# lambda 함수 정의
result = lambda data : [ map_data[i] for i in input_data ]
print('encoding = ', result(input_data))

# lambda 함수 정의&호출
print('encoding = ',(lambda data : [map_data[i] for i in input_data])(input_data))

