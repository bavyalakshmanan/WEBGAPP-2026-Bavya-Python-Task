class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}:{self.price:.2f}"
    
class discount:
    discount = 0.10

    def discountedprice(self):
        return self.price *(1-self.discount)
    
class ElectronicsProduct(product,discount):

    def __init__(self,name,price,warranty):
        super().__init__(name,price)
        self.warranty = warranty

    
    def describe(self):
        base = super().describe()
        return f"{base} Warranty: {self.warranty}"
    
laptop = ElectronicsProduct("THINKPAD",40000,3)

print(laptop.describe())
print(laptop.discountedprice())
print(ElectronicsProduct.__mro__)
