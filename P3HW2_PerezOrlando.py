# Orlando Perez 
# 10/16/2025
# P3HW2
# 

print()
# Get employee name
name = input("Enter employee's name: ")
#Get hours worked from employee
hours = float(input("Enter number of hours worked: "))
#Get pay rate from employee 
pay_rate= float(input("Enter employee's pay rate: "))
print("-----------------------------------------")
print(f"{"Employee name:":<15} {name}")
print()
print(f'{'Hours Worked':<10}  {'Pay Rate':<10}   {'Overtime':<10}   {'Overtime Pay':<10}   {'RegHour Pay':<10}   {'Gross Pay':<10}')
print("------------------------------------------------------------------------------------------------------")
print(f"{hours:<15.2f} {pay_rate:<15.2f}")
