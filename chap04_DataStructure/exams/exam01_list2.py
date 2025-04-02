'''
문2) 키보드로 5명의 학생 성적을 입력받아서 리스트에 저장하고,
     5명 학생의 성적의 평균을 구하고, 80점 이상 성적을 받은
     학생의 숫자를 계산하여 출력하시오.
     <조건> 평균 = 총점 / 인원수  

<출력 예시>
성적을 입력하시요: 50
성적을 입력하시요: 85
성적을 입력하시요: 60
성적을 입력하시요: 55
성적을 입력하시요: 82
성적의 평균은 66.4 입니다.
80점 이상 성적을 받은 학생은 2 명입니다.
'''

scores = []

for i in range(5) :
    print('성적을 입력하시요: ', end='')
    scores.append(int(input()))
    
sum_score = 0
num_score = 0

for i in scores :
    sum_score += i
    if i >= 80:
        num_score += 1

print('성적의 평균은 {} 입니다.'.format(sum_score/5))
print('80점 이상 성적을 받은 학생은 {} 명입니다.'.format(num_score))
    
