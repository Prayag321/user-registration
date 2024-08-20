"""
@Author: Prayag Bhoir
@Date: 19-08-2024
@Last Modified by: Prayag Bhoir
@Last Modified time: 19-08-2024
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


def main():
    while True:
        first_name = input("Enter the first name (or 0 to exit): ")
        if first_name == "0":
            break
        if validate_name(first_name):
            print("First name is valid")
        else:
            print("First name is invalid, try again.\n")
            continue
        
        last_name = input("Enter the last name (or 0 to exit): ")
        if last_name == "0":
            break
        if validate_name(last_name):
            print("Last name is valid")
        else:
            print("Last name is invalid, try again.\n")
            continue
        
        email = input("Enter the email (or 0 to exit): ")
        if email == "0":
            break
        if is_email_valid(email):
            print("Email is valid")
            break
        else:
            print("Email is invalid, try again.\n")


if __name__=="__main__":
    main()