
# Simple Aritmetic Calculator
import math

def calculate():
    try:
        num1 = float(input("Enter the first number"))
        operator = input("Enter the operator (+, -, *, /, %, ^, sqrt): ").strip()
        if operator.lower() == "sqrt":
            result = math.sqrt(num1)
            print(f"The square root of {num1} is {result}")
            
        
    except ValueError:
        print("Invalid Input! Enter a vali numerical number.")
        return
    