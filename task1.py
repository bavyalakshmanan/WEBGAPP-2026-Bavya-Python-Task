marks = [70 , 50 , 30 , 20 , 90]
def check(mark):
     if mark >= 50:
          return "pass"
     else:
          return "fail"
i = 0
     
while  i < len(marks):
     result = check(marks[i])
     print("student",i+1,":",result)
     i = i + 1 
print("\n")
for i  in range(len(marks)):
     result = check(marks[i])
     print("student",i+1,":", result)