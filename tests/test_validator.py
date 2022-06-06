import unittest 
from program import validator as v


class TestValidator(unittest.TestCase):
        
    def test_init(self):
        """
        
        """
        print('test_init')
        
        with self.assertRaises(FileNotFoundError):
            tst1 = v.Validator("wrongfile.xlsx")
            
        with self.assertRaises(ValueError):
            tst2 = v.Validator("./data/test1.xlsx")

    def test_load_data(self):

        """
        Purpose: ensure data is loaded into list form properly
        """
        print('test_load_data')
        
        # test 1: check row counts and values
        tst1 = v.Validator("./data/test1.csv")
        tst1.load_data()
        self.assertEqual(tst1.lineCount,2)
        self.assertEqual(tst1.inputData,[['Street Address', 'City', 'Postal Code'],['123 e Maine Street','Columbus','43215'], ['1 Empora St','Title','11111']])               
        
        # test 2: should fail because of no valid data
        tst2 = v.Validator("./data/test2.csv")
        self.assertEqual(tst2.lineCount, 0)
        with self.assertRaises(ValueError):
            tst2.load_data()
            
        

if __name__ == '__main__':
    unittest.main()