"""
if 관련 문제

문3) 사용자의 나이에 따라서 기본 티켓 요금 1만원은 무료 또는 할인됩니다. 나이가 7세 미만이면
   '무료 입니다.', 18세 미만이면 '청소년 할인'으로 50%, 65세 이상이면 '노인 할인'으로 30%가 
   적용되고, 그 외에 나머지 사용자는 기본 티켓 요금을 받습니다. <출력 예시>를 참고하여 
   조건문을 작성하시오.  

   <출력 예시>
   7세 미만인 경우 : 무료 입니다.
   18세 미만인 경우 : 청소년 할인은 5,000원 입니다.
   65세 이상인 경우 : 노인 할인은 3,000원 입니다.
   기타 사용자인 경우 : 기본 요금은 10,000원 입니다.        
"""

age = int(input("나이를 입력하세요: "))

ticket_price = 10000 # 기본 티켓 요금 

if age < 7 :
    print("무료 입니다.")
elif age < 18 :
    ticket_price = int(ticket_price / 2)
    print(f"청소년 할인은 {ticket_price:,}원 입니다.")
elif age < 65 :
    print(f"기본 요금은 {ticket_price:,}원 입니다.")
else :
    ticket_price = int(ticket_price * 0.3)
    print(f"노인 할인은 {ticket_price:,}원 입니다.")

