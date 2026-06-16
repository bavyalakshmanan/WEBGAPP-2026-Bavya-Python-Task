from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def charge(self, amount: float) -> bool:
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        pass

    def receipt(self, amount):
        return f"Receipt: ₹{amount:.2f} processed via {self.__class__.__name__}"


class RazorpayGateway(PaymentGateway):

    def charge(self, amount):
        print(f"Razorpay: charging ₹{amount}")
        return True

    def refund(self, txn_id):
        print(f"Razorpay: refunding {txn_id}")
        return True


class StripeGateway(PaymentGateway):

    def charge(self, amount):
        print(f"Stripe: charging ${amount}")
        return True

    def refund(self, txn_id):
        print(f"Stripe: refunding {txn_id}")
        return True



rzp = RazorpayGateway()
stripe = StripeGateway()


rzp.charge(500)
print(rzp.receipt(500))
rzp.refund("TXN1001")

print()

stripe.charge(1000)
print(stripe.receipt(1000))
stripe.refund("TXN2001")

