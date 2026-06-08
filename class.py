# __init__ is used to store a data...each object has seperate storage space
#self is used as keyword to get value of current object

class student:

     def __init__(self,name,dep):
        self.name = name
        self.dep = dep 


     def details (self):
       return f"{self.name} belongs to {self.dep} department"
     

s1 = student("Raj" , "VL")
s2 = student("Hari","ECE")


print(s1.details())
print(s2.details())

