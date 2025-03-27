
'''
문3) 3개의 단어를 키보드로 입력 받아서 각 단어의 첫자를 추출하여 단어의 약자를 출력하시오.
  조건1) 각 단어 저장 변수 : word1, word2, word3 
  조건2) 입력과 출력 구분선 : * 연산자 이용 
  조건3) 약자 저장 변수 : abbr
  조건4) 원래 단어 저장 변수 : origin_words  
  조건5) 뒤집힌 단어 저장 변수 : reversed_words
   
   <<화면출력 결과>>  
 첫번째 단어 입력 : korea 
 두번째 단어 입력 : baseball
 세번째 단어 입력 : orag
 =========================
 약자 : KBO
 원래 단어 : Korea Baseball Orag
 뒤집힌 단어 : garO llabesaB aeroK
'''

word1 = input('첫번째 단어 입력 : ')
word2 = input('두번째 단어 입력 : ')
word3 = input('세번째 단어 입력 : ')

abbr = word1[0] + word2[0] + word3[0]
origin_words = word1.capitalize() +' '+ word2.capitalize() +' '+ word3.capitalize()
reversed_words = origin_words[::-1]

print('약자 : ', abbr.upper())
print('원래 단어 : ', origin_words)
print('뒤집한 단어 : ', reversed_words)
