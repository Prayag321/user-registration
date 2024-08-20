import unittest
from user_registration import validate_name, is_email_valid

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

        # Valid emails
        self.assertTrue(is_email_valid('prayag@gmail.com'))
        self.assertTrue(is_email_valid('abc.xyz@bl.co'))
        self.assertTrue(is_email_valid('abc@bl.co.in'))

        # Invalid emails
        self.assertFalse(is_email_valid('abc@bl'))
        self.assertFalse(is_email_valid('abc@bl.c'))
        self.assertFalse(is_email_valid('abc@bl.corp'))


if __name__=="__main__":
    unittest.main()

    
    