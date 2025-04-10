"""
문1) 아래 urls 리스트를 대상으로 'http://news'로 시작하는 url만 추출하여 final_urls에 저장하시오. 
     
     <조건> findall()함수와 접두어(^) 이용 
         

    <출력결과> 
 final_urls :  ['http://news.com/test', 'http://news.com/test2']
"""


import re 

urls = ['http://news.com/test','now.co.kr', 'new.com','http://news.com/test2', 'http//~']

'''
final_urls = [] # 옳바른 url 저장 

for url in urls :
    result = re.findall('^http://news', url)
    #print(result) # []이면 패턴과 불일치한 url
    if result :
        final_urls.append(url)  # 패턴과 일치한 url 저장
'''      

# findall 사용
final_urls = [data for data in urls if re.findall('^http://news', data) ]

# match 사용
#final_urls = [data for data in urls if re.match('http://news', data) ]


print('final_urls :', final_urls) 



