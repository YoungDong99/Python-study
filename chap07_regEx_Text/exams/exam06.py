"""
문6) obama.txt(오바바 연설문) 파일을 읽어와서 텍스트를 전처리한 후 다음과 같이 출력하시오.
  
  <출력 예시>  
전체 단어수 = 4,882개
최고 출현 단어 :  the
top10 word = ['the', 'and', 'of', 'to', 'our', 'that', 'a', 'you', 'we', 'applause']

단어 빈도수
the : 206
and : 195
of : 152
to : 140
our : 109
that : 91
a : 83
you : 82
we : 81
applause : 75
"""

from re import sub

# 텍스트 전처리 함수
def clean_text(texts) : # list input
    # 단계1 : 소문자 변경
    texts_re = [st.lower() for st in texts] # list -> string 추출 


    # 단계2 : 특정 문자나 기호들을 제거     
    texts_re2 = [sub(r'[^\w\d\s]', '', st) for st in texts_re]
    

    #단계3 : 숫자 제거 : 변수 = [실행문(method/func) for 변수 in 열거형객체]
    texts_re3 = [sub('[0-9]', '', st) for st in texts_re2]    
   
    
    # 단계4 : 공백(white space) 제거
    texts_re4 = [sub(r'\s+', ' ', st) for st in texts_re3]

    return texts_re4



# 1.파일 읽기 : obama.txt(카페 다운로드)
path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'
rfile = open(path + '/obama.txt', mode = 'r') 


# 2. 줄단위 전체 읽기 
texts = rfile.readlines()


# 3.줄 단위 텍스트 전처리         
text_re = clean_text(texts)


# 4. 단어 카운트 : 전체 단어수 & 최고 단어 
# list 내포 이중 for문 : [실행문 for1  for2]
words = [word for sent in texts_re for word in sent.split()]
len(words) # 4882


# 단어 카운트 
wc = {}
for word in words :
    wc[word] = wc.get(word, 0) + 1


wc_sorted = sorted(wc, key=wc.get, reverse=True)


# 5. Top10 단어 & 단어 빈도수 
 
top10 = wc_sorted[:10]
print('top10 : ', top10)

print("========================================")

print('~~ 가장 많이 나온 단어 TOP10 ~~')
for word in top10:
    print(word, wc[word], sep=' : ')


print("========================================")

# 6. plus + 불용어 제외하기

# nltk 라이브러리
import nltk
from collections import Counter
from nltk.corpus import stopwords

# NLTK 불용어 리스트 다운로드
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# 하나의 문자열로 합친 후 단어 분리
words = " ".join(text_re).split()
filtered_words = [ word for word in words if word not in stop_words ]  # 불용어 제거

wc = Counter(filtered_words)

top_10_words = wc.most_common(10)
print("~~ 가장 많이 나온 단어 10개 (불용어 제외) ~~")
for word, count in top_10_words:
    print(f"{word}: {count}")

