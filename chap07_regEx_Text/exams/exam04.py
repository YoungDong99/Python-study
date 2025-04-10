"""
문4) 웹문서 파일(test.htm)를 대상으로 <li> 내용 </li> 형식을 갖는 태그만 추출하여 다음과 같이 출력하시오.
     정상 태그는 <li> 태그안에 1개 이상 문자가 포함된 태그들이 저장되고, 예외 태그는 그 외에 나머지 
     태그들을 저장합니다.
     
     <조건> search() 함수 이용
  
     <출력 예시>  
 정상 태그 : ['<li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>', '<li> nav : 네이게이션(메뉴) </li>', '<li> section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그</li>', '<li> aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) </li>', '<li> footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) </li>']
 예외 태그 : ['<!DOCTYPE html>', '<html>', '<head>', '<meta charset="UTF-8">', '<title> html5 - 시멘틱 태그 </title>', '</head>', '<body>', '<h1> 시멘틱 태그 ?</h1>', '<p> html5에서 웹문서에 의미를 부여하는 태그를 의미 </p>', '<h2> 주요 시멘틱 태그 </h2>', '<ul>', '</ul>', '</body>', '</html>', '', '']
"""

import re  

path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data'

# file 읽기 
file = open(path + "/test.html", mode = 'r', encoding='utf-8') # 웹문서 읽기 
lines = file.readlines() #  줄 단위 전체 읽기 - list 반환    

### 내용 채우기   ###
right_tags = [] # 정상 태그 저장 
wrong_tags = [] # 예외 태그 저장     

'''
for line in lines :
    tag = re.search(r"<li>(.*?)</li>", line)
    if tag :
        right_tags.append(line.strip())
    else :
        wrong_tags.append(line)
'''

for tag in lines :
    try :
        result = re.search('<li>.+</li>', tag)
        right_tags.append(result.group())
    except :
        print('예외발생!')
        wrong_tags.append(tag)


print('정상 태그 : ', right_tags)
print('예외 태그 : ', wrong_tags)

