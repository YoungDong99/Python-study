"""
문3) 아래 코드를 실행하면 22번 줄에서 오류(AttributeError)가 발생되고 프로그램이 중단됩니다.
    이유는 패턴과 일치된 <h> 태그를 찾으면 group() 메서드에 의해서 <h> 태그의 내용이 반환되지만  
    패턴과 일치된 <h> 태그를 찾지 못하면 반환된 문자열이 없으므로 오류가 발생합니다. 
    이 코드에 예외처리를 적용하여 <h> 태그 안에 내용이 있는 태그들은 모두 tags에 저장하시오.     
    
    <조건> search() 함수 이용

   <출력결과> 
 tags :  ['<h1>주 제목 내용</h1>', '<h2>부제목 내용</h2>']
"""

import re
 
texts = ["<span><h1>주 제목 내용</h1></span>", "<h1></h1>", "<p><h2>부제목 내용</h2></p>"]

tags = []

for tag in texts :
    try :
        search_text = re.search("<h.>.+</h.>", tag)
        search_text.group() # AttributeError: 'NoneType' object has no attribute 'group'
        tags.append(search_text.group())
    except Exception as e :
        print('예외발생 : ', e)

print('tags : ',tags)

