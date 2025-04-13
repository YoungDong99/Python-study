"""
mariaDB 관련 문제

문제5) HidiSQL을 이용하여 다음과 같은 단계로 student 테이블을 만들고, 
      DB연동 프로그램으로 student 테이블의 유무를 판단하여 존재하는 경우 
      레코드를 추가하고, 전체 레코드를 조회하시오.
  
단계1> HidiSQL 이용 : student 테이블 만들기(maria_student.sql 파일 참고) 


단계2> DB 연동 프로그램 작성 : 테이블이 있으면 레코드 3개 추가   
insert into student values (9411,'서진수','055)381-2158',201,1001);
insert into student values (9413,'이미경','02)266-8947',103,3002);
insert into student values (9415,'박동호','031)740-6388',202,4003);

단계3> DB 연동 프로그램 작성 : 레코드가 있으면 레코드 조회(select)   
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
    
    # 1. table 유무 판단 : student 
    cursor.execute("show tables")
    tables = cursor.fetchall()
    
    flag = False
    
    for table in tables :
        if 'student' in table :
            flag = True
    
    # 2. 레코드 추가 및 레코드 조회 
    if flag :
        query = "insert into student values (%s, %s, %s, %s, %s)"
        data = [
            (9411, '서진수', '055)381-2158', 201, 1001),
            (9413, '이미경', '02)266-8947', 103, 3002),
            (9415, '박동호', '031)740-6388', 202, 4003)
        ]
        cursor.executemany(query, data)
        conn.commit()
        print('레코드 삽입 완료~!')
        
    else :
        print('테이블이 존재하지 않습니다.')
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
    
    
    
    
    
    