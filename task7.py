class design:

    def __init__ (self,patten):
        self.patten =  patten
    
# 2nd def is known as method.
    def display (self):
        for  i in range(self.patten):
            for j in range(self.patten):
                

                if i==j:
                    print("p", end=" ")
                else:
                    print("-",end = " ")

            print()

p = int(input("ENTERN THE VALUE:"))
p1 = design(p)
p1.display()