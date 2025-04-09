# 정규표현식 관련 모듈 
import re # re.sub(), re.search(), re.compile()


### 3. re.sub(pattern, rep, string) 
# - 문자열(string)에서 패턴과 일치하는 문자를 찾아서 다른 문자 교체 

st1 = 'test^홍길동 abc 대한*민국 123$tbc'

text = re.sub('[\\^*$]', '', st1)  ## 슬래쉬 2개 : SyntaxWarning 제거
print(text) 
'''
역슬래쉬(\) 역할
  메타문자 -> 특수문자 : ^ -> r'\^'
  일반문자 -> 메타문자 : d -> r'\d', w -> r'\w', s -> r'\s'
'''

# test홍길동 abc 대한민국 123tbc



### 4. re.search(pattern, string)
# - 문자열(string)에서 패턴과 일치하는 문자열 검색  

# 예) 특정 태그(tag)안에 포함된 문자 반복 여부로 패턴 지정 
tag = "<span> <head>안녕하세요.</head> </span>"

head_tag = re.search("<head>.*</head>", tag)  # .* : 0번
head_tag.group() # '<head>안녕하세요.</head>'

head_tag = re.search("<head>.+</head>", tag)
head_tag.group() # '<head>안녕하세요.</head>'

head_tag = re.search("<head>.?</head>", tag)
head_tag.group() # AttributeError:

'''
re.match() vs re.search()
  re.match() : 문자열 시작부터 패턴 비교 (문자열 유효성 검증)
  re.search() : 문자열 전체 대상 패턴 비교 (부분 문자열 찾기)
'''


### 5. re.compile(pattern) 
# - 패턴을 객체로 생성하고, 정규표현식 메서드로 문자열 처리  

urls = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~']


# url 패턴 객체 생성 
url_pat = re.compile('^http://news')  # 패턴 객체

dir(url_pat)
'''
url_pat.findall(string) -> findall('패턴', string)
url_pat.match(string) = match('패턴', string)
url_pat.search(string) = search('패턴', string)
''' 


# url 패턴 반복 사용 
urls_result = [] # 정상 url 저장 

for url in urls :
    if url_pat.findall(url) : # 패턴객체.findall(url) = findall('패턴', url) 
        urls_result.append(url)
        
        
print(urls_result) # ['http://news.com/test', 'http://news.com/test2']

# 1) url_pat.findall(string)
urls_result = [url  for url in urls if url_pat.findall(url) ]

print(urls_result)        
        
# 2) url_pat.match(string)        
urls_result = [url  for url in urls if url_pat.match(url) ]

print(urls_result)  
        
# 2) url_pat.search(string)        
urls_result = [url  for url in urls if url_pat.search(url) ]

print(urls_result)       

