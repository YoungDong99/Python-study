"""
step01_mariaDB_test.py


 - mariaDB 연동 테스트 
 - goods 테이블 없는 경우 : 
   HidiSQL에서 goods 테이블 작성 및 레코드 추가(maria_goods.sql 참고) 
"""


# db 연결 함수  
def connect(**config) : # ** : dict 가변인수 
    print(config) # {'user': 'scott', 'pwd': 'tiger'}


# 환경변수 
config = {'user': 'scott', 'pwd' : 'tiger'} # dict 

# db 연결 함수 호출 
connect(config) # 주소 호출 : TypeError 

connect(**config) # 값 호출  

import pymysql # driver = python + mariaDB 

# 환경변수 
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True} # dict 

try :
    # 1. db 연동 객체 생성 
    conn = pymysql.connect(**config) # dict 원소 : 실인수 
    
    # 2. sql문 실행 객체 생성
    cursor = conn.cursor()
    
    # 3. sql문 실행 
    query = "select * from goods"
    cursor.execute(query)
    
    dataset = cursor.fetchall()
    
    for row in dataset :
        print(row[0], row[1], row[2], row[3])   
    
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()


