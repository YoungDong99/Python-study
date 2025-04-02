'''
문3) 리스트(list)에 추가할 원소의 개수를 키보드로 입력 받은 후, 입력 받은 수 만큼
     임의의 숫자를 리스트에 추가한다. 이후 찾을 값을 키보드로 입력받은 후  
     리스트에 해당 값이 있으면 "YES", 없으면 "NO"를 출력하시오. 
          
<출력 예시1>
list 개수 : 5
1
2
3
4
5
찾을 값 : 3  
YES

<출력 예시2>
list 개수 : 3
1
2
4
찾을 값 : 3 
NO
'''


size = int(input('list 개수 : ')) # list 크기 입력
    
nums = [] # 숫자 저장 : 빈list 

for i in range(size) :
    nums.append(int(input()))


if int(input('찾을 값 : ')) in nums :
    print('YES')
els : print('NO')
    

# for 문으로 찾기
find = int(input('찾을 값 : '))

for i in nums :
    if i == find:
        print('YES')
        break
    if i == nums[-1] :
        print('NO')
    
