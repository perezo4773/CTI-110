# Orlando Perez
# 9/23/2025
# P2LAB1
# Calculate values related to a circle

import math 

# Get the radius from the user as a float
radius= float(input("What is the radius of the circle? "))

#Calculate diameter
diameter= 2 * radius

# Calculate circumference
circum= 2 * math.pi * radius

#Calculate Area
area= math.pi * radius ** 2

# Display results to the user
print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the is {circum:.2f}")
print()
print(f"The area of the circle is {area:.3f}")