"""
함수 응용 

1. 텍스트 전처리 함수 정의 
2. 통계 계산 함수 : 표본의 분산/표준편차 
"""

# 1. 특정 패턴을 가진 문자열 추출
def extract_matching_strings(str_list, pattern):
    matching_strings = [] # 빈 list
    
    for st in str_list :
        if pattern in st :
            matching_strings.append(st)
    
    # list 내포 
    #matching_strings = [st for st in str_list if pattern in st]
    return matching_strings


str_list = ["apple", "banana", "cherry", "kiwi", "lemon"]
pattern = "le"

result = extract_matching_strings(str_list, pattern)
print("매칭된 문자열:", result) # 매칭된 문자열: ['apple', 'lemon']


# 2. 딕셔너리 리스트에서 특정 키의 값 추출
def extract_values_by_key(data_list, key):
    values = [item[key] for item in data_list if key in item]
    return values

data_list = [
    {"name": "Alice", "age": 25, "city": "New York"}, # dict : 1행 
    {"name": "Bob", "age": 30, "city": "Los Angeles"}, # dict : 2행 
    {"name": "Charlie", "age": 35} # dict : 3행 
] # list 

key = "age"
key = "name"
key = "city"

result = extract_values_by_key(data_list, key)
print("추출된 값들:", result) # 추출된 값들: [25, 30, 35]
# 추출된 값들: ['Alice', 'Bob', 'Charlie']
# 추출된 값들: ['New York', 'Los Angeles']


# 3. 숫자 리스트에서 짝수 필터링
def filter_even_numbers(num_list):
    even_numbers = [x for x in num_list if x % 2 == 0]
    return even_numbers

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even_numbers(num_list)
print("짝수 리스트:", result) # 짝수 리스트: [2, 4, 6, 8, 10]   


# 4. 통계 처리 함수 : 표본의 분산/표준편차 계산 함수
dataset = [2,4,5,6,1,8] # 표본(sample)

# 표본 분산과 표준편차 
from statistics import mean, variance, sqrt # 평균, 분산, 제곱근  

print('표본 평균 =', mean(dataset)) # 표본 평균 = 4.333333333333333
print('표본 분산 =', variance(dataset)) # 표본 분산 = 6.666666666666667
print('표본 표준편차 =', sqrt(variance(dataset))) # 표본 표준편차 = 2.581988897471611

'''
표본 분산 = sum((x변량-산술평균)**2) / n-1
표본 표준편차 = sqrt(표본분산)
'''

