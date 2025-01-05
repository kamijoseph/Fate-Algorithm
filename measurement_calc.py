
# Units Of Measurement Conversion Calculator

# Distance Converter
def distance_converter():
    unit = input("Is the distance in Miles or kilometers? ").strip().lower()
    try:
        distance = float(input("Enter the distance (e.g 5.0/ 6.3): "))
    except ValueError:
        print("Invalid Number.Please enter a valid numerical value")
        return
    
    if unit == "miles":
        converted_distance = round(distance * 1.60934, 2)
        print(f"{distance} miles is equal to {converted_distance * 1.60934} kilometers")
    elif unit == "kilometers":
        converted_distance = round(distance / 1.60934, 2)
        print(f"{distance} kilometers is equal to {converted_distance / 1.60934} miles")
    else:
        print("Invalid unit. Please enter either miles or kilometers")
        return
