class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

credit_card = CreditCardPayment()
paypal = PayPalPayment()
bitcoin = BitcoinPayment()

processor = PaymentProcessor(credit_card)
processor.process_payment(1000)

processor.set_strategy(paypal)
processor.process_payment(1500)

processor.set_strategy(bitcoin)
processor.process_payment(2000)