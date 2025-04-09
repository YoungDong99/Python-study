"""
단어 카운트(word count) 작업절차 
 1. 텍스트 파일 읽기
 2. 텍스트 전처리
 3. 단어 카운트
 4. TopN 단어 선정
"""

import re 

# 텍스트 전처리 함수 정의 
def clean_text(texts) : # list input

    # 단계1 : 소문자 변경
    texts_re = [st.lower() for st in texts] # list -> string 추출 


    # 단계2 : 문장부호 & 특수문자 제거     
    texts_re2 = [re.sub(r'[^\w\d\s]', '', st) for st in texts_re]
    

    #단계3 : 숫자 제거 : 변수 = [실행문(method/func) for 변수 in 열거형객체]
    texts_re3 = [re.sub('[0-9]', '', st) for st in texts_re2]    
   
    
    # 단계4 : 공백(white space) 제거
    texts_re4 = [re.sub(r'\s+', ' ', st) for st in texts_re3]

    return texts_re4


# 1. 텍스트 파일 읽기 
path = r'C:/ITWILL/2_Python/workspace/chap06_FileIO/data/'
file = open(path + '/ktext.txt', mode = 'r', encoding='utf-8') 

texts = file.readlines() # 전체 줄 단위 -> list 반환 
file.close()

# 2. 텍스트 전처리 
new_texts = clean_text(texts)    
print(new_texts)
'''
['우리나라 대한민국 우리나라 만세 ', '비아그라 gram 정력 최고 ', '나는 대한민국 사람 ', '보험료 원에 평생 보장 마감 임박 ', '나는 홍길동']
'''

# 3 단어 카운트(word count)
words = [] # 단어 저장 
wc = {} # 단어 출현빈도 

## 1) 단어 추춸 & 저장
words = [ word for st in new_texts for word in st.split() ]  # 문단 -> 문장 -> 단어어
print(words)
len(words)

## 2) 단어 출현빈도수
for word in words :
    wc[word] = wc.get(word, 0) + 1 

print(wc) 

# 4. TopN 단어 출력  

print('최다 출현 단어 :', max(wc, key = wc.get))

## 최다 출현 단어 여러 개일 경우
max_value = max(wc.values())  # 최댓값
max_keys = [ k for k, v in wc.items() if v == max_value ]  # value가 최댓값인 key 리스트

print('최다 출현 단어들 :', max_keys)

# Top5 단어 선정
wc_sorted = sorted(wc, key=wc.get, reverse=True)  # 단어 출현수로 내림차순 정렬
print(wc_sorted)

top5 = wc_sorted[:5]
print(top5)

'''
단어 -> 출현빈도
'''
for word in top5 : 
    print(word, wc[word], sep='->')

