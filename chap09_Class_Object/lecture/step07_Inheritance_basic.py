'''
클래스 상속( Inheritance )
 - 기존 클래스(부모)를 이용하여 새로운 클래스(자식) 작성 기법 
 - 목적 : 클래스 설계 시 가이드라인을 제시하는 역할
 - 상속 대상 : 부모클래스 멤버(멤버변수+멤버메서드)   
 - 생성자 상속 대상 아님 : 자식에서 부모 생성자 호출(자식 생성자 생략)
 
 형식)
 class 자식클래스(부모클래스) :
     클래스 본체
'''
     

# 동물 클래스 : 부모(멤버 : name, speak()) 
class Animal:
    # 생성자 : 이름 
    def __init__(self, name):
        self.name = name # 멤버변수 

    # 멤버메서드 : 원형 메서드 
    def speak(self):
        pass # 명령문(x)

# 강아지 : 자식1
class Dog(Animal): # name, speak()           
    def speak(self): # 메서드 재정의(override) : 원형 메서드 내용 추가 
        print(f"{self.name}가 짖습니다.")

# 고양이 : 자식2
class Cat(Animal):
    def speak(self): # 메서드 재정의 : 원형 메서드 내용 추가 
        print(f"{self.name}가 야옹합니다.")

# 강아지 : 자식1
dog = Dog("강아지")  # 생성자 
dir(dog)
'''
'name'
'speak'
'''
dog.name # '강아지'
dog.speak() # 강아지가 짖습니다.

# 고양이 : 자식2
cat = Cat("고양이")
dir(dog)
'''
'name'
'speak'
'''
cat.name # '고양이'
cat.speak() # 고양이가 야옹합니다.





