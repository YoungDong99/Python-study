"""
step04_zipcode_table.py

작업 목적 : text file -> DB table로 저장

 <작업순서>
1. table 생성 : sql developer에서 작업 (oracle_zipcode.sql 참고)   
2. zipcode.txt -> 서울 지역 추출 -> 레코드 추가    
3. 레코드 조회(동 or 구 검색)
"""

'''
query = """CREATE TABLE zipcode_tab(
zipcode char(14) not null,
city varchar(15) not null,
gu varchar(20) not null,
dong varchar(150) not null,
detail varchar(50) 
)"""

cursor.execute(query)  # 실제 table 생성 & auto commit
'''

import oracledb

path=r'C:/ITWILL/2_Python/workspace/chap08_DB_conn/data'


try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger') 
    
    # sql문 실행 객체 
    cursor = conn.cursor() 
    
    # 1. 레코드 조회 
    cursor.execute("select * from zipcode_tab")
    datasest = cursor.fetchall() # 검색 레코드 가져오기 
    
    # 2. 레코드 추가 or 레코드 조회 	
    if not(datasest) : # 레코드 없음
        #print('1) 레코드 추가')
        file = open(path + '/zipcode.txt', mode='r', encoding='utf-8')
        line = file.readline()
        
        while line :
            token = line.split('\t')
            if token[1] == '서울' :
                zipcode = str(token[0])
                city = token[1]
                gu = token[2]
                dong = token[3]
                detail = token[4]
            
                query = f"""INSERT INTO zipcode_tab
                            VALUES('{zipcode}', '{city}', '{gu}', '{dong}', '{detail}')"""
                
                cursor.execute(query)
                conn.commit()
                
            line = file.readline()
            
        file.close()
        print('레코드 삽입 성공!!')
            
            
    else : 
        #print('2) 레코드 조회')
        choice = int(input('1. 동 검색, 2. 구 검색 : '))
        if choice == 1 :
            dong = input('검색 동 입력 : ')
            
            query = f"SELECT * FROM zipcode_tab WHERE dong LIKE '{dong}%'"
            cursor.execute(query)
            dataset = cursor.fetchall()
            
            if dataset :
                for row in dataset :
                    print(row[0], row[1], row[2], row[3], row[4])
                print('검색 동 수 : ', len(dataset))
            else :
                print('잘못 입력했거나 해당 동이 없습니다.')
            
        elif choice == 2 :
            gu = input('검색 구 입력 : ')
            
            query = f"SELECT * FROM zipcode_tab WHERE gu LIKE '{gu}%'"
            cursor.execute(query)
            dataset = cursor.fetchall()
            
            if dataset :
                for row in dataset :
                    print(row[0], row[1], row[2], row[3], row[4])
                print('검색 구 수 : ', len(dataset))
            else :
                print('잘못 입력했거나 해당 구가 없습니다.')
            
        else :
            print('올바른 번호를 입력하세요')
                

except Exception as e :
    print('db error : ', e)
    conn.rollback() 
finally :
    cursor.close()
    conn.close()
    
    
    
    
    
    
    