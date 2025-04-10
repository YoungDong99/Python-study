'''
문5) 다음 texts의 텍스트를 대상으로 단계별로 텍스트를 전처리하는 함수를 완성하고, 전처리 전 텍스트를 인수로 
    함수를 호출하여 텍스트 전처리 결과를 확인하시오.(아래 출력 예시는 전처리 전과 후 비교) 
    
    <조건> sub() 함수 이용

<텍스트 전처리 전> 
[' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

<텍스트 전처리 후> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''


import re # re.sub


# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


print('<텍스트 전처리 전>')
print(texts)

def clean_text(texts) :  
    pass

    # 1. 소문자 변경 
    texts_re = [st.lower() for st in texts]
    
    # 2. 숫자 제거 
    texts_re = [re.sub('[0-9]', '', st) for st in texts_re]
    
    # 3. 문장부호 & 특수문자 제거 
    texts_re = [re.sub(r'[^\w\d\s]', '', st) for st in texts_re]
    
    # 4. 영문자 제거 
    texts_re = [re.sub(r'[a-z]', '', st) for st in texts_re]
    
    # 5. 공백 제거(2칸 이상 공백 -> 1칸 공백)
    texts_re = [re.sub(r'\s+', ' ', st) for st in texts_re]
    
    # 6. 문장 처음 공백 제거
    texts_re = [re.sub(r'^\s', '', st) for st in texts_re]
    
    return texts_re
    
print('<텍스트 전처리 후>')
print(clean_text(texts))

