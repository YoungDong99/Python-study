'''
oracle 관련 문제

문제2) 프로그램을 실행하면 아래와 같은 메뉴가 나타납니다. 이때 해당 메뉴 번호를 키보드로 입력하여 
       dept01 테이블을 관리할 수 있도록 db 프로그래밍을 완성하시오.     


    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 : 
'''    

import oracledb

# 레코드 조회 함수
def select() :
    print('select')
    try :
        conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                                user='c##scott',
                                password='tiger')
        cursor = conn.cursor()
        query = "select * from dept01"
        cursor.execute(query)    
        dataset = cursor.fetchall()
        
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

# 레코드 추가
def insert() :
    print('insert')
    try :
        conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                                user='c##scott',
                                password='tiger')
        cursor = conn.cursor()
        
        deptno = int(input('새 부서번호 입력 : '))
        dname = input('새 부서명 입력 : ')
        loc = input('새 부서위치 입력 : ')
        
        query = f"insert into dept01 values({deptno}, '{dname}', '{loc}')"
        cursor.execute(query)
        conn.commit()
    except Exception as e :
        print('db error :', e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()

# 레코드 수정
def update() :
    print('update')
    try :
        conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                                user='c##scott',
                                password='tiger')
        cursor = conn.cursor()
        
        deptno = int(input('수정할 부서번호 입력 : '))
        dname = input('수정할 부서명 입력 : ')
        loc = input('수정할 부서위치 입력 : ')
        
        query1 = f"select * from dept01 where deptno = {deptno}"
        cursor.execute(query1)
        
        row = cursor.fetchone()
        if row :
            query2 = f"""update dept01 
                    set dname = '{dname}', loc = '{loc}'
                    where deptno = {deptno}"""
            cursor.execute(query2)
            conn.commit()
        else :
            print('해당 부서번호가 없습니다.')
    except Exception as e :
        print('db error :', e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()

# 레코드 삭제
def delete() :
    print('delete')
    try :
        conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                                user='c##scott',
                                password='tiger')
        cursor = conn.cursor()
        
        deptno = int(input('삭제할 부서번호 입력 : '))
        
        query1 = f"select * from dept01 where deptno = {deptno}"
        cursor.execute(query1)
        
        row = cursor.fetchone()
        if row :
            query2 = f"delete from dept01 where deptno = {deptno}"
            cursor.execute(query2)
            conn.commit()
        else :
            print('해당 부서번호가 없습니다.')
    except Exception as e :
        print('db error :', e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()


try:
    # db 연결 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger')
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    while True :  # 무한루프 
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')    
        menu = int(input('\t메뉴번호 입력 : '))
        
        if menu == 1 :
            select()
        elif menu == 2:
            insert()
        elif menu == 3:
            update()
        elif menu == 4:
            delete()
        elif menu == 5 :
            print('프로그램 종료')
            break # 반복 exit
        else :
            print('해당 메뉴는 없습니다.')
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close() 
