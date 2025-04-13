"""
step03_emp_table.py

1. 테이블 유무 판단
   -> 테이블 없으면 '테이블 없음' 메시지 출력 
   -> 테이블 있으면 레코드 조회

2. 테이블 없는 경우 : HidiSQL에서 emp_test 테이블 작성 후 레코드 추가(maria_emp_test.sql 참고)
"""

import pymysql 

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
    conn = pymysql.connect(**config)
    # sql문 실행 객체 
    cursor = conn.cursor()    
    
    # 1. table 유무 판단 : emp_test 
    cursor.execute("show tables") # table 목록 조회 
    tables = cursor.fetchall() # table 목록 가져오기 
    
    print(tables)  # (('goods',), ('zipcode_tab',))  중첩tuple 반환
    
    
    
    # emp 테이블 조회 : 스위칭 (Switching) 기법  
    sw = False # 초기값 
    
    for table in tables : 
        if 'emp_test' in table : 
            sw = True  


    # 2. 레코드 조회/추가 or table 생성         
    if sw : # table 있는 경우 
        print('테이블 있음 ^_^')       
        
        # 테이블 레코드 조회
        query = "select * from emp_test"
        cursor.execute(query)  
        dataset = cursor.fetchall()
        
        for row in dataset :
            print(row)

    else : # table 없는 경우                 
        print('emp 테이블 없음 ㅠㅠ')            
    
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()    
    
   
    
    
    
    
    
    
    
    



