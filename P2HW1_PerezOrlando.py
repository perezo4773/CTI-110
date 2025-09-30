#Orlando Perez
#9/18/2025
#P1HW2
#Get calculations for travel expenses
print()
print("This program calculates and displays travel expenses")
print()

#Get budget value (int) from the user 
Budget= float(input("Enter Budget: "))
print()
#Get destination from user
Destination= input("Enter your travel destination: ")
print()
#Get gas value (int) cost from user
Fuel= float(input("How much do you think you will spend on gas? ") ) 
print()
#Get hotel value (int) from user
Accommodation= float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
#Get food value (int) from user
Food= float(input("Last, how much do you need for food? "))
print()
print()
print("------------Travel Expenses------------")

print(f"{'Location:<:40', Destination")
print("Initial Budget:",     Budget)
print("Fuel:",               Fuel)
print("Accommodation:",      Accommodation)
print("Food:",Food)
print("----------------------------------------")
print()
print()
#Display Remaining balance
print("Remaining Balance: ",Budget - Fuel - Accommodation - Food)





