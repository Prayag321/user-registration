"""
@Author: Prayag Bhoir
@Date: 19-08-2024
@Last Modified by: Prayag Bhoir
@Last Modified time: 20-08-2024
@Title : Python programs for test case
"""
import unittest
from user_registration import validate_name, is_email_valid, is_mobile_valid, is_password_valid

class TestUserRegistration(unittest.TestCase):
    def test_validate_name(self):
        # Valid names
        self.assertTrue(validate_name('Prayag'))
        self.assertTrue(validate_name('Deven'))
        self.assertTrue(validate_name('Ayu'))

        # Invalid names
        self.assertFalse(validate_name('prayag'))
        self.assertFalse(validate_name('Deven123'))
        self.assertFalse(validate_name('Ay'))

    def test_is_email_valid(self):
        # Valid emails
        self.assertTrue(is_email_valid('prayag@gmail.com'))
        self.assertTrue(is_email_valid('abc.xyz@bl.co'))
        self.assertTrue(is_email_valid('abc@bl.co.in'))
        self.assertTrue(is_email_valid('abc@gmail.com.com'))

        # Invalid emails
        self.assertFalse(is_email_valid('abc@bl'))
        self.assertFalse(is_email_valid('abc@bl.c'))
        self.assertFalse(is_email_valid('abc@bl.corp'))
        self.assertFalse(is_email_valid('abc@gmail.com.1a'))

    def test_is_mobile_valid(self):
        # Valid mobile numbers
        self.assertTrue(is_mobile_valid('91 9919819801'))
        self.assertTrue(is_mobile_valid('44 1234567890'))
        self.assertTrue(is_mobile_valid('12 2345678901'))

        # Invalid mobile numbers
        self.assertFalse(is_mobile_valid('91991981980'))  
        self.assertFalse(is_mobile_valid('91 99198198'))   
        self.assertFalse(is_mobile_valid('91 109919819801'))  

    def test_is_password_valid(self):
        # Valid passwords
        self.assertTrue(is_password_valid('Password123@'))  # Valid: 8+ chars, 1+ uppercase, 1+ digit, exact 1 special char
        self.assertTrue(is_password_valid('A1b2c3d4EZ!'))     # 8+ chars , 1 upper char, 1 digit ,exact 1 special char

        # Invalid passwords
        self.assertFalse(is_password_valid('password123'))  # No uppercase letter
        self.assertFalse(is_password_valid('Passwrd'))      # Less than 8 chars, no digit
        self.assertFalse(is_password_valid('Password'))     # no number
        self.assertFalse(is_password_valid('12345678'))     # No uppercase letter


if __name__=="__main__":
    unittest.main()

    
    