# import math
# class  shape:
#     def area(self):
#         return 0
#     def perimeter(self):
#        return 0
    
#     # def describe(self):
#     #     return(f'{self.__class__.__name__}:' f'area = {self.area():.2f} P = {self.perimeter():.2f}')
    
# class circle(shape):
#     def __init__(self,r):
#      self.r = r

#     def area(self):
#         return math.pi*self.r**2
    
#     def perimeter(self):
#         return 2 * math.pi * self.r
    
# class rectangle(shape):

#     def __init__(self,w,h):
#      self.w,self.h = w,h

#     def area(self):
#      return self.w*self.h

#     def perimeter(self):
#      return 2 * (self.w + self.h)

# class triangle(shape):
#     def __init__(self,a,b,c):
#      self.a,self.b,self.c = a,b,c

#     def perimeter(self):
#        return self.a + self.b + self.c 
    
#     def area(self):
#        s = self.perimeter()/2
#        return math.sqrt(s*(s-self.a)(s-self.b)(s-self.c))
    
# shapes = [circle(7),rectangle(4,6),triangle(3,4,5)]

# print(shape.area(shapes))
# print(shape.perimeter(shapes))

class Shape:

    def area(self):
        return 0

    def perimeter(self):
        return 0


class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r


class Rectangle(Shape):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) **0.5


shapes = [
    Circle(7),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print("Shape:", type(shape).__name__)
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
    print()
 







  


    
