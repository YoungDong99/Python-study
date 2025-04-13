"""
step05_join_subquery.py

1. HidiSQL SQL 파일 불러오기 & 테이블 생성 실습
  ->  maria_dept_test.sql 파일 선택 > dept_test 테이블 생성 
  ->  maria_emp_test.sql 파일 선택 > emp_test 테이블 생성 
  
2. join & subquery : emp_test vs dept_test 
  -> 표준(ANSI)  JOIN 
  -> subquery : 부서정보(10번) -> 사원정보 조회 
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
    
    # 1-1. ANSI inner join 
    sql = """SELECT e.eno, e.ename, e.sal, d.dno
             FROM emp_test e INNER JOIN dept_test d # 내부조인 
             ON e.dno = d.dno  # 조인조건 : 4개
                 AND e.sal >= 250 """ # 추가조건 : 3개(1개 제외)
                 
    cursor.execute(sql)
    dataset = cursor.fetchall()
    
    # 레코드 조회 
    print('\nANSI inner join')
    for row in dataset :
        print(row[0], row[1], row[2], row[3])   
    
    # 1-2. ANSI LEFT | RIGHT outer join : 사원이 없는 부서 추가 
    sql = """SELECT e.eno, e.ename, e.sal, d.dno
             FROM emp_test e RIGHT OUTER JOIN dept_test d # 내부조인 
             ON e.dno = d.dno """
             
    cursor.execute(sql)
    dataset = cursor.fetchall()
    
    # 레코드 조회 
    print('\nANSI outer join')
    for row in dataset :
        print(row[0], row[1], row[2], row[3])    
    
    # 2. subquery : 부서정보(10번) -> 사원정보 조회
    dno = int(input('부서번호 입력 : ')) # 10, 20
    sql= f"""SELECT *
             FROM emp_test 
             WHERE dno = (SELECT dno FROM dept_test
                          WHERE dno = {dno}) """
    cursor.execute(sql)
    dataset = cursor.fetchall()
    
    # 레코드 조회 
    print('\nSubquery')
    for row in dataset :
        print(row[0], row[1], row[2], row[3]) 
        
    print('전체 레코드 수 :', len(dataset))
    
        
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
