from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(amount):
        pass

class RazorPay(PaymentGateway):
    @staticmethod
    def pay(amount):
        print("Init payment...")
        print("Transferring funds Rs "+str(amount))
        print("Transaction Successfull")
        print("Thank you for using Razorpay")

class CashFree(PaymentGateway):
    @staticmethod
    def pay(accNo,amount):
        print("Init payment...")
        print("Transferring funds Rs "+str(amount))
        print("Transaction Successfull")
        print("Thank you for using Cashfree")

# all are having pay(amount)