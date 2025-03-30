"""
if 관련 문제

문2) 다음은 온라인 주문 금액에 따라서 할인 프로모션을 행사하고 있습니다. 주문 금액이 5만원
     이상인 고객에게 주문 금액의 10%을 할인하고, 5만원 미만의 고객에게는 할인이 없습니다.
     
     <출력 예시>
     주문 금액을 입력하세요: 80000  -> 주문 금액이 5만원 이상인 경우  
     할인 금액 : 8,000원
     총 결제 금액 : 72,000원
     
     
     주문 금액을 입력하세요: 45000  -> 주문 금액이 5만원 미만인 경우 
     할인 없음
     총 결제 금액 : 45,000원
"""

order_amount = float(input("주문 금액을 입력하세요: "))
discount = 0
total_price = order_amount

if order_amount >= 50000 :
    discount = int(order_amount * 0.1)
    print(f"할인 금액 : {discount:,}원")
else:
    print("할인 없음")

total_price = int(order_amount - discount)

print(f"총 결제 금액 : {total_price:,}원")

