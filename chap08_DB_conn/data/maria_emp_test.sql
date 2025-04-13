DROP TABLE emp_test; -- 테이블 삭제 

-- table 만들기 
CREATE TABLE emp_test(
eno int auto_increment primary KEY, -- 자동번호생성기  
ename varchar(20) not null,
hiredate date not null,
sal int not null,
bonus int default 0,
job varchar(20) not null,
dno int);

-- 자동번호생성기 시작번호 변경 
ALTER TABLE emp_test AUTO_INCREMENT = 2024001;

-- 시작번호 확인 
SHOW TABLE STATUS WHERE NAME = 'emp_test';

-- 레코드 추가 
INSERT INTO emp_test VALUES(null, '홍길동','2008-10-20',300, 35,'관리자',10);
INSERT INTO emp_test VALUES(null,'강호동', '2010-10-20', 250, 0,'사원', 20);
INSERT INTO emp_test VALUES(null,'유관순', '2008-03-20', 200, 0,'사원', 10);
INSERT INTO emp_test VALUES(null,'강감찬', '2007-01-20', 450, 100,'관리자', 20);

-- 레코드 조회 
SELECT * FROM emp_test;

COMMIT; -- DB 반영 
