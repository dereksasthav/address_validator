from ast import Add
from os.path import exists 
from csv import reader, writer
from program.address import Address
from program.utils import get_config


class Validator:

    def __init__(self, inputFileName: str):
        """
        inputFileName: string for input CSV file
        """

        if not exists(inputFileName):
            raise FileNotFoundError("File named {} was not found. Please enter a valid filename!".format(inputFileName))

        if not inputFileName.endswith('.csv'):
            raise ValueError("Input Filename needs to end with .csv")
        
        self.inputFileName = inputFileName
        self.inputData = None
        self.lineCount = 0
        self.outputData = []

    def load_data(self):
        """
        Purpose: based on input filename, read contents of file into a variable

        Output: list of lists, each element is a row of data from the input file, should be 3 elements each
        """
        result = []
        lineCount = 0
        with open(self.inputFileName) as f:
            csv_reader = reader(f, delimiter=",")
            for row in csv_reader:
                result.append(row)
                lineCount += 1
        
        # first row should be column header: ['Street Address', 'City', 'Postal Code']
        if result[0] != ['Street Address', 'City', 'Postal Code']:
            raise ValueError("Input file has wrong column header")

        # if no data besides header, raise Error
        if lineCount <= 1:
            raise ValueError("Input file has no valid data")

        self.inputData = result
        self.lineCount = max(0,lineCount - 1) # if only header row, return 0

    def validate_data(self) -> str:

        self.outputData = []

        if self.inputData != None and self.lineCount > 0:

            for addr in self.inputData[1:]:

                # create address object
                street, city, postal_code = addr
                add = Address(street, city, postal_code)

                # validate data
                add.get_api_response()
                valid_address = add.return_valid_address()
                self.outputData.append((repr(add), valid_address))
    
    def output_data(self):
        """
        Purpose: write output data to file

        Output a file with the file name defined in config.yml
        """
        cfg = get_config()
        output_filename = cfg['output']['output_file']

        if len(self.outputData) > 0:

            # open the file in the write mode
            with open(output_filename, 'w') as f:

                # create the csv writer
                writer = writer(f)
                
                # write a row to the csv file
                for pre, post in zip(self.inputData[1:], self.outputData):
                    row = pre + ' -> ' + post
                    writer.writerow(row)

    def run(self):
        self.load_data()
        self.validate_data()
        self.output_data()