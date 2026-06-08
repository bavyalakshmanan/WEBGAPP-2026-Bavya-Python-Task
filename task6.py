class design:
    def __init__(self,element):
        self.element = element

    def display(self):
     for i in range(5):
       for j in range(5):

          if i == 0 or i == 4 or j == 0 or j == 4:
            print(self.element,end=" ")

          else:
             print(" ", end= " ")

       print()

v = int(input("Enter the value"))
v1 =design(v)
v1.display()