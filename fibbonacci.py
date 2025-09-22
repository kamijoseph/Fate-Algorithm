
# Simple program to generate fibonacci numbers

def fib_generator(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("Welcome, this is the Fibonacci Number Generator")
    while True:
        try:
            n = int(input("Enter the number of fibonacci numbers you want to generate: "))
            if n < 1:
                print("Please enter a number greater than zero.")
                continue
            else:
                result = fib_generator(n)
                print(f"The first {n} Fibonacci numbers are: {result}")
                break
        except ValueError:
            print("Invalid input! Pleae enter a valid number.")

if __name__ == "__main__":
    main()