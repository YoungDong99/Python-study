"""
step04_csv_table.py


 <작업순서>
1. HidiSQL에서 생성한 student 테이블 확인    
2. student.csv 파일 내용으로 레코드 삽입/조회 
"""

import pandas as pd # csv file read 
import pymysql # db 연동 driver  

path = r'C:\ITWILL\2_Python\workspace\chap08_DB_conn\data'

student = pd.read_csv(path + '/student.csv')
student.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   sno     10 non-null     int64 
 1   name    10 non-null     object
 2   tel     10 non-null     object
 3   deptno  10 non-null     int64 
 4   propno  10 non-null     int64 
'''
print(student)

# 각 칼럼 추출 : 형식) DF.칼럼명 
sno = student.sno # 학번 
name = student.name # 학생명 
tel = student.tel # 전화번호 
deptno = student.deptno # 학과 
propno = student.propno # 지도교수 

size = len(sno) # 학생인원 

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

    
try :
    # db 연동 객체 생성 
    conn = pymysql.connect(**config) # 환경변수 
    # sql문 실행 객체 
    cursor = conn.cursor()    
    
    # 1. table 유무 판단 : student
    cursor.execute("show tables") # table 목록 조회 
    tables = cursor.fetchall() # table 목록 가져오기 
    
    sw = False # off
    for table in tables : 
        if 'student' in table : # if 'student' in ('student', )
            sw = True # on
    
    # 2. 레코드 추가 & 조회 
    if sw : # table 있는 경우   
        for i in range(size) :
            query = f"""Insert into student values(
                    {sno[i]},'{name[i]}','{tel[i]}',{deptno[i]},{propno[i]})"""
            cursor.execute(query) # 1행 레코드 삽입 
            
        conn.commit() # db 반영
        print('~ student 테이블에 레코드 삽입 ~ ')
        
    else : # table 없는 경우         
        print('student 테이블이 없습니다.')        
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close()
    conn.close()
    
  