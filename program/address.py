from program.utils import get_config
import requests
from typing import Dict

class Address:

    def __init__(self, street: str, city: str, postal_code: str):
        """
        Purpose: store street, city, postal_code of a given address
        """

        if not isinstance(street, str):
            raise ValueError("Input street must be type string")

        if not isinstance(city, str):
            raise ValueError("Input city must be type string") 
        
        if not (isinstance(postal_code, str) or (isinstance(postal_code, int) and len(str(postal_code))==5)):
            raise ValueError("All inputs to Address must be type string or int")

        self.street = street 
        self.city = city 
        self.postal_code = str(postal_code)
        self.valid_address = None 
        self.api_response = None

    def __repr__(self):
        return '{}, {}, {}'.format(self.street, self.city, self.postal_code)

    def construct_url(self) -> str:
        """
        Fill in API call URL with street, city, postal code, and API key

        Output (str): full URL to be used in GET request
        """

        cfg = get_config()
        api_key = cfg['api']['api_key']
        result_url = cfg['api']['api_url'].format(self.street, self.city, self.postal_code, api_key)

        return result_url

    def get_api_response(self):
        """
        Purpose: make API call to validate address
        """

        # construct URL, need to load from config
        url = self.construct_url()

        # make API GET call
        response = requests.get(url)
        self.api_response = response.json()
        
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


    def return_valid_address(self) -> str:
        """
        Purpose: parse API response from address validator website

        Output: str with API response text
        """
        if self.api_response != None:
            print(self.api_response)

            # parse the API response
            if self.api_response['status'] in ['VALID', 'SUSPECT']:
                result = "{} {}, {}, {}".format(self.api_response['streetnumber'],
                    self.api_response['street'],
                    self.api_response['city'],
                    self.api_response['postalcode'])
                self.valid_address = result
            else:
                self.valid_address = 'Invalid Address' 
                
        return self.valid_address