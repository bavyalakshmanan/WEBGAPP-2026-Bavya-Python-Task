class Department:

    def __init__(self,studentname):
        self.studentname = studentname

    def details(self):
        return "Student Details"
    
class CSE(Department):

    def details(self):
        return f"{self.studentname}: CSE Department"
    
class IT (Department):

    def  details(self):
     return f"{self.studentname}: IT Department"
  
class student(CSE):
   
    def __init__(self,studentname,project):
      super().__init__(studentname)
      self.project = project


    def details(self):
      super().details()
      print(CSE.details(self))
      return f"{self.studentname} is doing {self.project} project"
   
s1 = CSE("Arun")
s2 = IT("Kumar")
s3 = student("Santhosh","Gym Management System")


print(s1.details())
print(s2.details())
print(s3.details())
