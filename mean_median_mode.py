
# Mean, and Median Median Calculator

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
        occurence = numbers.count(number)
        if occurence > max_count[0]:
            max_count = (occurence, number)
    return max_count[1]

# Median Evaluation function
def median(numbers):
    numbers.sort()
    
    # Odd Length of numbers
    if len(numbers) % 2 == 1:
        return numbers[len(numbers) // 2]
    
    # Even Length of Numbers
    elif len(numbers) % 2 == 0:
        num1 = numbers[len(numbers) // 2 - 1]
        num2 = numbers[len(numbers) // 2]
        
        # Using the mean function above. there is an easer way but this is my code fren
        meanx = mean(num1,num2)
        return meanx

def main():
    print("Welcome, This is the Mean, Median and Mode Programme")
    numbers = []
    
    try:
        users_numbers = int(input("Enter your numbers (1,3,4,5,6,etc): "))
        numbers.append(users_numbers)
        # return numbers
    except ValueError:
        print("Invalid input! Enter valid numerical values")
        
    program_choice = input("For Mean press 1\nFor Mode press 2\nFor Median press 3\nFor all press 4\nEnter choice: ")
    if program_choice == "1":
        mean(numbers)
    elif program_choice == "2":
        mode(numbers)
    elif program_choice == "3":
        median(numbers)
    elif program_choice == "4":
        mean(numbers)
        mode(numbers)
        median(numbers)

if __name__ == "__main__":
    main()
