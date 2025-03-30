"""
for 관련 문제

문3) 키보드로 입력받은 문자열 중에서 모음과 자음의 개수를 집계하는 프로그램을 작성하시오.
     모음(홀소리) : aeiou, 자음(닿소리) : 나머지 21개 영문자
     
     <조건> 문자열은 1개 이상의 알파벳으로 구성된다. 
"""


original = input('문자열을 입력하시오: ')
lower_string = original.lower() # 소문자 변경 

vowels = 0  # 모음 문자 카운트
consonants = 0  # 자음 문자 카운트


# 문자열이 1개 이상이면서 알파벳 문자이거나 문장인 경우
if len(lower_string) > 0 and lower_string.isalpha() or " " in lower_string:
    for word in lower_string.split(' ') :
        for ch in word :
            if ch in 'aeiou' :
                vowels += 1
            else :
                consonants += 1
else :
    print('다시 입력하세요.')         		

print('모음 갯수 :', vowels)
print('자음 갯수 :', consonants)

