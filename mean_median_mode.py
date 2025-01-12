# Mean, Mode, and Median Calculator

# Mean calculation function
def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

# Mode Search function
def mode(numbers):
    max_count = (0, 0)
    for number in numbers:
        occurrence = numbers.count(number)
        if occurrence > max_count[0]:
            max_count = (occurrence, number)
    return max_count[1]

# Median Evaluation function
def median(numbers):
    numbers.sort()
    
    # Odd Length of numbers
    if len(numbers) % 2 == 1:
        return numbers[len(numbers) // 2]
    
    # Even Length of Numbers
    else:
        num1 = numbers[len(numbers) // 2 - 1]
        num2 = numbers[len(numbers) // 2]
        
        # Using the mean function above
        return mean([num1, num2])

def main():
    print("Welcome, This is the Mean, Median, and Mode Program")
    numbers = []

    users_numbers = input("Enter your numbers separated by commas (e.g., 1,3,4,5,6): ")
    try:
        numbers = [int(num) for num in users_numbers.split(',')]
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by commas.")
        return

    program_choice = input("For Mean press 1\nFor Mode press 2\nFor Median press 3\nFor all press 4\nEnter choice: ")
    if program_choice == "1":
        print(f"Mean: {mean(numbers)}")
    elif program_choice == "2":
        print(f"Mode: {mode(numbers)}")
    elif program_choice == "3":
        print(f"Median: {median(numbers)}")
    elif program_choice == "4":
        print(f"Mean: {mean(numbers)}")
        print(f"Mode: {mode(numbers)}")
        print(f"Median: {median(numbers)}")
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
