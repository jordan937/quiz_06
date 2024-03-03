class Order_store:
    def __init__(self):
        self.name = "customer"

    def store(self, customer):
        print(f"Storing order for {customer}")

class Order_calc:
    @staticmethod
    def calc():
        print("calc")

class Order_val:
    @staticmethod
    def valid():
        print("valid")

class Order_send:
    @staticmethod
    def send():
        print("send")

class Order_upd:
    @staticmethod
    def update():
        print("update")

def main():
    obj = Order_store()
    obj.store('Emma')

if __name__ == "__main__":
    main()