'''
문1) 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오.

 << 출력 결과 >>
단계1 : [10, 1, 5, 2, 10, 1, 5, 2]
단계2 : [10, 1, 5, 2, 10, 1, 5, 2, 20]
단계3 : [1, 2, 1, 2]
'''

lst = [10, 1, 5, 2] # list 생성

# 단계1 : lst 원소를 2개 생성하여 result 변수에 저장/출력 
result = lst * 2
print(result)
# 단계2 : lst의 첫번째 원소에 2를 곱하여 result 변수에 추가/출력
last = lst[0] * 2
result.append(last)
print(result)

# 단계3 : result의 짝수 번째 원소만 result2 변수에 추가/출력
result2 = []
cnt = 0
for i in result :

    if cnt % 2 == 1 :
        result2.append(i)
    cnt += 1
    
# 리스트 형식을 활용한 방법
result2 = result[1::2]

print(result2)
