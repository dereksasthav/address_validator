import sys 
from program.validator import Validator

def main():

    filename = sys.argv[1]
    v = Validator(filename)
    v.run()


if __name__ == '__main__':
    main()