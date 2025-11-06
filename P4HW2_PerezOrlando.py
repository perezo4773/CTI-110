# Orlando Perez 
# 10/16/2025
# P4HW2
# Get pay amount for employee multiple employees 

print()
# Get employee name
name = input("Enter employee's name: ")

#Get hours worked from employee
hours = float(input("Enter number of hours worked: "))

#Get pay rate from employee 
rate= float(input("Enter employee's pay rate: "))

# Initialize counters
count = 0
#look over questionable 
num_employees = 0
# while loop
while count < num_employees:
    print()
    print(f"{count + 1} ")

# new 
total_reg_pay = 0
total_ot_pay = 0
total_gross_pay = 0

# Get total hourly rate
reg_hour = 40
overtime_rate = 1.5
# Calculate rate  
if hours <= reg_hour:
    reg_pay = reg_hour * rate
    overtime_hours = 0
    overtime_pay = 0
    gross_pay = reg_pay
else:
    overtime_hours = hours - reg_hour
    reg_pay = reg_hour * rate
    overtime_pay = rate * overtime_rate * overtime_hours
    gross_pay = (reg_hour * rate) + (overtime_hours * rate * overtime_rate)

print("-----------------------------------------")
print(f"{"Employee name:":<15} {name}")
print()
print(f'{'Hours Worked':<10}  {'Pay Rate':<10}   {'Overtime':<10}   {'Overtime Pay':<10}   {'RegHour Pay':<10}   {'Gross Pay':<10}')
print("------------------------------------------------------------------------------------------------------")
print(f"{hours:<13.2f} ${rate:<13.2f} {overtime_hours:<12.2f} ${overtime_pay:<11.2f} ${reg_pay:<13.2f} ${gross_pay:<15.2f}")
