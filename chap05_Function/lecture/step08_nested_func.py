"""
중첩함수(nested function) : 함수에 포함된 함수 

형식)
def outer(인수) :
    명령문
    def inner(인수) :
        명령문
    return inner
"""

# 1. 중첩함수 예
def a() : # outer
    print('a 함수')
    
    def b() : # inner 
        print('b 함수')
    return b # inner 함수 반환 : 클로저

# 단계1. 외부함수 호출
print = a()

# 단계2. 내부함수 호출
print()
original_print = print
print = original_print

# 2. 중첩함수 응용 : 캡슐화(자료 + 함수)
'''
 - outer 함수 역할 : dataset 생성, inner 함수 포함 
 - inner 함수 역할 : dataset 조작 (합계, 평균)
'''


def outer_func(data) : # 외부함수(자료 생성 + 합계, 평균) 
    #dataset = data # dataset 생성 (공용 자료)
    
    # inner 함수 
    def tot() : # 합계
        tot_val = sum(data)
        return tot_val

    def avg(tot_val) : # 평균 
        avg_val = tot_val / len(data)
        return avg_val        
    
    return tot, avg # inner 함수 반환 

# 단계1. 외부함수(데이터생성, 내부함수 반환)
tot, avg = outer_func([1,2,3,4,5])

# 단계2. 내부함수 호출
tot_val = tot()
avg_val = avg(tot_val)

print(f'합계 = {tot_val}, 평균 = {avg_val}')

# 3. nonlocal 명령어 : inner -> outer 값 접근

'''
획득자(getter) 함수 : 함수 내의 값을 외부로 넘기는 함수
지정자(setter) 함수 : 함수 내의 값을 수정하는 함수
'''

def main_func(num) : # outer
    num_val = num # data 생성 
    
    # inner 
    def get_func() : # 값 획득 : 획득자 
        return num_val  
    
    def set_func(value) : # 값 지정 : 지정자 
        nonlocal num_val  # inner가 아닌 outer에서 만든 변수
        num_val = value  
        
    return get_func, set_func


# 외부함수 호출
get_function, set_function = main_func(100)

# 내부함수 호출 : 획득자
num_val = get_function()
print('함수 내의 값 = ', num_val)


# 내부함수 호출 : 지정자
set_function(200)  # 100 -> 200 변경
print('함수 내의 값 = ', num_val)














