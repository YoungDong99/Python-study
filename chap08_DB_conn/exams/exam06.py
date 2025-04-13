"""    
mariaDB 관련 문제
    
문제6) 서브쿼리(subquery)를 이용하여 특정 사원이름(ename)을 키보드로 입력받아서
     해당 사원의 부서정보(dept) 출력하시오.
     만약 해당 사원이 없는 경우 '해당 사원 없음'이라는 메시지를 출력한다.
     
     사용 테이블 : emp_test, dept_test 
       
   <출력 결과 예시>
  사원 이름 입력 : 유관순
  10 영업부 뉴욕시   
    
  사원 이름 입력 : 테스트
  해당 사원 없음
"""

import pymysql # driver 

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
    
    name = input('사원 이름 입력 : ')
    
    query1 = f"select * from emp_test where ename = '{name}'"
    cursor.execute(query1)
    row = cursor.fetchone()
    
    if row :
        dno = row[6]
        query2 = f"select * from dept_test where dno = {dno}"
        cursor.execute(query2)
        dept = cursor.fetchone()
        print(dept[0], dept[1], dept[2])
    else :
        print('해당 사원 없음x')
  
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()