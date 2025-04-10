'''
문2) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 


문장 내용 
['programming is fun', 'very fun!', 'have a good time', 
 'mouse is input device', 'keyboard is input device', 'computer'] 
문장 수 :  6 

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 
 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 
 'is', 'input', 'device', 'computer']
단어 수 :  22
'''

 
import os  # 파일 경로 변경, 폴더 생성, 삭제 등

# 파일 읽기 
os.chdir(r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data')
file = open("etest.txt", mode = 'r')

texts = file.readlines() # 줄단위 읽기 

print(texts) # list 반환 
'''
['programming is fun\n', 'very fun!\n', 'have a good time\n', 
 'mouse is input device\n', 'keyboard is input device\n', 
 'computer is input output system'] 
'''
sents = [sent.strip() for sent in texts ]

print('문장 내용\n', sents)
print('문장 수 : ', len(sents))

print()

words = [ word for sent in sents for word in sent.split() ]  # sep 생략 : ' ', '\n'

print('단어 내용\n', words)
print('단어 수 : ', len(words))

















