'''
함수 장식자 
  - 다른 함수의 시작과 종료부분에 장식을 추가하는 기능 

함수장식자 적용 예
@함수장식자
def 함수명() :
    실행문
'''

# 함수 장식자 
def hello_deco(func) :  
    def inner() : 
        print('*'*20)
        func()
        print('*'*20)
    return inner
    

# 대상 함수에 함수 장식자 적용  
@hello_deco
def hello() :
    print('my name is 홍길동')


# 함수 호출 
hello()

'''
동작 방식
1. hello() 는 hello_deco(hello) 가 된다.
2. 즉 hello 함수가 inner 함수로 변경
3. -> 따라서 hello()를 실행하면 실제로 inner() 함수 실행
4. inner에서 func() 는 hello() 이므로 원래 함수 실행 > my name is 홍길동 출력

※ hello_deco(hello) 는 inner 함수를 반환(return) -> 즉 hello는 inner가 된다.
'''

#####################
## 함수장식자 응용 예
#####################
'''
함수 호출 전 : 로그인(인증)
함수 호출 : 인증 성공 시 웹 페이지 오픈
함수 호출 후 : 로그아웃(인증 정보 말소)
'''

# 로그인 인증 처리
def login(uid, upwd) :
    # id = 'hong', pwd = '1234'
    if uid == 'hong' and upwd == '1234' :   # db 역할
        return True # 인증 성공
    else :
        return False # 인증 실패

# 함수장식자 : 중첩함수

def auth(user) :  # 외부함수(함수명)
    def info(uid, upwd) :  # 내부함수(인수)
        # 로그인 인증 처리
        result = login(uid, upwd)
        
        if result :
            print('환영합니다!!')
            user(uid, upwd)  # 함수 호출 : 웹 페이지 open
            print('~~ 로그아웃 ~~')
        else :
            print('로그인 실패')
    return info


# 사용자1 함수
@auth
def user1(uid, upwd) :
    print(f'*** {uid} 사용자 웹 페이지 오픈')

@auth
# 사용자2 함수
def user2(uid, upwd) :
    print(f'*** {uid} 사용자 웹 페이지 오픈')


# 사용자 호출
user1('hong', '1234')  # 로그인 성공


user2('hong', '4567')  # 로그인 실패



















