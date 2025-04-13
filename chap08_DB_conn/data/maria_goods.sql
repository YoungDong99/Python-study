DROP TABLE goods; -- 테이블 삭제 


-- 테이블 작성 
CREATE TABLE goods(
 code int PRIMARY KEY,
 name varchar(20) not null,
 su int not null,
 dan int not null
);


-- 레코드 추가
INSERT INTO goods values(1,'냉장고', 2, 850000);
INSERT INTO goods values(2,'세탁기', 3, 550000);
INSERT INTO goods values(3,'HDTV', 2, 1500000);


-- 레코드 조회 
SELECT * FROM goods;


COMMIT; -- DB 반영

 
