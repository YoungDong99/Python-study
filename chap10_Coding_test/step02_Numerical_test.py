
### 2. 수치 연산 : 수열을 대상으로 연산(피보나치 수열, 팩토리얼 계산) 


# [1] 팩토리얼 계산하기 : 정수 N을 입력받아서 N의 팩토리얼을 계산
'''
 예) n=5 일 때 1*2*3*4*5 = 120
'''
def factorial(n) :
    result = 1
    
    for i in range(1, n + 1): 
        result *= i 
    
    return result


# 테스트 입력
n = 5
print('result =',factorial(n))  # result = 120



# [2] 피보나치 수열 출력하기 : 정수 N을 입력받아 N의 피보나치 수열 나열  
'''
피보나치 수열 : 두 개의 항을 더하여 다음 항을 만드는 수열
예) n=8 -> [0, 1, 1, 2, 3, 5, 8]
'''

def fibonacci_numbers(n) :
    fib_nums = [0, 1]  # 피보나치 수열의 배열  
    
    while True:
        next_num = fib_nums[-1] + fib_nums[-2]  
        
        if next_num > n:   
            break # 반복 중단 조건
        
        fib_nums.append(next_num)  
        
    return fib_nums

# 테스트 입력
n = 8
print('result =', fibonacci_numbers(n)) # [0, 1, 1, 2, 3, 5, 8]

n = 34
print('result =', fibonacci_numbers(n)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]




'''
 [문제] 반복문과 조건문을 활용하여 다음 수열의 합을 구하시오.
        수열 : -1, 3, -5, 7, -9, 11, -13, ... ,N
        
        예) N = 100 일 때 수열합 = 50 
'''

# 힌트) 부호 변경 
sign = -1
print('sign =', sign) # sign = -1
print('sign =', sign * -1) # sign = 1



def number_sequence(N) :      
    total = 0 # 수열의 합 초기화 
    sign = -1  # 첫 항이 -1이므로 시작 부호는 음수
    
    '''
    ## 항 개수가 N개인 수열의 합
    num = 1
    for i in range(1, N+1) :
        if i % 2 == 1 :
            total += num * sign
        else :
            total += num * (sign * -1)
        num += 2
    '''
    
    
    ## 해답 : N까지 포함 가능한 범위 내에서 수열 구성 후 합 구하기
    for num in range(1, N+1, 2) :
        total += sign * num
        sign *= -1
    
    
    '''
    ## while문 이용
    i = 0
    while i < N :
        i += 1
        if i % 2 != 0 :
            total += sign * i
            sign = sign * -1
    '''
    
    return total # 수열의 합
    

# 함수 호출 
total = number_sequence(100)

print(total)

