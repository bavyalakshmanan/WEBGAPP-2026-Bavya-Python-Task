class employee:
    def salary(self):
        return 0

    
class develpoer(employee):
   def salary(self):
        return 60000
    
class tester (employee):
    def salary(self):
        return 70000

class manager(employee):
    def salary(self):
        return 80000

employees = [
    develpoer(),
    tester(),
    manager()
]

for emp in employees:
    print(type(emp).__name__)
    print("salary:",emp.salary())
    print()
