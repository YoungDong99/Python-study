"""
step05_join.py
"""

import oracledb

try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger')
    # sql문 실행 객체 
    cursor = conn.cursor()
    
    # oracle inner join  
    sql = """SELECT e.empno, e.ename, e.sal, e.job, d.deptno
    FROM emp e, dept d
    WHERE e.deptno = d.deptno"""  # 1명 이상 근무하는 부서
    
    # ANSI inner join  
    sql = """SELECT e.empno, e.ename, e.sal, e.job, d.deptno
    FROM emp e INNER JOIN dept d
    ON e.deptno = d.deptno"""    # 1명 이상 근무하는 부서
    
    # oracle outer join  
    sql = """SELECT e.empno, e.ename, e.sal, e.job, d.deptno
    FROM emp e, dept d
    WHERE e.deptno(+) = d.deptno"""  # 부족한 사원테이블에 +, 부서테이블이 기준
    
    # ANSI outer join  
    sql = """SELECT e.empno, e.ename, e.sal, e.job, d.deptno
    FROM emp e RIGHT OUTER JOIN dept d
    ON e.deptno = d.deptno"""    # 부서는 있는데 사원이 없는 경우 포함
    
    cursor.execute(sql)
    dataset = cursor.fetchall()
    
    # 레코드 조회 
    for row in dataset :
        print(row[0], row[1], row[2], row[3], row[4])   
    
    print('조회 레코드 수 :', len(dataset))
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
    
    
    
    
    
    
    
    
    
    
    