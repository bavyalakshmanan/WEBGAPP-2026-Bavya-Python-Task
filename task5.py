class passenger:

    def __init__(self,name, ticketprice):
        self.name = name
        self.ticketprice = ticketprice

    def travel (self):
        print("PASSENGER NAME:", self.name)    
        print("TICKETPRICE:", self.ticketprice)


travelers = [
             passenger("Arun", 200),
             passenger("Varun",400),
             passenger("Tharun",600),
]

for p in travelers:
    p.travel()

i = 0
total = 0


while i < len(travelers):
     total += travelers[i].ticketprice
     i += 1


print("TOTAL TICKETPRICE:", total)