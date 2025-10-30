# Orlando Perez 
# 10/30/2025
# P4HW1
# 


# I empty list to store scores
grades = []

# Get number of grades from User
user_grades = int(input(" How many scores do you want to enter? "))
# Use a while loop to get  grades from the user
for g in range (user_grades) :
    grade = float(input(f"Enter Score # {g+1}: "))

    while grade < 0 or grade > 100: 
            print("INVALID Score entered !!!!")
            print("Score should be between 0 and 100 ")
            grade = float(input(f"Enter score # {g+1} again: ")) 
    grades.append(grade)


# Calculate results

low = min(grades)
high = max(grades)
grades.remove(min(grades))
total = sum(grades)
avg = total / len(grades)



# Display results
print("------------ Results ------------")
print(f"{'Lowest Score:':<20} {low}")
print(f"{'Modified List:':<20} {grades}")
print(f"{'Scores Average:':<20} {avg:.2f}")


# Determine letter grade based on average
if avg >= 90:
    print("Your grade is: A")
elif avg >= 80:
    print("Your grade is: B")
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")
print("---------------------------------")

