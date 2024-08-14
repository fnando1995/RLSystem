from business_rule_engine import RuleParser
import os
import calendar

def rule_one_shift_per_day(employee_data,employee_report_filepath):
    """
    Validates that the employee only works one shift per day
    Args:
        employee_data <dict>: Data of the employee (name and shifts)
        employee_report_filepath <str> filepath to save errors about employee
    """
    def print_error(day,report):
        """
        Function to print errors in the employee report file
        """
        with open(report,"a") as f:
            f.write(f"- Worked more than one shift on {day}\n")
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

def rule_no_more_than_five_days(employee_data,employee_report_filepath):
    """
    Validates that the employee work no more than five days in the week.
    Args:
        employee_data <dict>: Data of the employee (name and shifts)
        employee_report_filepath <str> filepath to save errors about employee
    """
    def print_error(report):
        """
        Function to print errors in the employee report file
        """
        with open(report,"a") as f:
            f.write(f"- Worked more than 5 days in the week.\n")    
    rule = f"""
    rule "five days work max"
    when
        shift > 5 = True
    then
        print_error(report)
    end
    """    
    parser = RuleParser()
    parser.register_function(print_error)
    parser.parsestr(rule)
    # validate
    parser.execute({
        "shift":len(employee_data['shifts'].keys()),
        "report":employee_report_filepath
    })


def rule_nigth_shifts(employee_data,employee_report_filepath):
    """
    Validates that the employee does not work Night shifts two consecutives days.
    Args:
        employee_data <dict>: Data of the employee (name and shifts)
        employee_report_filepath <str> filepath to save errors about employee
    """    
    def print_error(day_1,day_2,report):
        """
        Function to print errors in the employee report file
        """
        with open(report,"a") as f:
            f.write(f"- Worked the night shift on both {day_1} and {day_2}.\n")    
    rule = f"""
    rule "nigth_shifts"
    when
        AND(day_1_shift_nigth = day_2_shift_nigth,day_1_shift_nigth = "Night")
    then
        print_error(day_1,day_2,report)
    end
    """    
    parser = RuleParser()
    parser.register_function(print_error)
    parser.parsestr(rule)
    # validate
    week_days = list(calendar.day_name)
    for idx in range(len(week_days)-1):
        day_1 = week_days[idx]
        day_2 = week_days[idx+1]
        if day_1 in employee_data['shifts'] and day_2 in employee_data['shifts']:
            parser.execute({
                "day_1": day_1,
                "day_2": day_2,
                "day_1_shift_nigth": employee_data['shifts'][day_1][-1],
                "day_2_shift_nigth":employee_data['shifts'][day_2][-1],
                "report":employee_report_filepath
            })



def validate_rules(data,report_filepath):
    """
    This function generalize the RL System and helps to validate all the rules of the system.

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
        # validating rule 2: one shift per dar
        rule_no_more_than_five_days(employee_data,employee_report_filepath)
        # validating rule 3: night shifts
        rule_nigth_shifts(employee_data,employee_report_filepath)