name = ["hari" , "vijay" , "ram" ]
marks = [70 , 80 , 35 ]
department = ["VL" , "IT" , "CSE"]


def check(mark):
     if mark >= 50:
          return "pass"
     else:
          return "fail"
     
for i in range (len(name)):
    print("      name:" , name[i])
    print("     marks:" , marks[i])
    print("department:" , department[i])
    print("    result:" , check(marks[i]))

i = 0
pass_count = 0
fail_count = 0

while i < len(marks):
     if marks[i] >= 50:
          pass_count += 1
     else:
          fail_count += 1


     i += 1


print("number  of students passed:",pass_count)
print("number of students failed:",fail_count)
#i += 1 must be inside the while loop but outside the if else block.