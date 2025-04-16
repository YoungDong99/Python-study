# class 정의

class TV :
    
    # 생성자 : 객체 생성 시점 1회 호출 특수 메서드 
    def __init__(self):
        # 동적멤버변수 초기화 
        print('~ 생성자 ~ ')
        self.power = False # 전원(off/on) 
        self.channel = 10 # 채널 
        self.volume = 5  # 볼륨    

    
    # 멤버메서드 : 리모콘 기능 
    def changePower(self):
        self.power = not(self.power) 

    def volumeUp(self):
        self.volume += 1
        
    def volumeDown(self):
        self.volume -= 1        
       
    def channelUp(self):
        self.channel += 1 
        
    def channelDown(self):
        self.channel -= 1
                  


tv1 = TV()  # 생성자 -> 객체

dir(tv1) # 객체 = 변수(자료) + 메서드(처리) 
'''
'changePower'
'channel'
'channelDown'
'channelUp'
'power'
'volume'
'volumeDown'
'volumeUp'
'''

tv1.changePower() #  전원 on
tv1.power # True 

# 채널 올리기
for i in range(5) :
    tv1.channelUp()

tv1.channel # 채널 확인 : 15

# 볼륨 올리기
for i in range(5) :
    tv1.volumeUp()

tv1.volume # 볼륨 확인 : 10




