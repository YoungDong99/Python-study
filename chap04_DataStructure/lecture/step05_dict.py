"""
step05_dict.py

dict 특징 
 - 순서 없는 자료구조(set과 공통점) 
 - key와 value 한쌍(set과 차이점) 
 형식) {key1:value1, key2:value2, ...}
 - key 중복 불가  
 - key 이용 : 값(value) 조회, 수정 
 객체[key] : dict 객체 
 객체[색인] : list or tuple 객체  
"""

# 1. dict 생성 
person = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(person) 
print(len(person), type(person)) # 3 <class 'dict'>


# 2. key 이용 : 수정, 삭제, 추가, 검색 
person['name'] # '홍길동' : 검색 
person['age'] = 45 # 수정 
del person['addr'] # 삭제 
person['pay'] = 350 # 추가 

print(person) # {'name': '홍길동', 'age': 45, 'pay': 350}

# 3. for + dict
for key in person.keys() : # key 넘김 : key in person
    print(key, end = ' ') # key
    print(person[key]) # value
    
for value in person.values() :  # value 넘김 
    print(value) # value

# 한 변수 사용 
for item in person.items() : # key+value
    print(item) # (key, value) : 튜플로 넘김

# 두 변수 사용     
for key, value in person.items() : # key+value
    print(key, value)

  
    
# key 검색 
print('age' in person) # True    
print('addr' in person) # False

if 'age' in person :
    print('age 키 있음')
else :
    print('age 키 없음')


# 4. 단어 빈도수 
charset = ['pay', 'name', 'pay', 'name', 'age'] # 단어집 : list 
charset

# 방법1) key 검색 이용 
wc = {} # 빈set -> {'pay' : 2, 'name': 2, 'age' : 1}

for ch in charset :
    print(ch)
    if ch not in wc : # 사전에 key 없음 
        wc[ch] = 1 # key 없음 : {'pay' : 1, 'name' : 1}
    else :
        wc[ch] += 1 # key 있음 
        
print(wc) # {'pay': 2, 'name': 2, 'age': 1}


# 방법2) dict.get() 메서드 이용 
wc = {} # 빈 set or dict 

dir(wc) # get 

#wc.get(key, 기본값)
help(wc.get)
# Return the value for key if key is in the dictionary, else default.

'''
wc.get('kim', 0) + 1 # 0+1 =1 : 집합에 key 없는 경우(기본값 반환) 
wc.get('kim', 0) + 1 # 10+1=11 : 집합에 key 있음 경우(값 반환)
'''

for ch in charset :
    wc[ch] = wc.get(ch, 0) + 1
    
print(wc) # {'pay': 2, 'name': 2, 'age': 1}
    


# 5. {key : [value1, value2]}
# 예) {'사번' : [급여, 수당]}
emp = {'1001' : [250, 50], '1002' : [200, 40], '1003': [300, 80]}

for eno, price in emp.items() : # 'key:value'
    print('사번 : ', eno, end = ' -> ')
    print(f'급여 : {price[0]},  수당 : {price[1]}')
    


# key 이용 : 급여 + 보너스 
pay = {'홍길동' : 200, '이순신':250, '유관순' : 200} # dict1
bonus = {'홍길동' : 50, '이순신':80, '유관순' : 30} # dict2

# list 내포 
tot_price = [pay[name] + bonus[name] for name in pay.keys()] # 형식1) 
print(tot_price) # [250, 330, 230]

print('전체 급여 합계 =', sum(tot_price)) # 전체 급여 합계 = 810
print('전체 급여 평균 =', sum(tot_price) / len(tot_price)) # 전체 급여 평균 = 270.0


