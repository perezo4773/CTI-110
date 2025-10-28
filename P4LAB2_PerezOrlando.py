# Orlando Perez 
# 10/28/2025
# P4LAB2
# Use nested loop

# Create a variable so that the while loop is True for first run 
run_again = "yes"

# While loop to coontrol running/ending the program
while run_again == "yes":
    print("Program is running...")
    print()
    # get an interger from the user
    user_num = int(input("Enter an interger: "))
    
    if user_num >= 0:
        print("Display Multiplication")
        print()
        # For loop to display the multiplication
        for i in range (1,13):
            print(f"{user_num} * {i} = {user_num * i} ")
            
    print()
    if user_num < 0:
        print("This program does not handle negative number")
        
    
    
    run_again = input("Would you like to run the program again? ").lower()    
# Loop breaks here
print()
print("Thanks for using the program... Goodbye!")
    
