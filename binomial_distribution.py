
# Binomial Ditributions Calculator
from math import comb

def binomial_distributions():
    
    # Check for valid n, k and p numerical values
    while True:
        try:
            n = int(input("Enter the number of trials (n): "))
            k = int(input("Enter the number of successes (k): "))
            p = float(input("Enter the probability of success in a single try(p): "))
            
            # Probability should be between 0 and 1
            if not (0 <= p <= 1):
                print("Error: Probbility must be between 0 and 1")
                return
            
            # Implementing the binomial distributions Equation
            probability = comb(n, k) * (p**k) * ((1-p)**(n-k))
            print(f"\nThe probability of getting exactly {k} number of successes in {n} number of trials is {probability: .6f}")
            
        except ValueError:
            print("Please enter a valid numerical value.")
            
        # Calculate again Prompt
        calculate_again = input("would you like to perfom more calculations? (Yes/No): ").strip().lower()
        if calculate_again != "yes":
            print("\nExiting the Binomial distribution Calculator. Goodbye!")
            break

# Main function of the Programm
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