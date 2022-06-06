


class Address:

    def __init__(self, street, city, postal_code):
        """
        Purpose: store street, city, postal_code of a given address
        """
        self.street = street 
        self.city = city 
        self.postal_code = postal_code
        self.valid_address = None 
        self.is_valid = False 

    def validate_address(self):
        """
        Purpose: make API call to validate address
        """

        # construct URL, need to load from config
        # make API GET call
        # parse API result : helper?
        # store validated address
        # set self variables 