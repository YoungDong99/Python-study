"""
텍스트 전처리 : 특수문자, 불용어 처리 
"""

import re # re 모듈 가져오기 

# 전처리 텍스트  
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,  A124&***$?']


# 텍스트 전처리 함수 정의 
def clean_text(texts) : # list input

    # 단계1 : 소문자 변경
    texts_re = [st.lower() for st in texts] # list -> string 추출 
    print('texts_re :', texts_re)

    # 단계2 : 문장부호 & 특수문자 제거     
    texts_re2 = [re.sub(r'[^\w\d\s]', '', st) for st in texts_re]
    print('texts_re2 :', texts_re2)

    #단계3 : 숫자 제거 : 변수 = [실행문(method/func) for 변수 in 열거형객체]
    texts_re3 = [re.sub('[0-9]', '', st) for st in texts_re2]    
    print('texts_re3 :', texts_re3)
    
    # 단계4 : 공백(white space) 제거
    texts_re4 = [re.sub(r'\s+', ' ', st) for st in texts_re3]
    print('texts_re4 :', texts_re4)
          
    return texts_re4


print('텍스트 전처리 전')
print(texts)
# ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,  A124&***$?']

print('텍스트 전처리 후')
result_texts = clean_text(texts)
print(result_texts)
# ['afabasabag', 'abtta a', 'uysfsfa a']


