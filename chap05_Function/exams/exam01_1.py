'''
step01 

문1) start ~ end 사이의 합계 구하기(단 start는 end 보다 적거나 같다.)   

<출력 예시>
start : 1
end : 5

합계 = 55
'''

# 1. 함수 정의
def get_sum(start, end):
    sum_value  = 0
    
    for i in range(start, end+1) :
        sum_value += i
            
    return sum_value


# 2. 키보드 입력 
start = int(input('start : '))
end = int(input('end : '))


# 3. 함수 호출 & 합계 출력 
sum_value = get_sum(start, end) 

print('합계 =', sum_value)
