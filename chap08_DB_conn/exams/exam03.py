'''
oracle 관련 문제

문제3) 기준 테이블은 교수(professor), 대상 테이블은 학생(student)을 대상으로 
      표준(ANSI) RIGHT OUTER JOIN을 수행하여 학생명(name), 주전공(deptno1), 
      교수명(name), 교수번호(profno)를 조회하여 출력하시오.
      
      공통칼럼 : profno  
      
      
      힌트) FROM 테이블1  RIGHT OUTER JOIN 테이블2 ON 공통칼럼;


  <출력 결과>
****************************
 학생명 전공 교수명 교수번호 
****************************
 서진수 101 조인형 1001
 김신영 101 박승곤 1002
 일지매 101 박승곤 1002
 None None 송도권 1003
 김진욱 102 양선희 2001
 서재수 102 양선희 2001
 신은경 102 김영조 2002
 None None 주승재 2003
 None None 김도형 3001
 이미경 103 나한열 3002
 None None 김현정 3003)
 김재수 201 심슨 4001
 임세현 201 심슨 4001
 안광훈 201 최슬기 4002
 박동호 202 박원범 4003
 오나라 202 박원범 4003
 김문호 201 박원범 4003
 None None 차범철 4004
 None None 바비 4005
 None None 전민 4006
 노정호 301 허은 4007
 구유미 301 허은 4007
***************************
전체 레코드 수 :  22

'''

import oracledb

try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger')
    # sql문 실행 객체 
    cursor = conn.cursor()
    
    
    # 표준(ANSI) RIGHT OUTER JOIN     
    sql = """SELECT s.name, s.deptno1, p.name, p.profno
             FROM student s RIGHT OUTER JOIN professor p
             ON s.profno = p.profno"""


    cursor.execute(sql)
    dataset = cursor.fetchall()
    
    print('*'*25)
    print('학생명 전공 교수명 교수번호')
    print('*'*25)
    
    # 레코드 조회 
    for row in dataset :
        print(row[0], row[1], row[2], row[3])   
    
    print('*'*25)
    print('전체 레코드 수 : ',len(dataset)) 
       
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close()
    conn.close()
    
