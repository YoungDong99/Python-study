﻿
'''
문1) 다음과 같이 수량과 단가 변수를 만들어서 금액을 출력하시오.

 조건1) 수량 변수 : su = 5
 조건2) 단가 변수 : dan = 800
 조건3) 주소 확인 : 수량과 단가 변수  
 조건4) 금액 계산 : price = 수량 * 단가 


<화면출력 예시>
su 주소 : 1858560352
dan 주소 : 2241324818224
금액 = 4000
'''
# 1. 변수 초기화 
su = 5
dan = 800
price = su * dan

# 2. 변수의 주소 출력 
print('su 주소 : ', id(su))
print('dan 주소 : ', id(dan))
print('price 주소 : ', id(price))

#  3. price 계산 & 출력 
print('수량 : ', su)
print('단가 : ', dan)
print('금액 : ', price)










