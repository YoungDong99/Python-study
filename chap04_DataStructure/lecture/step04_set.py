"""
step04_set.py

set 특징 
 - 순서 없는 자료구조(색인 사용 불가)
 - 중복 허용 불가 
  형식) 변수 = {값1, 값2,...}
"""

# 1. set 생성 
st = {1, 3, 5, 1, 5} # 중복 허용 불가 
print(st, len(st)) # {1, 3, 5} 3

# for + set
for s in st :
    print(s, end = ' ') # 1 3 5
    
    
# 2. 중복 불가 
gender = ['남','여','남','여'] # list(중복 허용)
gender

# list -> set 형변환 
sgender = set(gender)
print(sgender) # {'남', '여'}

# set -> list 형변환 
lgender = list(sgender)
print(lgender) # ['여', '남']


# 집합관련 
set1 = {1, 3, 4, 5, 7} # 집합1
set2 = {3, 5} # 집합2

dir(set1) # set의 메서드 확인 

# 집합관련 메서드 
set1.union(set2) #  합집합 : {1, 3, 4, 5, 7}
set1.difference(set2) # 차집합 : {1, 4, 7}
set1.intersection(set2) # 교집합 : {3, 5}

# 집합관련 연산자(|, -, &)
set1 | set2 #  합집합 : {1, 3, 4, 5, 7}
set1 - set2 # 차집합 : {1, 4, 7}
set1 & set2 # 교집합 : {3, 5} 


# 원소 추가 
set2.add(7)
print(set2) # {3, 5, 7}

# 원소 삭제 
set2.discard(7) 
print(set2) # {3, 5}

# 단어집과 불용어 
text = "This is a book"

words = text.split(sep=' ')
words # ['This', 'is', 'a', 'book']

# list -> set 
swords = set(words)
swords # {'This', 'a', 'book', 'is'}

# 불용어 집합
del_words = {'a', 'the', 'and', 'but'}

result = swords.difference(del_words) # 불용어 제거 
print(result) # {'is', 'This', 'book'}


