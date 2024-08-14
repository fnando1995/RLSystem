import os

def generate_report(ids,report_filepath):
    """
    Read the report files of each employee_id and rewrites to the 
    validation report file.
    """
    # delete report if already exists
    if os.path.exists(report_filepath):
        os.remove(report_filepath)
    # iterate over the employee_ids
    for employee_id in ids:
        # generates the employee report
        employee_report_filepath = os.path.join(os.path.dirname(report_filepath),f'{employee_id}.txt')
        # read all the lines in employee report
        with open(employee_report_filepath) as f:
            lines = f.readlines()
        # rewrites to the report file all the lines of the employee report
        with open(report_filepath,"a") as f:
            for line in lines:
                f.write(line)
        # delete employee report
        os.remove(employee_report_filepath)