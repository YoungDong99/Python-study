'''
반복문(while)

형식)
while 조건 :
    실행문
    실행문 
'''

# 1. 카운터와 누적 변수 
cnt = tot = 0 # 초기화

while cnt < 5 : 
    cnt += 1  # 카운터 변수
    tot += cnt #  누적 변수
    print('cnt = %d, tot = %d' %(cnt, tot))

print(cnt, tot) 
print() # line skip


# 2. 1 ~ n까지 수열 누적합
cnt = tot = 0

while cnt < 100 : # 100회 반복
    cnt += 1 # 카운터
    tot += cnt # 누적 합
                
print('1 ~ 100까지 합 = %d' %tot)   

        
# 3. 무한 루프 : 무한 반복문
while True :
    num = int(input('숫자 입력 : '))
    
    if num % 10 == 0 : # exit 조건 
        print('프로그램 종료')
        break # loop exit     
    print('입력 값 -> ', num)


# 컴퓨터 난수 생성 module 
import random  # 난수 관련 함수 제공

dir(random)   # 난수 관련 함수 목록

r = random.randint(1, 10)
print(r)

r2 = random.random()  # 0~1 난수 실수
print(r2)


# 난수 0.01 미만이면 종료 후 난수 갯수 출력 
cnt = 0 
while True :
    r = random.random()
    print(random.random())
    if r < 0.01 :
        print(r)
        break
    else :
        cnt += 1
print(cnt)


# 4. continue, break

i = 0
while i < 10 :
    i += 1 # 카운터
    if i == 3 : 
        continue #  다음 문장 skip
    if i == 6 : # 2차 작성  
        break #  루프 탈출(loop exit)
    print(i, end = ' ') 



# 간단한 게임 만들기
print('>> 숫자 맞추기 게임 <<')

ran = random.randint(1, 100)
cnt = 0
while True :
    num = int(input('예상 숫자 입력 : '))
    if num < 1 or num > 100 :
        print('1~100 사이 숫자를 입력하세요')
        continue
    cnt += 1
    if num == ran :
        print('성공!')
        print('시도횟수 :', cnt)
        break
    elif num > ran :
        print('아래')
    else :
        print('위')
