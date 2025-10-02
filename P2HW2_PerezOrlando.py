# Orlando Perez 
# 10/3/2025
# P2HW2
# Create list of module Grades
print()
# Get module 6 grade value from user 
Module_1= float(input("Enter grade for Module 1: "))

# Get module 2 grade value from user
Module_2= float(input("Enter grade for Module 2: "))

# Get module 3 grade value from user
Module_3= float(input("Enter grade for Module 3: ") ) 

# Get module 4 grade value from user
Module_4= float(input("Enter grade for Module 4: "))

# Get Get module 5 grade value from user
Module_5= float(input("Enter grade for Module 5: "))
# Get module 6 grade value from user
Module_6 = float(input("Enter grade for Module 6: "))
print()
print()
 # create list of Module
grades = [Module_1,Module_2,Module_3,Module_4,Module_5,Module_6]

#print the list of Module grades
print()
print(grades)
# Function to give the # of items in a list
print()
list_grades = len(grades)

# Get results of Module grades
print("------------Results------------")
print((f"{'Lowest Grade:':<20} {(min)(grades)}"))
print((f"{'Highest Grade:':<20} {(max)(grades)}"))
print((f"{'Sum of Grade:':<20} {(sum)(grades)}"))
print(f"{'Average:':<20} {(sum)(grades)/ list_grades:.2f}")
print("-----------------------------------------")