"""
step03_CRUD.py

  - CRUD : Create, Read, Update, Delete
  
  준비 : dept -> dept01 생성
"""

import oracledb

try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger') 
    dir(conn)
    '''
    conn.commit() : db 반영
    conn.rollback() : dml 명령의 작업취소
    '''
    
    # sql문 실행 객체 
    cursor = conn.cursor()
    
    
    # 4. 레코드 삭제 : Delete(부서번호 -> 해당 부서 삭제)
    deptno = int(input('삭제할 부서번호 입력 : '))
    
    query1 = f"select * from dept01 where deptno = {deptno}"
    cursor.execute(query1)
    
    row = cursor.fetchone() # 1개 레코드 : 문자열
    if row :
        # 부서정보 삭제
        query2 = f"delete from dept01 where deptno = {deptno}"
        cursor.execute(query2)
        conn.commit()
    else :
        # 부서번호 없음
        print('해당 부서번호가 없습니다.')
        
    
    # 3. 레코드 수정 : Update (부서번호 -> 부서명 또는 부서위치)
    '''
    deptno = int(input('수정할 부서번호 입력 : '))
    dname = input('수정할 부서명 입력 : ')
    loc = input('수정할 부서위치 입력 : ')
    
    query1 = f"select * from dept01 where deptno = {deptno}"
    cursor.execute(query1)
    
    row = cursor.fetchone() # 1개 레코드 : 문자열
    if row :
        # 부서번호 있음
        query2 = f"""update dept01 
                set dname = '{dname}', loc = '{loc}'
                where deptno = {deptno}"""
        cursor.execute(query2)
        conn.commit()
    else :
        # 부서번호 없음
        print('해당 부서번호가 없습니다.')
    '''
    
    
    # 2. 레코드 삽입 : Create(Insert)
    '''
    deptno = int(input('새 부서번호 입력 : '))
    dname = input('새 부서명 입력 : ')
    loc = input('새 부서위치 입력 : ')
    
    query = f"insert into dept01 values({deptno}, '{dname}', '{loc}')"
    cursor.execute(query)  # 실제 레코드 삽입
    conn.commit()  # db 반영
    '''
    
    
    # 1. 레코드 조회    
    query = "select * from dept01" # 부서테이블  
    cursor.execute(query)    
    dataset = cursor.fetchall() # 전체 레코드 
    '''
    rows = cursor.fetchall() : 여러 개 레코드 가져오기 (다중행 레코드)
    row = cursor.fetchone() : 1개(기본키) 레코드 가져오기(단일행 레코)
    '''
    
    print('-'*40)
    print('code\t name\t\t\t  loc')
    print('-'*40)
    for row in dataset :
        print("{0:^4}\t{1:<12}\t{2:<5}".format(row[0],row[1],row[2]))
        
    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))        

except Exception as e :
    print('db error :', e)
    conn.rollback()
finally :
    cursor.close()
    conn.close()

