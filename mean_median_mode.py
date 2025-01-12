
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
    pass

def main():
    pass

if __name__ == "__main__":
    main()
