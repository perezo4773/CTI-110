# Orlando Perez
# 9/25/2025
# P2LAB2
# Using dictionaries


# Create Dictionary
cars= {"Camaro": 18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Create a variable to hold the keys 
keys = cars.keys()
print()
print(keys)
print()
#Get the name of one the cars from user
user_car= input("Enter a vehicle to see it's mpg: ")
print()
#Display the user's chosen car and it's mpg
print(f"The {user_car} gets {cars[user_car]} mpg.")
print()
# Get the miles to drive the car from the user
miles_to_drive = float(input(f"How many miles will you drive the {user_car}? " ))
#Calculate gallons of gas needed
gas_needed = miles_to_drive/cars[user_car]
print()
print(f"{gas_needed: .2f} gallon(s) of gas are needed to drive the {user_car} {miles_to_drive} miles.")












