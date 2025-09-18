#Orlando Perez
#9/18/2025
#P1HW2
#Get calculations for travel expenses
print()
print("This program calculates and displays travel expenses")
print()

#Get budget value (int) from the user 
Budget= int(input("Enter Budget: "))
print()
#Get destination from user
Destination= input("Enter your travel destination: ")
print()
#Get gas value (int) cost from user
Fuel= int(input("How much do you think you will spend on gas? ") ) 
print()
#Get hotel value (int) from user
Accomodation= int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
#Get food value (int) from user
Food= int(input("Last, how much do you need for food? "))
print()
print()
print("------------Travel Expenses------------")

print("Location: ",Destination)
print("Initial Budget:", Budget)
print()
print("Fuel:",Fuel)
print("Accomadation:", Accomodation)
print("Food:",Food)
print()
#Display Remaining balance
print("Remaining Balance: ",Budget - Fuel - Accomodation - Food)





