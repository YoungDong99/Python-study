'''
step05 

문) tot 함수를 인수로 받아서 dataset 각 원소의 합을 계산하는 함수를 완성하시오.

  <출력 결과>
  tot = [12.5, 7, 22.3]
'''

# tot 함수 정의 
def tot(x):
    return sum(x)

# tot 함수를 인수로 받는 함수 정의 
def my_func(func, datas):
    '''
    result = []
    for i in range(len(datas)) :
        result.append(func(datas[i]))
    '''
    for i in datas :
        print(i)
        
    #result = [ tot(data) for data in datas ]  # 외부 함수 호출
    result = [ func(data) for data in datas ]  # 자체 함수 호출 (더 효율적)
    return result

# dataset
dataset = [[2,4.5,6], [3,4], [5,8.3,9]]


print('tot =', my_func(tot, dataset))


