'''
for 관련 문제

문1) 사원의 정보를 저장한 emp 변수를 대상으로 사원의 이름만 추출하여 names에 저장하시오.

       <출력결과>
       이름 = ['홍길동', '이순신', '강호동']
'''

emp = ['1001,홍길동,사원','1002,이순신,대표','1001,강호동,관리자']
names = []


for e in emp :
    name = e.split(sep=',')
    names.append(name[1])


print('이름 = ', names)

