from os.path import exists 
from csv import reader

class Validator:

    def __init__(self, inputFileName: str):
        """
        inputFileName: string for input CSV file
        """

        if not exists(inputFileName):
            raise FileNotFoundError("File named {} was not found. Please enter a valid filename!")

        if not inputFileName.endswith('.csv'):
            raise ValueError("Input Filename needs to end with .csv")
        
        self.inputFileName = inputFileName
        self.outputFileName = './data/output.csv'
        self.inputData = None
        self.lineCount = 0
        self.outputData = None

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

    def validate_data(self):

        if self.inputData != None and self.lineCount > 0:

            for addr in self.inputData[1:]:

                # create address object
                # validate data
                pass
    