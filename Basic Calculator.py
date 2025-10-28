class calculator:
    def addition(self,a,b):
        return a+b
    def division(self, a, b):
        if b == 0:
            return "you can't divide by zero"
        else:
            return a / b
    def multiplication(self,a,b):
        return a*b
    def subtraction(self,a,b):
        return a-b

Calculator = calculator()
a=float(input("please enter first number:"))
b=float(input("please enter second number:"))
operation = input("Choose the operation you want to perform (+, -, *, /): ")
if operation == "+":
    print(Calculator.addition(a,b))
elif operation == "-":
    print(Calculator.subtraction(a,b))
elif operation == "*":
    print(Calculator.multiplication(a,b))
elif operation == "/":
    print(Calculator.division(a,b))
else:
    print("Invalid operation")