'''
for 관련 문제

문2) 여러 줄의 문자열(multiline)에서 공백을 기준으로 단어(token)을 추출하고, 단어 개수를 출력하시오.
   
   <출력 결과>    
   안녕
   Python
   세계로
   오신걸
   환영
   합니다.
   파이션은
   비단뱀
   처럼
   매력적인
   언어
   입니다.
   
   단어 개수 : 12
'''

multiline="""안녕 Python 세계로 오신걸
환영 합니다.
파이션은 비단뱀 처럼 매력적인 언어 입니다."""

count = 0  # 단어 갯수 저장 -> 또는 words 리스트에 저장후 길이를 세어도 됨

for sent in multiline.split('\n') :
    for word in sent.split(' ') :
        count += 1

print('단어 개수 :', count)

