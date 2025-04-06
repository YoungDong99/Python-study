'''
문3) 다음과 같은 조건으로 '서울' 지역에 해당하는 주소를 추출하여 줄 단위로 파일에 저장하시오.
    <조건1> 저장할 경로 : path
    <조건2> 저장할 파일명 : 'seoul_addr.txt' 
'''


path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'

rfile = open(path + "/zipcode.txt", mode='r', encoding='utf-8') # 읽을 파일 
wfile = open(path + "/seoul_addr.txt", mode='w', encoding='utf-8') # 저장할 파일

lines = rfile.readline() # 첫줄 읽기 
print(lines)

while lines :       
    token = lines.split(sep='\t') # 토큰 생성
    
    if token[1].startswith('서울') :
        wfile.write(lines)
        
    lines = rfile.readline()
    
    
wfile.close()
rfile.close()



## 파일 객체의 버퍼를 강제로 비우는 역할
wfile.flush()







