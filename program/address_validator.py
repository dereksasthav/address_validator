from typing import List 
import requests 

class address:

    def __init__(self, street, city, postal_code, country = 'US'):
        self.street = street 
        self.city = city 
        self.postal_code = postal_code 
        self.country = country
        self.valid_address = None

    def __parse_result(api_result: str) --> str:
        """
        api_result: json object from API
        output: string of address or "Invalid Address" result
        """



    def validate_address(self):
        """
        Purpose: make API call to address validator website and return result
        Output: JSON result from API
        """
        pass






api_key = 'av-3e87cf5eb3fafa129cbe67cf7b88c283'

"""
File Structure Needed:

empora_interview/config.yml
empora_interview/readme.md
empora_interview/requirements.txt
empora_interview/setup.py
empora_interview/address_validator/__init__.py
empora_interview/address_validator/__main__.py
empora_interview/address_validator/main.py # this loads the config and passes to validator class
empora_interview/address_validator/validator.py # this loads a CSV file and determines if it's valid
empora_interview/address_validator/address.py # class file for address (needs to be passed API key)
empora_interview/address_validator/utils.py # need to be able to read config, and read html request
empora_interview/tests/address_tests.py # test a few addresses
empora_interview/tests/validator_tests.py # see how it handles invalid files
empora_interview/tests/utils_tests.py # test any utils

"""
