'''
pickle 파일 
 - 파이썬 객체(list, dict)를 이진파일(binary)로 저장
 - 파이썬 객체(딕셔너리, 리스트, 클래스 등)를 바이너리 형식으로 저장하고 불러오는 모듈
 - 문자열(JSON) 변환 없이 그대로 저장할 수 있지만, 파이썬에서만 사용 가능
 - 속도가 빠르고 복잡한 객체도 저장할 수 있지만, 보안에 취약 -> 신뢰할수 없는 데이터 로드 주의
'''

# 1. file read 
path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data' 

file = open(path + '/ktext.txt', mode = 'r', encoding='utf-8')
text = file.readlines() 
file.close()

print(text)


# 2. word 추출
'''
words = []
for line in text : # list
    for word in line.split() : 
        words.append(word)
'''
words = [ word for line in text for word in line.split() ]

print(words)
print(type(words))  # <class 'list'>


'''
python 객체(list, dict 등) 텍스트 파일에 저장 불가
file = open(path + '/words.txt', mode='w')
file.write(words)
'''

# 3. pickle save & load 

import pickle 
'''
dump(객체, 파일) : 피클 파일 저장
load(파일) : 피클 파일 읽기
'''


# binary file save
file = open(path + '/wc_data.pickle', mode='wb')  # 'wb' = write binary
pickle.dump(words, file) 
file.close()


# load
file = open(path+'/wc_data.pickle', mode='rb') # 'rb' = read binary
wc_data = pickle.load(file) # load(file)

print(type(wc_data)) # <class 'list'>
print(wc_data)
file.close()










