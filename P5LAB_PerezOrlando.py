# Orlando Perez 
# 11/11/2025
# P5LAB
# Create a simulated customer self-checkout machine

import random 

def calculate_change(change):

    print()
    
    # Convert the value to a round number
    change = round(change * 100)


    # Display dollar amount 
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")  

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")


    if num_dimes> 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes") 

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels") 

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies") 
    if num_dollars < 1:
        if num_dollars == 0:
            print("no dollars")

# Define the main function
def main():
    # Generate a random value for cart total
    cart_total = round(random.uniform(0.01, 100.00), 2)
    print(f"Your total is: ${cart_total:.2f}")
    print()
    # Get cash in from user
    cash_in = float(input("Cash Entered: $"))
    
    # Calculate change owed
    customer_change = cash_in - cart_total
    
    # Display customer change
    print(f"Change owed to customer: ${customer_change:.2f}")
    
    
    
    # Call the function to calculate change
    calculate_change(customer_change)
    


# Call the main
main()