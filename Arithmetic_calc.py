
# Simple Aritmetic Calculator
import math

def calculate():
    try:
        num1 = float(input("Enter the first number: "))
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
            print(f"{num1} {operator} {num2} = {result}")   
    except ValueError:
        print("Invalid Input! Enter a vali numerical number.")
        return
    
def main():
    print("Welcome to the Arithmetic Calculator")
    while True:
        # Choice to calculate or exit
        calculate_choice = input("Do you want to calculate? (yes/no): ").strip().lower()
        if calculate_choice == "yes":
            calculate()
        elif calculate_choice == "no":
            print("Thank you for using the Arithmetic Calculator")
            break
        else:
            print("Invalid Input! Enter yes or no")
            continue
        
if __name__ == "__main__":
    main()
    
# Calculator Finished