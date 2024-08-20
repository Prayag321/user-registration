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
      bool:True if match False otherwise
    """
    pattern = "^[A-Z][A-Za-z]{2,}$"
    return bool(re.match(pattern,name))

def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")

    if validate_name(first_name):
        print("First name is valid")
    else:
        print("First name is invalid")
        
    if validate_name(last_name):
        print("Last name is valid")
    else:
        print("Last name is invalid")
        

if __name__=="__main__":
    main()