'''
oracle 관련 문제 

문제1) emp01 테이블의 조회 결과를 다음과 같은 양식(format)으로 출력하시오.  
      <조건1> empno : 숫자 5자리 오른쪽 기준, ename, job : 왼쪽 기준, sal : 천단위 콤마
      <조건2> 기타 양식은 <출력결과> 참고 
      
 
          <출력결과>     
---------------------------------
empno   ename   job	       sal
---------------------------------
 7369  SMITH   CLERK         800
 7499  ALLEN   SALESMAN    1,600
 7521  WARD    SALESMAN    1,250
 7566  JONES   MANAGER     2,975
 7654  MARTIN  SALESMAN    1,250
 7698  BLAKE   MANAGER     2,850
 7782  CLARK   MANAGER     2,450
 7788  SCOTT   ANALYST     3,000
 7839  KING    PRESIDENT   5,000
 7844  TURNER  SALESMAN    1,500
 7876  ADAMS   CLERK       1,100
 7900  JAMES   CLERK         950
 7902  FORD    ANALYST     3,000
 7934  MILLER  CLERK       1,300
---------------------------------
전체 레코드 수 : 14
---------------------------------
'''

import oracledb

try :
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger') 
    cursor = conn.cursor()
    
    query = "select empno, ename, job, sal from emp01"
    cursor.execute(query)
    
    dataset = cursor.fetchall()
    
    print('-'*40)
    print('empno\t ename\t\t job\t\t   sal  ')
    print('-'*40)
    
    for row in dataset :
        #print("{0:^5}\t {1:<7}\t {2:<10}\t {3:>5}".format(row[0], row[1], row[2], row[3]))
        print(f"{row[0]:^5}\t {row[1]:<7}\t {row[2]:<10}\t {row[3]:5,}")
    
    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))
    print('-'*40)
    
except Exception as e :
    print('db error : ', e)

finally:
    cursor.close()
    conn.close()

