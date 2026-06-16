class employee:
    def salary(self):
        return 0

    
class Develpoer(employee):
   def salary(self):
        return 60000
    
class Tester (employee):
    def salary(self):
        return 70000

class Manager(employee):
    def salary(self):
        return 80000

employees = [
    Develpoer(),
    Tester(),
    Manager()
]

for emp in employees:
    print(type(emp).__name__)
    print("salary:",emp.salary())
    # print()
