"""
list & for 문제
"""

# 3) 문자열 리스트에서 길이가 5 이하인 단어만 추출하고 출력하시오.

words = ["apple", "banana", "grape", "orange", "kiwi", "pear"]

short_words = [d for d in words if len(d) <= 5]

print(short_words) # 출력결과 : ['apple', 'grape', 'kiwi', 'pear']


# 4) 주어진 원소에서 양수는 남기고, 음수는 0으로 바꾸시오.
numbers = [10, -5, 20, -15, 30, -25]

positive_numbers = [0 if d < 0 else d for d in numbers]

print(positive_numbers) # 출력결과 : [10, 0, 20, 0, 30, 0]


# 5) 주어진 text에서 모음('aeiou')을 제거하고, 자음만으로 문자열을 만드시오.
text = "Hello, how are you today?"

consonants_only = [s for s in text if s not in 'aeiou']

filtered_text = ''.join(consonants_only)

print(filtered_text) # 출력결과 : Hll, hw r y tdy?

