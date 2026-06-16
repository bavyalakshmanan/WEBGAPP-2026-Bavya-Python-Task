# from abc import ABC

# class PaymentGateway(ABC):

#     @abstractmethod

#     def charge(self,amount:float,currency:str)-> dict:
#         pass

#     @abstractmethod

#     def refund(self,txnid:str,amount:float)-> bool:
#         pass
    
#     def generatereceipt (self,amount,currency,txnid):

#         return {
#             "txnid": txnid,
#             "amount":amount,
#             "currency":currency,
#             "gateway":self.__class.name__,
#             # "time": datetime.datetime.now().isoformat()
#         }
    
#     class RazorpayGateway(PaymentGateway):

#         def charge(self,amount,currency='INR'):
#             txn = f 'rzp_{id(self):x}'

#             print(f'[Razorpay] charging {currency} {amount}')
#             return self.generatereceipt(amount,currency,txn)
    
#         def refund(self, txnid,amount):

#             print(f'[Razorpay] Refunding{amount}')
#             return True
from abc import ABC, abstractmethod
import datetime

class PaymentGateway(ABC):

    @abstractmethod
    def charge(self, amount: float, currency: str) -> dict:
        pass

    @abstractmethod
    def refund(self, txn_id: str, amount: float) -> bool:
        pass

    def generate_receipt(self, amount, currency, txn_id):
        return {
            'txn_id': txn_id,
            'amount': amount,
            'currency': currency,
            'gateway': self.__class__.__name__,
            'time': datetime.datetime.now().isoformat()
        }


class RazorpayGateway(PaymentGateway):

    def charge(self, amount, currency='INR'):
        txn = f'rzp_{id(self):x}'
        print(f'[Razorpay] Charging {currency} {amount}')
        return self.generate_receipt(amount, currency, txn)

    def refund(self, txn_id, amount):
        print(f'[Razorpay] Refunding {amount}')
        return True


# Create Object
gateway = RazorpayGateway()

# Charge Payment
receipt = gateway.charge(500)

print("\nReceipt:")
print(receipt)

# Refund Payment
gateway.refund(receipt['txn_id'], 500)


