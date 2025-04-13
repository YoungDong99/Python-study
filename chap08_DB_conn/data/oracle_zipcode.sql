CREATE TABLE zipcode_tab(
zipcode char(14) not null, -- 우편번호 
city varchar(15) not null, -- 시/도 
gu varchar(20) not null,  -- 구 
dong varchar(150) not null, -- 동 
detail varchar(50) -- 상세주소    
);