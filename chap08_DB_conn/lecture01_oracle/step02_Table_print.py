"""
step02_Table_print.py

 - db 테이블 조회 및 양식 출력 
"""

import oracledb

try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger') 
    # sql문 실행 객체 
    cursor = conn.cursor()    
        
    # 1. 레코드 조회    
    query = "select * from dept" # 부서테이블  
    cursor.execute(query)        # sql문 실행
    dataset = cursor.fetchall()  # 전체 조회 레코드 반환
    print(dataset)  # list
    
    # 2. 레코드 양식 출력 
    print('-'*40)
    print('code\t name\t\t\t  loc')
    print('-'*40)
    for row in dataset :
        # {색인:양식}
        #print(row)  # 레코드 : tuple
        print("{0:^4}\t{1:<12}\t{2:>8}".format(row[0],row[1],row[2]))
        
    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))
    
    '''
    ^ : 가운데 정렬
    < : 왼쪽 정렬(문자열)
    > : 오른쪽 정렬(숫자)
    주의 : 칼럼 값의 최대길이보다 같거나 크게 지정
    '''

except Exception as e :
    print('db error :', e)        
finally :
    # db 연동 객체 & cursor 객체 닫기 : 역순 닫기
    cursor.close()
    conn.close()

