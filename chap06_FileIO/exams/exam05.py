"""
문5) 아래 코드는 labels.json 파일의 자료를 읽어와서 labels의 리스트에 저장된 상태이다. 
    이때 labels의 리스트 객체를 pickle 파일로 저장한 후 읽어와서 파일의 내용을 출력하시오.
    
    조건> path 경로에 'labels.pickle' 파일명으로 저장
"""

import json


path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'


# json file read : json 문자열 
file = open(path + "/labels.json", mode='r', encoding='utf-8') # file객체 생성 

lines = file.readlines()

file.close() # fille 닫기 


# labels 리스트에 저장 
labels = [json.loads(line) for line in lines]

print(labels)
type(labels) # list


    
import pickle 

# [단계1] pickle file save
file = open(path + '/labels.pickle', mode='wb')

pickle.dump(labels, file) #(obj, file)

file.close()

# [단계2] pickle file load
file = open(path + '/labels.pickle', mode='rb')

file_load = pickle.load(file) #(obj, file)
print(file_load) # labels 객체와 동일함 

file.close()











