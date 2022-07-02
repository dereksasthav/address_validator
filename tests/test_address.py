from this import s
import unittest 
from unittest.mock import patch
from program import address as a
from program.utils import get_config

class TestAddress(unittest.TestCase):

    def setUp(self) -> None:
        
        self.cfg = get_config()
        self.street1 = '100 Derek Street'
        self.city1 = 'Chicago'
        self.zip1 = '60657'

        self.tst1 = a.Address(self.street1,self.city1, self.zip1)
        self.ref_url1 = self.cfg['api']['api_url'].format(self.street1, self.city1, self.zip1, self.cfg['api']['api_key'])

        self.street2 = '123 e Maine Street'
        self.city2 = 'Columbus'
        self.zip2 = '43215'

        self.tst2 = a.Address(self.street2,self.city2, self.zip2)

    def test_init(self):
        
        print('test_init')

        with self.assertRaises(ValueError):
            tst1 = a.Address(self.street1,self.city1, 5)
        
        with self.assertRaises(ValueError):
            tst2 = a.Address(self.street1, None, self.zip1)
        
        with self.assertRaises(ValueError):
            tst3 = a.Address([self.street1],self.city1, self.zip1)

    
    def test_construct_url(self):

        print('test_construct_url')

        url1 = self.tst1.construct_url()
        self.assertEqual(url1, self.ref_url1)


    def test_get_api_response(self):

        print('test_get_api_response')

        with patch('program.address.requests.get') as mocked_get:
            mocked_get.return_value.ok = True 
            mocked_get.return_value.text = 'Success'

            validated_address = self.tst1.get_api_response()
            mocked_get.assert_called_with(self.ref_url1)
            self.assertEqual(validated_address, 'Success')


    def test_return_valid_address(self):

        print('test_return_valid_address')
        self.tst1.get_api_response()
        self.assertEqual(self.tst1.return_valid_address(), 'Invalid Address')

        self.tst2.get_api_response()
        tst2_address = self.tst2.return_valid_address()
        self.assertEqual(tst2_address, '123 E Main St, Columbus, 43215-5207')
    
        
if __name__ == '__main__':
    unittest.main()
    

"""
{'status': 'SUSPECT', 'ratelimit_remain': 97, 'ratelimit_seconds': 225, 'cost': 1.5, 'formattedaddress': '123 E Main St,Columbus OH 43215-5207', 'addressline1': '123 E Main St', 'addresslinelast': 'Columbus OH 43215-5207', 'street': 'E Main St', 'streetnumber': '123', 'postalcode': '43215-5207', 'city': 'Columbus', 'state': 'OH', 'country': 'US', 'county': 'Franklin', 'diagnostics': 'ward mult', 'type': 'S', 'latitude': 39.9563931, 'longitude': -82.9960062}
123 E Main St, Columbus, 43215-5207
{'status': 'INVALID', 'ratelimit_remain': 96, 'ratelimit_seconds': 224, 'cost': 1.5, 'formattedaddress': '1 Empora St,Title 11111', 'addressline1': '1 Empora St', 'addresslinelast': 'Title 11111', 'street': 'Empora St', 'streetnumber': '1', 'postalcode': '11111', 'city': 'Title', 'country': 'US'}
"""