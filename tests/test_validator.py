import unittest 
from program import validator as v
import filecmp


class TestValidator(unittest.TestCase):
        
    def test_init(self):
        """
        
        """
        print('test_init')
        
        with self.assertRaises(FileNotFoundError):
            tst1 = v.Validator("wrongfile.xlsx")
            
        with self.assertRaises(ValueError):
            tst2 = v.Validator("./data/test_input1.xlsx")

    def test_load_data(self):

        """
        Purpose: ensure data is loaded into list form properly
        """
        print('test_load_data')
        
        # test 1: check row counts and values
        tst1 = v.Validator("./data/test_input1.csv")
        tst1.load_data()
        self.assertEqual(tst1.lineCount,2)
        self.assertEqual(tst1.inputData,[['Street Address', 'City', 'Postal Code'],['123 e Maine Street','Columbus','43215'], ['1 Empora St','Title','11111']])               
        
        # test 2: should fail because of no valid data
        tst2 = v.Validator("./data/test_input2.csv")
        self.assertEqual(tst2.lineCount, 0)
        with self.assertRaises(ValueError):
            tst2.load_data()

    
    def test_output_data(self):

        """
        Purpose: ensure the output data correctly writes to the output csv file

         Issue:
            Having trouble getting the validator output_data function to not write an extra line at the end of the file
        """
        print('test_output_data')
        
        tst1 = v.Validator("./data/test_input1.csv")
        tst1.outputData = [
            ('123 e Maine Street, Columbus, 43215','123 E Main St, Columbus, 43215-5207' ),
            ('1 Empora St, Title, 11111', 'Invalid Address')
        ]

        tst1.output_data()
        f1 = './data/output.csv' # output file from test
        f2 = './data/test_output1.csv' # file to compare against 
        self.assertTrue(filecmp.cmp(f1,f2))
        

if __name__ == '__main__':
    unittest.main()