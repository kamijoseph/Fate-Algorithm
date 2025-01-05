
# Units Of Measurement Conversion Calculator
def distance_converter():
    unit = input("Is the distance in Miles or kilometers? ").strip().lower()
    try:
        distancee = float(input("Enter the distance: "))
    except ValueError:
        print("Invalid Number.Please enter a valid numerical value")
        return