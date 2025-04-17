'''
 문2) 동적 멤버변수를 이용하여 도서(Book) 클래스를 정의하고, 도서 객체 2개를 생성하시오.
      
      <조건1> 생성자를 이용하여 도서 제목, 저자, 페이지수를 동적 멤버변수로 만든다.  
      <조건2> display_info 메서드에서 도서 정보(제목, 저자, 페이지 수)를 출력한다. 
      
      
<< 출력결과 예시>> 

<도서 객체1> 
제목 : 파이썬기초
저자 : 홍길동
페이지 수 : 300

<도서 객체2>
제목 : 파이썬분석
저자 : 존스미스
페이지 수 : 350 
'''


# 도서 클래스 정의 
class Book:
    def __init__(self, title, author, pages) :
        self.title = title
        self.author = author
        self.pages = pages
        
    def display_info(self):
        print('제목 : ', self.title)
        print('제목 : ', self.author)
        print('제목 : ', self.pages)
    
##############################################    
    
# 도서1 객체 
book1 = Book('파이썬기초', '홍길동', 300)
book1.display_info()

# 도서2 객체 
book2 = Book('파이썬분석', '존스미스', 350) 
book2.display_info()
