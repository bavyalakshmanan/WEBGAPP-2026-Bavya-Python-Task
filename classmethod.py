# class Student:
#     college = "ABC College"

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def change_college(cls, new_college):
#         cls.college = new_college

#     def display(self):
#         print("Name:", self.name)
#         print("College:", self.college)


# Student.change_college("Michael college")


# s1 = Student("Ishwarya")
# s1.display()

class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

    @classmethod 
    def change_college(cls, new_college):
     cls.college =  new_college
    def display (self):

        print("Name:",self.name)
        print("College:",self.college)

Student.change_college("Michael college")

s1 = Student("Bavya")
s1.display()