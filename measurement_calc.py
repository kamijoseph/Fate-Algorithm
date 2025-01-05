
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

# Temperature Converter
def temperature_converter():
    unit = input("Is the temperature in Celsius or Fahrenheit? ").strip().lower()
    try:
        temperature = float(input("Enter the temperature (e.g 5.0/ 60.3): "))
    except ValueError:
        print("Invalid Number.Please enter a valid numerical value")
        return
    
    if unit == "celsius":
        converted_temperature = round((temperature * 9/5) + 32, 2)
        print(f"{temperature} degrees Celsius is equal to {converted_temperature} degrees Fahrenheit")
    elif unit == "fahrenheit":
        converted_temperature = round((temperature - 32) * 5/9, 2)
        print(f"{temperature} degrees Fahrenheit is equal to {converted_temperature} degrees Celsius")
    else:
        print("Invalid unit. Please enter either celsius or fahrenheit")
        return

# Weight Converter   
def weight_converter():
    unit = input("Is the weight in Pounds or Kilograms? ").strip().lower()
    try:
        weight = float(input("Enter the weight (e.g 500.0/ 60.3): "))
    except ValueError:
        print("Invalid Number.Please enter a valid numerical value")
        return
    
    if unit == "pounds":
        converted_weight =  round(weight / 2.20462, 2)
        print(f"{weight} pounds is equal to {converted_weight} kilograms")
    elif unit == "kilograms":
        converted_weight = round(weight * 2.20462, 2)
        print(f"{weight} kilograms is equal to {converted_weight} pounds")
    else:
        print("Invalid unit. please enter either pounds or kilograms")
        return

# Volume Converter
def volume_converter():
    unit = input("Is the volume in litres or gallons?:").strip().lower()
    try:
        volume = float(input("Enter the volume (e.g 499.0/ 6000.7): "))
    except ValueError:
        print("Invalid Number. Please enter a valid numerical value")
        return
    
    if unit == "litres":
        converted_volume = round(volume * 0.264172, 2)
        print(f"{volume} litres is equal to {converted_volume} gallons")
    elif unit == "gallons":
        converted_volume = round(volume / 0.264172, 2)
        print(f"{volume} gallons is equal to {converted_volume} litres")
    else:
        print("Invalid unit. Please enter either litres or gallons")
        return
