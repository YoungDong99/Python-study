'''
json 파일
 - 네트워크상에서 표준으로 사용되는 텍스트 파일
 - 활용 : 서로 다른 플랫폼에서 파일 공유

json 모듈 기능 
 1. encoding : Python객체 -> json file 저장
 2. decoding : json file 읽기 -> Python객체   
'''

import json # json 모듈

dir(json)
'''
dump : json file write (배열 타입(대괄호))
dumps : json file write (객체 타입(중괄호))
load : json file read (배열 타입(대괄호))
loads : json file read (객체 타입(중괄호))
scanner : 
'''
path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'

##########################
### 1. json encoding
##########################

# 순서 : [ python 객체 -> json 문자열 ] -> json file  >>  [] : json 인코딩
# 형식) json.dumps(python 객체)

# 1) python객체 : dict, list 등
user = { 'eno': 1234,  'ename': '홍길동', 'job':'관리자'} 
type(user) # dict

# 2) json 인코딩 : json 문자열  
json_encoding = json.dumps(user, ensure_ascii=False)
# ensure_ascii=False : ASCII 인코딩 안함
print(json_encoding)  #  {"eno": 1234, "ename": "홍길동", "job": "관리자"}
type(json_encoding)  # str
## 파이썬에서 만든 객체가 json 문자열로 바뀌었다


# 3) json file 저장  
file = open(path + "/json_data.txt", mode='w', encoding='utf-8')  # 1. file 객체  # 확장자 json으로 해도 무방함

#file.write(user) ## 에러발생 : TypeError: write() argument must be str, not dict
# python 객체(dict, list) : 텍스트 파일 저장 시 오류 -> pickle 타입으로 해결가능
      
file.write(json_encoding)  # 2. file 쓰기
file.close()  # 3. file 객체 닫기



##########################
### 2. json decoding 
##########################

'''
  json file -> [ json 문자열 -> python 객체 ]
  형식) json.loads(json 문자열)
'''


# 1) json file 읽기
file = open(path + "/json_data.txt", mode='r', encoding='utf-8')  # 1. file 객체
dir(file)

# 2) json 문자열 
json_data = file.readline()
file.close()  # 3. file 닫기

print(json_data)  # {"eno": 1234, "ename": "홍길동", "job": "관리자"}
type(json_data)  # str


# 3) json 디코딩 : json 문자열 -> python 객체(dict)
python_dict = json.loads(json_data)

# python dict 
print(python_dict)  # {'eno': 1234, 'ename': '홍길동', 'job': '관리자'}
print(type(python_dict))  # <class 'dict'>




#############################
### 3. json file 읽기
#############################

# 1) json file 읽기  
file = open(path + "/usagov_bitly.json", mode='r', encoding='utf-8')

# 2) json 문자열
lines = file.readlines()
file.close() # fille 닫기 

print(lines)
print(len(lines))
type(lines[0])  # str : json 문자열

# 3) json 디코딩 : json 문자열  -> python 객체  
result = []  # python 객체 저장

for line in lines :
    result.append(json.loads(line)) # json.loads(json문자열 -> python 객체) 

print(result)
print(len(result))  # 3560 : [{1}, {2}, {3}, ..., {3560}] : [python객체]
type(result[0])  # dict : python객체 


'''
url 추출 : "u" : "http://~"
'''

urls = []

for row in result : # list 
    if 'u' in row : # dict 
        urls.append(row['u']) # key -> value 추출(url)

    
print(urls)
print(len(urls))


