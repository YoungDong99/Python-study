'''
우편번호 찾기 - 52,144개
[우편번호]tab[도/시]tab[구]tab[동]tab[세부주소] 
[135-807]  서울  강남구  개포1동 우성3차아파트  (1∼6동)
[135-807]  서울  강남구  개포1동 우성3차아파트 
'''

# 파일 경로 
path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'


# 우편번호 파일 읽기
file = open(path + '/zipcode.txt', mode = 'r', encoding='utf-8')  
'''
mode : 읽기 or 쓰기 
encoding : 인코딩 방식
'''

line = file.readline() # 첫줄 읽기
print(line)

print(type(line))


token = line.split(sep='\t')
print(token)

print(token[3]) 


dong = input('검색할 동 입력하세요 : ')

cnt = 0  # 카운터 변수
while line :  # line != null : 반복
    token = line.split(sep='\t')  # tab
    
    if token[3].startswith(dong) :  # 접두어 비교
        cnt += 1
        print(line)
    
    line = file.readline()  # 2번째줄 ~ 마지막줄

print(cnt)
file.close()



    