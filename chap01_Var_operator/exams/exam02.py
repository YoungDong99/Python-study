'''
문2) 다음 밑변, 윗변, 높이를 이용하여 사다리꼴의 넓이를 구하시오.

    조건1) 밑변(base), 윗변(upper), 높이(height)
           변수 선언 : base = 12, upper = 7, height = 9
    조건2) 사다리꼴 넓이(area) 
             area = (base + upper) * height / 2
    조건3) 사다리꼴 넓이(area) 출력 

   <<화면출력 결과>>
  사다리꼴 넓이 =  85.5
'''

# 1. 변수 선언 
base = 12
upper = 7
height = 9

# 2. 사다리꼴 넓이 계산
area = (base + upper) * height / 2

# 3. 사다리꼴 넓이 출력
print('사다리꼴 넓이 : ', area)
