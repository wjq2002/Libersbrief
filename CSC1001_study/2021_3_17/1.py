import math

class Circle(): 
    
    def __init__(self, radius = 1): 
        self.radius = radius
    
    def area(self): 
        return self.radius**2*math.pi
    
    def perimeter(self): 
        return self.radius*2*math.pi
    
    def set(self, radius): 
        self.radius = radius

# 使用预设值调用类        
circle1 = Circle()
print(circle1.radius)
print(circle1.area())

# 给定 self 的 radius 值
circle2 = Circle(2)
print(circle2.radius)
print(circle2.area())

# 使用类的 set 函数修改 radius 值
circle3 = Circle()
circle3.set(10)
print(circle3.radius)
print(circle3.area())

# 直接调用 radius 值进行修改
circle4        = Circle()
circle4.radius = 5
print(circle4.radius)
print(circle4.area())

class ClassName:
    
    def __init__(self):
        self.x = 1
    
    def m1(self):
        self.y = 2
        z = 5
        print('y= ', self.y, 'z= ',z)
        
    def m2(self):
        self.y = 3
        z = self.x + 1
        print('y= ', self.y, 'z= ',z)
        self.m1()

myobj = ClassName()
myobj.m2()