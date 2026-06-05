# class name():
#     def stu(self):
#         print("I am sutdent")
# SI =name()
# SI.stu()

class Student:
    def __init__(self,name,roll_no):
       self.name = name
       self.roll_no = roll_no
    
    def report(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print()

s1 = Student("Ishwarya", 101)
s2 = Student("Kaviya",102)
s3 = Student("Bavya", 103)

s1.report()
s2.report()
s3.report()