class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark


    def details (self):
        print("Name:",self.name)
        print("Mark:",self.mark)


        if self.mark >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")


students=[
        student("Ajay" , 77),
        student("Bala" , 32),
        student("Rose" , 85 ),
        student("Hari" , 97),
        student("kumar" , 30)
         ]

for student in students:
    student.details()


i = 0
pass_count = 0
fail_count = 0

while i < len(students):

    if students[i].mark >= 50:
     
     pass_count += 1

    else:
     fail_count += 1

    i = i+1


print("NUMBER OF STUDENTS PASSED:",pass_count)
print("NUMBER OF STUDENTS FAILED:",fail_count)

