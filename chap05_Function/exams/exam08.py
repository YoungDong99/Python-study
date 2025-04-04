'''
문8) 다음과 같이 단 수를 인수로 넘겨서 해당 구구단을 장식하여 함수 장식자를 정의하시오.


<출력 예시>
*** 2단 ***
2 * 1 = 2
2 * 2 = 4
   :
2 * 9 = 18
***********
'''

def gugu_deco(func) :
    def inner(d) :
        print(f'*** {d}단 ***') 
        func(d)
        print('*'*12) 
    return inner

@gugu_deco 
def gugu_dan(num):
    for i in range(1, 10) :
        print('%d * %d = %d'%(num, i, num*i))

gugu_dan(2)
