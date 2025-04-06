"""
문4) json 형식을 갖는 labels.json 파일을 읽어와서 다음과 같이 처리하시오.
    단계1> json file 읽기 & json 디코딩
    단계2> 'url'키를 이용하여 url자료 추출한다.(url'키가 없는 경우를 대비하여 예외처리)  
"""

import json

path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'



# [단계1] json file 읽기 
file = open(path + "/labels.json", mode='r', encoding='utf-8') # 1. file 객체 

# json 문자열
json_str = file.readlines() # 2. file 읽기 : list 반환 

file.close() # 3. file 닫기 

'''
result = [] 
for row in lines :
    result.append(json.loads(row)) 
'''

# python객체(dict) : json 디코딩 
labels = [json.loads(row) for row in json_str] # list 내포 


print(labels)

# [단계2] url 자료 추출 
'''
urls = [] # url 저장 
for row in labels :
    if 'url' in row :
        urls.append(row['url'])
'''

# 리스트 내포로 표현
urls = [ row['url'] for row in labels if 'url' in row]

print(urls)



