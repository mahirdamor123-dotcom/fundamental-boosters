# Interactive Personal Data Collector
# A simple beginner program using input, print, variables, types, and operators.

from datetime import date

print("=" * 55)
print("Welcome to the Interactive Personal Data Collector!")
print("Enter your name, age, height, and favourite number.")
print("Your answers are shown on screen and are not saved.")
print("=" * 55)

# Collect input and convert it to the appropriate data type.
name = input("Please enter your name: ").strip()
age = int(input("Please enter your age in whole years: "))
height = float(input("Please enter your height in meters (example 1.68): "))
favourite_number = int(input("Please enter your favourite whole number: "))

# Simple calculations with the values the user entered.
current_year = date.today().year
approximate_birth_year = current_year - age
age_next_year = age + 1
double_favourite_number = favourite_number * 2

# Show a conversion from a float to an integer.
# int() truncates the decimal part; round() gives a rounded value.
height_as_integer = int(height)
rounded_height = round(height)
age_as_text = str(age)

print("\n" + "=" * 55)
print("Here is the information you entered:")
print("=" * 55)

print(f"Name: {name}")
print(f"  Value: {name!r}")
print(f"  Type: {type(name).__name__}")
print(f"  id: {id(name)}")

print(f"\nAge: {age}")
print(f"  Type: {type(age).__name__}")
print(f"  id: {id(age)}")

print(f"\nHeight: {height:.2f} meters")
print(f"  Type: {type(height).__name__}")
print(f"  id: {id(height)}")

print(f"\nFavourite number: {favourite_number}")
print(f"  Type: {type(favourite_number).__name__}")
print(f"  id: {id(favourite_number)}")

print("\nCalculations and type conversions:")
print(f"Approximate birth year: {approximate_birth_year} (current year minus age)")
print(f"Age next year: {age_next_year}")
print(f"Favourite number doubled: {double_favourite_number}")
print(f"Height converted with int(): {height_as_integer} (decimal part removed)")
print(f"Height rounded to a whole number: {rounded_height}")
print(f"Age converted from int to str: {age_as_text!r} (type: {type(age_as_text).__name__})")

print("\nThank you for using the Personal Data Collector!")
print("Keep exploring Python!")
