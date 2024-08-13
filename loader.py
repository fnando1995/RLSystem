import csv

def load_data(file_path):
    """
    This functions read a csv an return a list of dictionaries
    Args:
        file_path <str> File path of the CSV file
    """
    # Read file and read as csv
    if not file_path.endswith(".csv"):
        raise TypeError("Only csv files allowed.")
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def get_employees(file_path):
    """
    This functions transforms a csv file to a dictionary of the employees with the id, name and shifts.
    Args:
        file_path <str> File path of the CSV file
    """
    # Read records
    records = load_data(file_path)

    # Define the list of all weekdays
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    # Initialize an empty dictionary to hold the transformed data
    transformed_data = {}
    
    # Iterate through each record in the list
    for record in records:
        emp_id  = record["EmployeeID"]#f'e{record["EmployeeID"]}'
        name    = record['Name']
        day     = record['Day'].lower()  # Convert day to lowercase
        shift   = record['Shift']

        # Check if the employee ID already exists in the transformed_data dictionary
        if emp_id not in transformed_data:
            # Add a new entry for the employee
            #
            transformed_data[emp_id] = {
                                                'name': name,
                                                'shifts': {day: [''] for day in week_days}
                                            }

        # Append the current shift to the list for the given day
        transformed_data[emp_id]['shifts'][day].append(shift)
        if '' in transformed_data[emp_id]['shifts'][day]:
            transformed_data[emp_id]['shifts'][day].remove('')

    return transformed_data