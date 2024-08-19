import unittest
from user_registration import validate_name

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

if __name__=="__main__":
    unittest.main()

    
    