
# print("1.")
# for i in range (4, 0, -1):
#      for j in range (i):
#           print(4 - j,  end=" ")
#           print ()

# print("2.")
# for i in range (4):
#          for j in range (4):
#              print(4 - j,  end=" ")
#          print ()

# print("3.")
# for i in range(4):
#     for j in range(4):
#         if i == 0 or i == 3 or j == 0 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# print("4.")

# for i in range(65, 91):
#     print(chr(i), "=", i)

# print("5.")

# class Laptop:

#     def __init__(self, brand, product, showroom, price, ram, processor):

#         self.brand = brand
#         self.product = product
#         self.showroom = showroom
#         self.price = price
#         self.ram = ram
#         self.processor = processor

#     def report(self):

#         print("Brand:", self.brand)
#         print("Product:", self.product)
#         print("Showroom:", self.showroom)
#         print("Price:", self.price)
#         print("RAM:", self.ram)
#         print("Processor:", self.processor)
#         print()


# l1 = Laptop("Lenovo", "IdeaPad Slim 3",
#             "Lenovo Exclusive Store", "₹45,000",
#             "8GB", "Intel Core i3")

# l2 = Laptop("HP", "Victus 15",
#             "HP World", "₹68,000",
#             "16GB", "AMD Ryzen 5")

# l3 = Laptop("Dell", "Inspiron 15",
#             "Dell Exclusive Store", "₹52,000",
#             "8GB", "Intel Core i5")

# l4 = Laptop("Acer", "Nitro V",
#             "Acer Mall", "₹75,000",
#             "16GB", "Intel Core i7")

# l5 = Laptop("ASUS", "VivoBook 15",
#             "ASUS Exclusive Store", "₹50,000",
#             "8GB", "AMD Ryzen 3")


# l1.report()
# l2.report()
# l3.report()
# l4.report()
# l5.report()

print("6.")
class Laptop:
    price = 50000
    def __init__(self, brand, product, showroom,  ram, processor):

        self.ram = ram
        self.brand = brand
        self.product = product
        self.showroom = showroom
        self.processor = processor

    def report(self):

        print("Brand:", self.brand)
        print("Product:", self.product)
        print("Showroom:", self.showroom)
        print("Price:", self.price)
        print("RAM:", self.ram)
        print("Processor:", self.processor)
        print()


l1 = Laptop("Lenovo", "IdeaPad Slim 3",
            "Lenovo Exclusive Store",
            "8GB", "Intel Core i3")

l2 = Laptop("HP", "Victus 15",
            "HP World",
            "16GB", "AMD Ryzen 5")

l3 = Laptop("Dell", "Inspiron 15",
            "Dell Exclusive Store", 
            "8GB", "Intel Core i5")

l4 = Laptop("Acer", "Nitro V",
            "Acer Mall",
            "16GB", "Intel Core i7")

l5 = Laptop("ASUS", "VivoBook 15",
            "ASUS Exclusive Store", 
            "8GB", "AMD Ryzen 3")


l1.report()
l2.report()
l3.report()
l4.report()
l5.report()