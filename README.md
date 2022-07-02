# address_validator
Validates input addresses with API and writes validated responses to file

Author: Derek Sasthav

## Setup
This program can be executed in the command line with Python.

First, you must activate a virtual environment and install the proper packages per the requirements.txt file

```
cd filepath/address_validator
python3 -m venv venv
venv\Scripts\activate
```

The API credentials can be configured in the *config.yml* file. This file also allows for configuration of the output file directory. Specifically, you should update the api_key field and the output_file parameter if desired.

## How to Run the Code

Run the command line program with this line:

```
python -m program input_filename.csv
```

The input file must be a valid csv file with the 3 headers: Street Address, City, and Postal Code

## How to Test the Code

To test the code, run the command line code below:

```
python -m unittest
```

## Teardown

Once finished, you can deactivate your virtual environment:

```
deactivate
```


## Key Decisions

1. I decided to create a separate class for the address and validator. This allowed me to more easily test the components of the data load, API call, and the data output. I also thought it would allow for easier extensibility in case we wanted to add more functionality to the API validation at a later date by just updating the address class.

2. To reduce the number of API calls, I tested the validator.validate_data class method with a mock API call. See the method test_address.TestAddress.test_get_api_response

## Future Improvements

1. Right now, the address class returns 3 specific fields to the Validator class when I output the data.Then, the validator class has to parse 3 specific fields before outputting the data. I would rather generalize this so that the Validator class outputs whatever is returned from the Address class

2. I'd like to improve the mock API call testing and add more test cases
