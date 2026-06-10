class department:

    def __init__(self,name):
        self.name = name

    def details(self):
         return "student name"

class VL(department):
    def details(self):
         return f"{self.name} is belong to  VL department"

class EEE(department):       
    def details (self):
         return f"{self.name} is belong to EEE department"
    
class task(VL):
    def __init__(self,name,project):
        self.project = project
        super().__init__(name)

    def details(self):
        return f"{self.name} done the {self.project} project"
    

s1 = VL("Ajay")
s2 = EEE("Vijay")
s3 = task("Raj","TRACKING")

print(s1.details())
print(s2.details())
print(s3.details())