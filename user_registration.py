"""
@Author: Prayag Bhoir
@Date: 19-08-2024
@Last Modified by: Prayag Bhoir
@Last Modified time: 20-08-2024
@Title : Python programs user ragistration on regex
"""
import re

def validate_name(name):
    """
    Description:
      This function validates the user name

    Parameters:
      name(str): User input name

    Returns:
      bool:True if match, False otherwise
    """
    pattern = "^[A-Z][A-Za-z]{2,}$"
    return bool(re.match(pattern,name))

def is_email_valid(email):
    """
    Description:
      This function validates the email

    Parameters:
      email(str): User input email

    Returns:
      bool:True if match, False otherwise
    """
    pattern = "^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$"
    return bool(re.match(pattern, email))


def is_mobile_valid(mobile):
    """
    Description:
      This function validates the mobile number

    Parameters:
      mobile(str): User input mobile number

    Returns:
      bool: True if match, False otherwise
    """
    pattern = r"^\d{2} \d{10}$"
    return bool(re.match(pattern, mobile))

def is_password_valid(password):
    """
    Description:
      This function validates the password based on predefined rules.

    Parameters:
      password (str): User input password.

    Returns:
      bool: True if match, False otherwise.
    """
    pattern = r'^(?=.*[A-Z]).{8,}$'  # Password must be at least 8 characters long
    return bool(re.match(pattern, password))

def validate_user_input(input_prompt, validation_func, success_message, failure_message):
    """
    Description:
      This function handles the validation of user input.

    Parameters:
      input_prompt(str): The prompt to be displayed to the user.
      validation_func(func): The function that validates the input.
      success_message(str): The message to display on successful validation.
      failure_message(str): The message to display on failed validation.

    Returns:
      bool: True if the user enters "0" to exit, False if the loop should continue.
    """
    while True:
        user_input = input(input_prompt)
        if user_input == "0":
            return None  # User to exit
        if validation_func(user_input):
            print(success_message)
            return user_input  # Valid input
        else:
            print(failure_message)


def main():
    # Validate first name
    first_name = validate_user_input(
        "Enter the first name (or 0 to exit): ",
        validate_name,
        "First name is valid",
        "First name is invalid, try again.\n"
    )
    if first_name is None:
        return  # User exited

    # Validate last name
    last_name = validate_user_input(
        "Enter the last name (or 0 to exit): ",
        validate_name,
        "Last name is valid",
        "Last name is invalid, try again.\n"
    )
    if last_name is None:
        return  # User exited

    # Validate email
    email = validate_user_input(
        "Enter the email (or 0 to exit): ",
        is_email_valid,
        "Email is valid",
        "Email is invalid, try again.\n"
    )
    if email is None:
        return  # User exited

    # Validate mobile number
    mobile = validate_user_input(
        "Enter the mobile number (or 0 to exit): ",
        is_mobile_valid,
        "Mobile number is valid",
        "Mobile number is invalid, try again.\n"
    )
    if mobile is None:
        return  # User exited
    
    # Validate password
    password = validate_user_input(
        "Enter the password (at least 8 characters long, or 0 to exit): ",
        is_password_valid,
        "Password is valid",
        "Password is invalid, must be at least 8 characters long and 1 upper case char, try again.\n"
    )
    if password is None:
        return  # User exited

    # All inputs are valid
    print("\nRegistration Successful!")
    print(f"Name: {first_name} {last_name}")
    print(f"Email: {email}")
    print(f"Mobile: {mobile}")
    print(f"Password: {password}")

if __name__=="__main__":
    main()