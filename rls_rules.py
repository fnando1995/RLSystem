from business_rule_engine import RuleParser
import os

def print_error(error,report):
    with open(report,'a') as f:
        f.write(error+'\n')

def rule_one_shift_per_day(employee_data,employee_report_filepath):
    """
    employee_data <dict> {"name":"","shifts":{"monday":["Afternoon"]}}
    employee_report_filepath <str> filepath to save errors about employee
    """
    def print_error(day,report):
        """
        Function to print errors in the employee report file
        """
        with open(report,"a") as f:
            f.write(f"- Worked more than one shift on {day.capitalize()}")

    rule = f"""
    rule "one shift per day"
    when
        shift > 1 = True
    then
        print_error(day,report)
    end
    """    
    parser = RuleParser()
    parser.register_function(print_error)
    parser.parsestr(rule)
    # iter over all days to validate
    for day,shifts in employee_data['shifts'].items():
        parser.execute({
            "day":day,
            "shift":len(shifts),
            "report":employee_report_filepath
        })



def validate_rules(data,report_filepath):
    """
    This function generalize the RL System.
    Args
        data <dict> data about the schedules of the employees to validate in form of a dictionary
    
    Returns

        <dict> Dictionary with the errors per employee schedule

    """
    for employee_id,employee_data in  data.items():
        # validate file of employee
        employee_report_filepath = os.path.join(os.path.dirname(report_filepath),f'{employee_id}.txt')
        if os.path.exists(employee_report_filepath):
            os.remove(employee_report_filepath)
        with open(employee_report_filepath,"a") as f:
            f.write(f"EmployeeID: {employee_id}, Name: {employee_data['name']}\n")
        # validating rule 1: one shift per dar
        rule_one_shift_per_day(employee_data,employee_report_filepath)