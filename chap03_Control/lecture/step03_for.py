'''
반복문(for)

형식) 
for  변수 in 반복가능객체(iterable) :
    실행문
    실행문
    
반복가능객체(iterable) : 문자열, 리스트, range(n)
'''


# 1. 문자열 객체
string = "나는 홍길동 입니다."

# 문자 -> 변수 넘김
for s in string :
    print(s, end = '')  # end : 한 줄에 나오도록
print()


# 2. list 객체 
lst = [1, 2, 3, 4, 5]  
for i in lst :
    print('원소 : ', i)
    

# 3. range 객체 : 순서 있는 정수 생성   
num1 = range(10)  
print('num1 : ', num1)  # range(0, 10) 
list(num1) # list(range(10))
'''
range() 함수는 파이썬에서 연속된 정수를 생성하고, list()는 그 결과를 리스트로 변환
'''

for n in num1 :
    print('n=',n)


num2 = range(1, 11)
print('num2 : ', num2)  # range(1, 11)

'''
range(stop) : 0 ~ stop-1
range(start, stop) : start ~ stop-1
'''

# 4. list + range 객체    
num2 = range(1, 5)  
print('num2 : ', num2)  

num2 = list(num2) # list형 변환 
print(num2)  # [1, 2, 3, 4]

  

# 5. 중첩 반복문
'''
for i in 열거형객체 :
   for j in 열거형객체 :
      실행문
'''

# 구구단 출력 : range() 함수 이용
for i in range(2, 10):    
    print('~~~ {}단 ~~~'.format(i))
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i * j))
        
        

texts = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = []
words = []

for sent in texts.split(sep='\n') :
    print('sent : ', sent)
    sents.append(sent)
    for word in sent.split(sep=' ') :
        print('word : ', word)
        words.append(word)

print(sents)  # 문장 저장 리스트
print(words)  # 단어 저장 리스트
print('단어의 길이 : ', len(words))

        
        