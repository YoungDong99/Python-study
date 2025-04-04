'''
문7) 중첩함수 응용 : 아래와 같이 outer와 inner 함수의 역할에 맞게 두 개의 내부함수(innder)를 
     완성하시오.

 1.outer 함수 역할 : 3명 학생의 점수(scores) 저장, inner 함수 포함 
 2.inner 함수 역할 : 
   tot_df 함수 : 각 학생의 점수(3개 과목)를 이용하여 촘점을 계산한 후 총점을 반환한다.
   avg_df 함수 : 각 학생의 총점과 과목수를 인수로 받아서 평균을 계산하고 결과를 출력한다.
     
 <출력 결과> 
  평균 = [70.0, 85.0, 79.0]
'''


def scores_pro(scores) : # outer 
    
    # 총점 계산 : inner
    def tot_df() :
        sums = [ sum(score) for score in scores ]
        return sums
        
    # 평균 계산 : inner
    def avg_df(tots, cnt) :
        avgs = [ sum(score)/len(score) for score in scores]
        return avgs
    
    return tot_df, avg_df # 내부함수 반환 


# 실인수로 사용할 3명의 학생 성적(과목수 3개) 
scores = [[60,80,70], [80,85,90], [70,82,85]]


# 외부함수 호출  
tot_df, avg_df = scores_pro(scores) # 내부함수 반환  

# 내부함수 호출
t = tot_df()
print(t)

a = avg_df(t, 3)

print('평균 = ', a)








