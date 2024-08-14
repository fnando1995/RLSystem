from loader import get_employees
from rls_rules import validate_rules
from report import generate_report
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(
                    prog='Rule Based System for Schedule',
                    description='This systems helps to validate all rules for schedule creation.')
    parser.add_argument('--file', type=str, default='data/schedules.csv',
                        help='filepath of the csv schedule file')
    parser.add_argument('--report', type=str, default='data/validation_report.txt',
                        help='filepath of the validation file')
    return parser.parse_args()
    
if __name__ == "__main__":
    # Get the arguments from console
    args = get_arguments()
    
    try:
        # load the data from the csv
        data_loaded = get_employees(args.file)
        # Validate all the rules
        validate_rules(data_loaded,args.report)
        # Generates the final report
        generate_report(data_loaded.keys(),args.report)
    except NameError as e:
        print(e)
    
    