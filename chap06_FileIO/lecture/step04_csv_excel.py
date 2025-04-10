'''
csv, excel file read
 - 칼럼 단위로 작성된 excel 파일 유형 읽기
'''

import pandas as pd  # csv, excel 읽기

dir(pd)

'''
'read_csv', : csv file 읽기 
'read_excel', : excel file 읽기 
''' 

##########################
### 1. csv file 
##########################

# 1) file 읽기 및 내용 보기  
path = r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data' 
bmi = pd.read_csv(path + '/bmi.csv', encoding='utf-8')

dir(bmi)
'''
info() : 객체 정보 제공
head() : 제목과 앞부분 5개 
tail() : 제목과 뒷부분 5개 
'''

print(bmi.info())
'''
<class 'pandas.core.frame.DataFrame'> : 행열구조 자료(DataFrame) 
RangeIndex: 20000 entries, 0 to 19999 : 행 개수 
Data columns (total 3 columns): 열 개수 
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   height  20000 non-null  int64  : 정수형 
 1   weight  20000 non-null  int64  : 정수형 
 2   label   20000 non-null  object : 문자형 
'''

print(bmi.head(10))
print(bmi.tail())
    
# 2) 칼럼 단위 추출 : 객체.칼럼명
height = bmi.height # 키
weight = bmi.weight # 몸무게
label = bmi.label # bmi 레이블(normal, thin, fat)


# 3) 칼럼 단위 연산 
print('height mean : ', sum(height) / len(height)) # height mean :  164.9379
print('weight mean : ', sum(weight) / len(weight)) # weight mean :  62.40995 

print('max height:', max(height)) # max height: 190
print('max weight:', max(weight)) # max weight: 85

# 유일값, 빈도분석 
dir(label)
label.unique() # ['thin', 'normal', 'fat']
label.value_counts()
'''
normal    7677
fat       7425
thin      4898
'''

# 4) 조건 검색 : 조건으로 행 선택(비교, 논리연산자 사용) 
bmi[(bmi.height >= 180)] # 비교연산자 
bmi[(bmi.weight >= 50) & (bmi.weight <= 70)] # 논리연산자 and 
bmi[(bmi.label=='thin') | (bmi.label=='fat')] # 논리연산 or
bmi[~(bmi.label=='normal')] # 논리연산 not


##########################
### 2. excel file 
##########################

# 1) file 읽기 및 내용보기 
ex = pd.ExcelFile(path + '/sam_kospi.xlsx')
kospi = ex.parse('sam_kospi')
print(kospi)

dir(kospi)
'''
info()
head()
tail()
'''

# 칼럼 정보 
print(kospi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 247 entries, 0 to 246
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   Date    247 non-null    datetime64[ns]
 1   Open    247 non-null    int64         
 2   High    247 non-null    int64         
 3   Low     247 non-null    int64         
 4   Close   247 non-null    int64         
 5   Volume  247 non-null    int64 
'''

kospi.info()
kospi.head()
# 2) 컬럼 추출 
high = kospi.High
low = kospi.Low


# 3) 칼럼 단위 통계  
print('High mean :', high.mean())
print('Low mean :', low.mean())

# 파생변수
diff = high - low

# 칼럼 추가 
kospi['diff'] = diff

kospi.head()


# 4) csv 파일 저장 
kospi.to_csv(path + '/kospi_df.csv', index=None)
# index=None : 행 이름 제외 






