'''
step01

문2) 각 층 단위로 별(Start) 출력 및 별의 총 개수 구하기   


<출력 예시>
층수(height) 입력 : 5 
*
**
***
****
*****
별(start) 개수 : 15 
'''


# 1. 함수 정의
def StarCount(height):
    cnt = 0
    for i in range(height) :
        print('*'*(i+1))
        cnt += (i+1)
    return cnt


# 2. 키보드 입력 & 함수 호출 
star_cnt = StarCount(int(input('층수(height) 입력 : '))) # 층 수 입력

# 3. 별(start) 개수 출력 
print('별(start) 개수 : %d'%star_cnt)

