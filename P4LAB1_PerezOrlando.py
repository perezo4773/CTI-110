# Orlando Perez
# 10/23/2025
# P4LAB1
# Use loops to draw a square and triangle 
 
import turtle

# Create our drawing object (turtle)
yoshi = turtle.Turtle()

# Create a window to draw line 
window = turtle.Screen()

# Change the background 
window.bgcolor("blue")

# Change color of pen 
yoshi.pencolor("green")

# Make the pen size thicker 
yoshi.pensize(5)

# Logic to draw the square
sides = 4

while sides > 0:
    yoshi.forward(100)
    yoshi.right(90)
    # Decrement sides so the loop ends eventually 
    sides = sides - 1

# For loop to draw triangle
for t in range (3):
    yoshi.forward(100)
    yoshi.left(120)
    
    

# End of the program
window.mainloop()






