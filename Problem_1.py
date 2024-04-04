'''
1. Exceptional Weather Forecast

Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a 
weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start
Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

Ensure that your program only accepts numerical input and provides a friendly error message if 
the user enters something that can't be converted to a number.

Task 2: Temperature Conversion
Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

Task 3: User Experience
Implement an else block that prints the converted temperature in a user-friendly format.

Add a finally block that thanks the user for using the weather forecast application, 
ensuring that this message is displayed regardless of whether an exception was caught or not.
'''

def temp_conversion(temp):
    try:
        if temp < -50:
            raise ZeroDivisionError("Number provided is way too low. Try again")
        if temp > 120:
            raise OverflowError("Number provided is way too high. Try again")
    except ZeroDivisionError as ze:
        print(ze)
    except OverflowError as oe:
        print(oe)
    else:
        converted_temp = (temp - 32) * 5/9
        print(f"\nGreat job! Your converted temperature is: {converted_temp}\n")


while True:
    try:
        user_input = float(input("Welcome to the program! Please enter the temperature in Fahrenheit or type '00' to finish: "))
        if user_input == 00:
            break
    except ValueError:
        print("Invalid number. Please try again!")
    else:
        converted_temp = temp_conversion(user_input)
    finally:
        print("Thank you for using the conversion program!\n")


