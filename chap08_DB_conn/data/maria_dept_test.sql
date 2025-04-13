DROP TABLE dept_test; -- 테이블 삭제 

CREATE OR REPLACE TABLE dept_test(
dno INT PRIMARY KEY, -- 키본키
dname VARCHAR(50) NOT NULL,
loc VARCHAR(100) NOT NULL
);


-- 레코드 추가 
INSERT INTO dept_test VALUES(10, '영업부', '뉴욕시');
INSERT INTO dept_test VALUES(20, '기획실', '서울시');
INSERT INTO dept_test VALUES(30, '연구실', '대전시');

-- 레코드 조회 
SELECT * FROM dept_test;

COMMIT; -- DB 반영

 
