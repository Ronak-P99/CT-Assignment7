'''
2. The Recipe Ratio Adjuster

Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, 
handling any type of arithmetic errors or user input exceptions.

Task 1: Start
Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

Task 2: Quantity Calculation
Calculate the adjustment factor by dividing the desired servings by the original servings.

Use a try block to catch any arithmetic errors that may occur during the calculation.

Task 3: Serving Success
If the calculation is successful, display the adjusted recipe quantities to the user.

Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

'''

def adjustment_factor(original, desired):
    try:
       adjusted =  desired / original
       print(f"\nYour adjusted recipe value is: {adjusted}")
    except ZeroDivisionError:
        print("\nYour original value can not be 0!")

try:
    while True:
        user_package_serving = float(input("\nWelcome! Please provide how many servings are specified on your recipe: "))
        user_serving = float(input("\nNow, specify the number of servings you wish to make: "))
        adjustment_factor(user_package_serving, user_serving)

        
        try_again_input = input("\nWould you like to adjust your recipe again? (yes/no) ")
        if try_again_input.lower() != 'yes':
            break

except ValueError:
    print("\nPlease provide numbers")

finally: 
    print("\nYum, your meal will come out amazing!")       