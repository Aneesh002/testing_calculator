import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

class calculator:

    def add(self, x, y):
        logging.info("Performing addition")
        return x + y

    def sub(self, x, y):
        logging.info("Performing subtraction")
        return x - y

    def mul(self, x, y):
        logging.info("Performing multiplication")
        return x * y

    def div(self, x, y):
        logging.info("Performing division")
        return x / y

    def operation(self):
        while True:
            print("1. for adding ")
            print("2. for sub ")
            print("3. for mul ")
            print("4. for div")

            choice = input("Enter the value from 1-4   ")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", self.add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", self.sub(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", self.mul(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", self.div(num1, num2))
            else:
                print("Invalid input")


if __name__=="__main__":
    calc = calculator()
    calc.operation()