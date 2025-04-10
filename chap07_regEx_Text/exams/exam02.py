'''
문2) 사용자별 이메일 주소(emails)를 대상으로 정규표현식을 적용하여 email 양식이 올바른 
     2명의 email 주소를 추출하시오. 이메일 주소의 형식과 올바른 email 양식의 주소를 판단하는
     정규표현식은 다음과 같다. 
     
     <조건> match() 함수 이용
     
     
     email형식) 아이디@호스트이름.최상위도메인           
     
     email 양식 조건  
      아이디 : 첫자는 영문소문자(^[a-z]), 단어길이 3자 이상(\w{3,})
      호스트이름 : 영문소문자 시작([a-z]), 단어길이 2자 이상(\w{2,})
      최상위 도메인 : 영문소문자 3자리 이하([a-z]{3})
     
     힌트) email 양식 정규표현식 : '^[a-z]\w{3,}@[a-z]\w{2,}.[a-z]{3}'
     
      
    
  << 올바른 email 출력 결과 >>
  right_emails = ['you2@naver.com', 'kimjs@gmail.com']
'''

import re

# 사용자 이메일 주소 
emails =  ['hong@12.com', 'you2@naver.com', '12kang@hanmail.net', 'kimjs@gmail.com']


# 올바른 이메일 저장 
'''
right_emails = [] 

for email in emails :
    if re.match(r'^[a-z]\w{3,}@[a-z]\w{2,}.[a-z]{3}', email) :
        right_emails.append(email)
## if문에서 None 은 false 로 동작, Match 객체는 true처럼 동작함
'''

## 리스트 내포
right_emails = [ e for e in emails if re.match(r'^[a-z]\w{3,}@[a-z]\w{2,}.[a-z]{3}', e) ]

print('right_emails = ', right_emails)


