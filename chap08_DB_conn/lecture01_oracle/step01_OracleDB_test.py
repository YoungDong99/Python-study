"""
step01_OracleDB_test.py

  준비 : pip install oracledb
 - db 연동 테스트 
"""

import oracledb # driver = python + db

dir(oracledb)
'''
connect(dsn, user, password) : db 연동 객체 생성 메서드  
version : 버전 확인 속성  
'''
oracledb.version # '3.1.0'

try :
    # 1. db 연동 객체 생성 : dsn(DB url : ip주소:포트번호/db명)   
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger')
    dir(conn) # cursor
    
    # 2. sql문 실행 객체 
    cursor = conn.cursor()
    dir(cursor) # execute
    
    # 3. sql문 작성 & 실행 
    query = "select * from emp" # sql문 
    cursor.execute(query) # sql실행 
    
    # 4. 레코드 가져오기 & 출력     
    dataset = cursor.fetchall() # 조회된 전체 레코드 
        
    for row in dataset :
        print(row) # 한 줄(레코드) 출력  
        
    print('\n전체 레코드 : ', len(dataset))           
except Exception as e :
    print('db error : ', e)
finally :
    # 객체 닫기 
    cursor.close()
    conn.close()
    
    