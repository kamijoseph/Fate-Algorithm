
# Simple Aritmetic Calculator
import math

def calculate():
    try:
        num1 = float(input("Enter the first number"))
        operator = input("Enter the operator (+, -, *, /, %, ^, sqrt): ").strip()
        if operator.lower() == "sqrt":
            result = math.sqrt(num1)
            print(f"The square root of {num1} is {result}")
        else:
            num2 = float(input("Enter the second number: "))
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("You cannot divide by zero!")
                    return
            elif operator == "%":
                result = num1 % num2
            elif operator == "^":
                result = num1 ** num2
            else:
                print("Invalid operators! Supported operators are +, -, *, /, %, ^, sqrt")
                return
            
            
        
    except ValueError:
        print("Invalid Input! Enter a vali numerical number.")
        return
    