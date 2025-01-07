
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

