# Mean, Median, and Mode Calculator

def mean(numbers):
    total = sum(numbers)
    return total / len(numbers)


def mode(numbers):
    max_count = (0, 0)
    for number in numbers:
        occurrence = numbers.count(number)
        if occurrence > max_count[0]:
            max_count = (occurrence, number)
    return max_count[1]


def median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 1: 
        return numbers[length // 2]
    else: 
        num1 = numbers[length // 2 - 1]
        num2 = numbers[length // 2]
        return mean([num1, num2])

def main():
    print("Welcome! This is the Mean, Median, and Mode Calculator.")
    while True:
        numbers = []
        while True:
            try:
                users_numbers = input("Enter your numbers separated by commas (e.g., 1,3,4,5,6): ")
                numbers = list(map(int, users_numbers.split(',')))
                break
            except ValueError:
                print("Invalid input. Please enter only numbers separated by commas.")
        
        while True:
            print("\nOptions for calculations:")
            print("1. Calculate Mean")
            print("2. Calculate Mode")
            print("3. Calculate Median")
            print("4. Calculate All together")
            program_choice = input("Enter your choice (1/2/3/4): ").strip()

            if program_choice == "1":
                print(f"Mean: {mean(numbers):.2f}")
            elif program_choice == "2":
                print(f"Mode: {mode(numbers)}")
            elif program_choice == "3":
                print(f"Median: {median(numbers)}")
            elif program_choice == "4":
                print(f"Mean: {mean(numbers):.2f}")
                print(f"Mode: {mode(numbers)}")
                print(f"Median: {median(numbers)}")
            else:
                print("Invalid choice. Please select a valid option (1/2/3/4).")
                continue

            run_again = input("\nWould you like to calculate again with the same numbers? (yes/no): ").lower()
            if run_again == "no":
                break

        new_set = input("\nWould you like to calculate with a new set of numbers? (yes/no): ").lower()
        if new_set == "no":
            print("Thank you for using the calculator! Goodbye!")
            break

if __name__ == "__main__":
    main()
