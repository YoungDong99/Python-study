'''
텍스트 파일 입출력(file input/output)
 - 데이터 입출력 시(file, db) 예외 처리한다.
 형식) open('파일경로/파일명', mode='r'/'w'/'a')
        mode = 'r' : 파일 읽기
        mode = 'w' : 파일 쓰기
        mode = 'a' : 파일 쓰기 + 추가
'''


# 파일 경로 
path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'

# 1. 파일 읽기 
file = open(path + "/etest.txt", mode = 'r')
dir(file)
'''
read() : 전체 내용 읽기  
readline() : 한 줄 읽기  
readlines() : 모든 줄 리스트로 반환  
write() : 문자열 쓰기(한 줄)
writelines() : 여러 줄 쓰기  
seek() : 파일 위치 이동  
tell() : 현재 위치 확인  
flush() : 버퍼 비우기  
close() : 객체 닫기  
'''


print(file.read()) # 파일 객체 이용 : 전체 읽기
file.close() # 객체 닫기



# 2. 파일 쓰기(자동 생성) 
ftest2 = open(path + '/ftest3.txt', mode = 'w')  # 1. 파일 객체
ftest2.write('my first write ~~~~~') # 2. 파일 쓰기 
ftest2.close()  # 3. 객체 닫기



# 3. 파일 쓰기(추가 - 기존 내용 끝에 추가) 
ftest3 = open(path + '/ftest3.txt', mode = 'a')  # 1. 파일 객체
ftest3.write('\nmy second text ~~!!!')  # 2. 추가 문장
ftest3.close()  # 객체 닫기


# 4. 다양한 읽기 모드
file = open(path + '/etest.txt')  # mode = 'r' (생략시 기본값)
dir(file)
'''
read() : 모든 내용을 한 번에 읽기(문자열 반환)
readline() : 한 줄씩 읽기(문자열 반환)
readlines() : 모든 내용을 줄 단위 읽기(리스트 반환)
'''

## read() : 모든 내용을 한 번에 읽기(문자열 반환)
full_text = file.read()
print(full_text, type(full_text)) # <class 'str'>


## readline : 한 줄씩 읽기(문자열 반환)
row = file.readline()
print(row, type(row))  #  <class 'str'>


## readline + 반복문(while)
while True : 
    row = file.readline()
    
    if row :  # 문장 있음
        print(row.strip())
    else :   # EoF (문장없음)
        break


## readlines : 모든 내용을 줄 단위 읽기
rows = file.readlines()

print(rows)
'''
['programming is fun\n', 'very fun!\n', 'have a good time\n', 
 'mouse is input device\n', 'keyboard is input device\n', 
 'computer is input output system']
'''


print(type(rows))  # <class 'list'>

file.close()

# 문장 단위 출력
for now in rows :
    print(now.strip())  # '\n' 제외 
    


# 5. with 키워드 이용
with open(path + '/etest.txt') as file :
    # 파일 객체 이용, 자동 close
    print(file.read())


# 자동으로 파일 닫힘
print(file.read())


























