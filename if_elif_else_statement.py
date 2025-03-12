# if_elif_else_statement.py

# Step 1: Get input from the user
user_input = input("Enter your numeric grade: ")

# Step 2: Convert the input to an integer
try:
    grade = int(user_input)
    
    # Step 3: Determine the letter grade using if...elif...else
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    # Step 4: Print the letter grade
    print("Your grade is:", letter_grade)

except ValueError:
    # Input validation: handle non-integer input
    print("Invalid input. Please enter an integer.")
