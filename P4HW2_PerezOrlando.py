# Orlando Perez 
# 11/2/2025
# P4HW2
# Get pay amount for employee multiple employees 

# new variables



num_employees = 0
total_reg_pay = 0
total_ot_pay = 0
total_gross_pay = 0

print()
# Get employee name
name = input("Enter employee's name or 'Done' to terminate: ")

# Use a while loop to get  grades from the user
while name != "Done":
    num_employees += 1
    
    



    #Get hours worked from employee
    hours = float(input("Enter number of hours worked: "))

    # Get pay rate from employee 
    rate= float(input("Enter employee's pay rate: "))


    # Get total hourly rate
    reg_hour = 40
    overtime_rate = 1.5
    # Calculate rate  
    if hours <= reg_hour:
        reg_pay = hours * rate
        overtime_hours = 0
        overtime_pay = 0
        gross_pay = reg_pay
    else:
        overtime_hours = hours - reg_hour
        reg_pay = reg_hour * rate
        overtime_pay = rate * overtime_rate * overtime_hours
        gross_pay = (reg_hour * rate) + (overtime_hours * rate * overtime_rate)
    total_reg_pay +=  reg_pay
    total_ot_pay += overtime_pay
    total_gross_pay += gross_pay
    
    

    print("-----------------------------------------")
    print(f"{"Employee name:":<15} {name}")
    print()
    print(f'{'Hours Worked':<10}  {'Pay Rate':<10}   {'Overtime':<10}   {'Overtime Pay':<10}   {'RegHour Pay':<10}   {'Gross Pay':<10}')
    print("------------------------------------------------------------------------------------------------------")
    print(f"{hours:<13.2f} ${rate:<13.2f} {overtime_hours:<12.2f} ${overtime_pay:<11.2f} ${reg_pay:<13.2f} ${gross_pay:<15.2f}")
    name = input("Enter employee's name or Done to terminate: ")
    
# Display results
print(f"{'Total number of employees entered: ':<20} {num_employees}")
print(f"{'Total amount paid for overtime:':<20} {total_ot_pay:.2f}")
print(f"{'Total amount paid for regular hours':<20} {total_reg_pay:.2f}")
print(f"{'Total amount paid in gross:':<20} {total_gross_pay:.2f}")