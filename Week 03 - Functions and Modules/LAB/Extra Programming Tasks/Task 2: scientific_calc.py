"""
## Task 2: Scientific Calculator (Unit Conversion Chart)
Create a Scientific Calculator imitating the Unit Conversion Chart (Fig. 1).

Allow the user to choose between length, temperature, mass, volume, pressure, and energy.
Create separate functions for each calculation within the types of unit.
Allow the user to choose between units.
For example, if the user chooses length, then the programme should allow the user to choose between conversions: m/ft, in/cm, or mi/km.
The user should then enter the value to calculate. Finally, the system should do the conversion and print out the result.

![Unit Conversion Chart](Unit-Conversion-Chart.png)

*Fig 1. Unit Conversion Chart*
"""

unit = (input("Choose a unit type (length, temperature, mass, volume, pressure, energy): ").lower())

def length():
    length_conversion = input("Choose a conversion (m/ft, in/cm, mi/km): ").lower()
    if length_conversion == "m/ft":
        value = float(input("Enter the value in meters: "))
        result = value * 3.28084
        print(f"{value} meters = {result:.2f} feet.")
    elif length_conversion == "in/cm":
        value = float(input("Enter the value in inches: "))
        result = value * 2.54
        print(f"{value} inches = {result:.2f} centimeters.")
    elif length_conversion == "mi/km":
        value = float(input("Enter the value in miles: "))
        result = value * 1.60934
        print(f"{value} miles = {result:.2f} kilometers.")
    else:
        print("Invalid conversion choice.")

def temperature():
    temp_conversion = input("Choose a conversion (C/F, F/C): ").lower()
    if temp_conversion == "c/f":
        value = float(input("Enter the value in Celsius: "))
        result = (value * 9/5) + 32
        print(f"{value} degrees Celsius = {result:.2f} degrees Fahrenheit.")
    elif temp_conversion == "f/c":
        value = float(input("Enter the value in Fahrenheit: "))
        result = (value - 32) * 5/9
        print(f"{value} degrees Fahrenheit = {result:.2f} degrees Celsius.")
    else:
        print("Invalid conversion choice.")

def mass():
    mass_conversion = input("Choose a conversion (kg/lb, lb/kg): ").lower()
    if mass_conversion == "kg/lb":
        value = float(input("Enter the value in kilograms: "))
        result = value * 2.20462
        print(f"{value} kilograms = {result:.2f} pounds.")
    elif mass_conversion == "lb/kg":
        value = float(input("Enter the value in pounds: "))
        result = value * 0.453592
        print(f"{value} pounds = {result:.2f} kilograms.")
    else:
        print("Invalid conversion choice.")

def volume():
    volume_conversion = input("Choose a conversion (l/gal, gal/l): ").lower()
    if volume_conversion == "l/gal":
        value = float(input("Enter the value in liters: "))
        result = value * 0.264172
        print(f"{value} liters = {result:.2f} gallons.")
    elif volume_conversion == "gal/l":
        value = float(input("Enter the value in gallons: "))
        result = value * 3.78541
        print(f"{value} gallons = {result:.2f} liters.")
    else:
        print("Invalid conversion choice.")

def pressure():
    pressure_conversion = input("Choose a conversion (Pa/psi, psi/Pa): ").lower()
    if pressure_conversion == "pa/psi":
        value = float(input("Enter the value in Pascals: "))
        result = value * 0.000145038
        print(f"{value} Pascals = {result:.2f} pounds per square inch.")
    elif pressure_conversion == "psi/pa":
        value = float(input("Enter the value in pounds per square inch: "))
        result = value * 6894.76
        print(f"{value} pounds per square inch = {result:.2f} Pascals.")
    else:
        print("Invalid conversion choice.")
    
def energy():
    energy_conversion = input("Choose a conversion (J/cal, cal/J): ").lower()
    if energy_conversion == "j/cal":
        value = float(input("Enter the value in Joules: "))
        result = value * 0.239006
        print(f"{value} Joules = {result:.2f} calories.")
    elif energy_conversion == "cal/j":
        value = float(input("Enter the value in calories: "))
        result = value * 4.184
        print(f"{value} calories = {result:.2f} Joules.")
    else:
        print("Invalid conversion choice.")

if unit == "length":
    length()
elif unit == "temperature":
    temperature()
elif unit == "mass":
    mass()
elif unit == "volume":
    volume()
elif unit == "pressure":
    pressure()
elif unit == "energy":
    energy()
