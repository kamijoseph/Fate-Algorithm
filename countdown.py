# Count down counter
import time

def count_down():
    my_timer = int(input("Enter the time in Seconds: "))
    
    for x in range(my_timer, 0, -1):
        seconds = x % 60
        minutes = int((x / 60)) % 60
        hours = int((x / 3600))
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("Time's up anon")
    
def main():
    count_down()
    return "Countdown Timer"

if __name__ == "__main__":
    main()