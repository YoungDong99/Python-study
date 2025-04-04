"""
모듈(module) 
  - 파이썬에서 제공되는 파일(*.py)
  - 경로 : ~\anaconda3\Lib0
  - 함수와 클래스 제공 

모듈 함수  
 - 파이썬 제공 함수 
 
모듈 유형
 1. built-in 모듈 : 내장함수 제공
 2. import 모듈 : 외장ㅎ마수 제공
"""

#import builtins

help(sum)
# Help on built-in function sum in module builtins:


# 1. built-in 모듈 : 내장함수 
dataset = list(range(1,6))
print(dataset)  # [1, 2, 3, 4, 5]

# built-in 모듈 제공 내장함수  
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))
print('len=', len(dataset))
#mean(datatset)


# 2. import 모듈 : 외장함수 


# from 모듈 import 함수1, 함수2, 함수3, .... 방법1)
from statistics import mean, median, stdev, pstdev, quantiles  # 평균, 중위수, 표준편차  
from statistics import * # 모든 함수 사용 

# import 모듈 ... 방법2) 
import statistics

statistics.mean(dataset) # 3

# 모듈에서 제공하는 함수 or 클래스 확인
dir(statistics)

'''
mean: 평균
median: 중위수
median_low: 중위값이 두 개일 때 작은 값 반환
median_high: 중위값이 두 개일 때 큰 값 반환
mode: 최빈값 (가장 많이 등장하는 값)
multimode: 여러 개의 최빈값 반환 (리스트 형태)
pstdev: 모집단의 표준 편차
pvariance: 모집단의 분산
stdev: 표본의 표준 편차
variance: 표본의 분산
harmonic_mean: 조화평균
geometric_mean: 기하평균 (버전 3.8부터 지원)
quantiles(data, n): 데이터의 분위수 (n등분)
'''



print('평균 :', mean(dataset)) # 평균 : 3
print('중위수 : ', median(dataset)) # 중위수 :  3
print('표준편차 :', stdev(dataset)) # 표준편차 : 1.5811388300841898
print('모표준편차 :', pstdev(dataset)) # 모표준편차 : 1.4142135623730951
print('사분위수 :', quantiles(dataset)) # 사분위수 : [1.5, 3.0, 4.5]






















