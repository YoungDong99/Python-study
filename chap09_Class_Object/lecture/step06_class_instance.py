'''
클래스멤버와 인스턴스멤버 
 1. 클래스(class) 멤버 : 클래스로 호출할 수 있는 변수와 메서드
    형식) 클래스명.변수 or 클래스명.클래스메서드() 

 2. 인스턴스(instance) 멤버 : 객체로 호출할 수 있는 변수와 메서드
    형식) 객체.필드 or 객체.메서드()
'''

class MathClass :
    # 클래스 선어부 : 클래스 변수  
    x_class = 100
    y_class = 50
    
    def __init__(self, x, y) :
       # 동적멤버변수 : 인스턴스 변수  
       self.x_ins = x
       self.y_ins = y

    @classmethod # 함수장식자 
    def add(cls) :  # 클래스 메서드(cls)
        return cls.x_class + cls.y_class

    @classmethod
    def subtract(cls) : # 클래스 메서드(cls)
        return cls.x_class - cls.y_class

    def multiply(self) : # 인스턴스 메서드(self) 
        return self.x_ins * self.y_ins

    def divide(self) : # 인스턴스 메서드(self)
        return self.x_ins / self.y_ins
    

# 클래스 멤버 호출 : 클래스명.멤버(클래스를 함수처럼 사용)
dir(MathClass)
'''
'add'      : 클래스 메서드
'divide'   : 인스턴스 메서드(x)
'multiply' : 인스턴스 메서드(x)
'subtract' : 클래스 메서드
'x_class'
'y_class'
'''

MathClass.x_class # 100
MathClass.y_class # 50

MathClass.add() # 150
MathClass.subtract() # 50

# 객체를 이용하여 호출 
MathClass.divide()  # TypeError  
MathClass.multiply() # TypeError

# 2. 인스턴스(instance) 멤버
obj = MathClass(100, 50)

dir(obj) # 객체 : 클래스 멤버 + 인스턴스 멤버 호출 
'''
 'add',     : 클래스 메서드  
 'divide',  : 인스턴스 메서드
 'multiply', : 인스턴스 메서드
 'subtract', : 클래스 메서드 
 'x_class', : 클래스 변수 
 'x_ins',  : 인스턴스 변수 
 'y_class', : 클래스 변수
 'y_ins'    : 인스턴스 변수
''' 

obj.divide() # 2.0 : 객체.인스턴스 메서드()
obj.multiply() # 5000 : 객체.인스턴스 메서드()
obj.add() # 150
obj.subtract() # 50




















