
# Simple Compound Interest Calculator
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value  > 0:
                return value
            else:
                print("Value must be greater than zero. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_compound_interest():
    principal = get_positive_float("Enter the principal amount: ")
    rate = get_positive_float("Enter the annual interest rate: ")
    time = get_positive_float("Enter the time in years: ")
    
    # Calculate the compound interest
    amount = principal * (1 + rate/ 100) ** time
    
    # Display the result
    print(f"\nPrincipal amount: ${principal:.2f}")
    print(f"Annual interest rate: {rate:.2f}%")
    print(f"Time in years: {time:.2f}")
    print(f"Amount after {time} years: ${amount:.2f}")

def main():
    print("\nWelcome. This is a simple compound interest calculator.")