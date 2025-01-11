
# Binomial Ditributions Calculator
def binomial_distributions():
    pass

def main():
    print ("=== Binomial Distribution Calculator === \n")
    print ("=== Solution must have a binary outcome ===")
    print ("=== Trials should be indipendent ===")
    print ("=== Number of trials should be included ===")
    print ("=== The probability of each trial should be equal ===")
    print ("=== The probability should be between 0 and 1 ===\n")
    print("---------------------------------------------------------")
    
    calculate_bs = input("To calculate, press 1 and 2 to exit: ")
    if calculate_bs == "1":
        binomial_distributions()
    else:
        print("Goodbye! See you next time!")

if __name__ == "__main__":
    main()