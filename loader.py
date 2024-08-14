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
    
    # Initialize an empty dictionary to hold the transformed data
    transformed_data = {}
    
    # Iterate through each record in the list
    for line_number,record in enumerate(records):
        emp_id  = record["EmployeeID"]
        name    = record['Name']
        day     = record['Day']
        shift   = record['Shift']
        
        if emp_id in transformed_data:
            # Check for name consistency
            if transformed_data[emp_id]['name'] != name:
                msg = f"You are trying to name {emp_id} as {name}, but {emp_id} already has name: {transformed_data[emp_id]['name']}. Check line #{line_number+1} in csv."
                raise NameError(msg)
                
            # Append shift to the existing entry
            if day not in transformed_data[emp_id]['shifts']:
                transformed_data[emp_id]['shifts'][day] = [shift]
            else:
                transformed_data[emp_id]['shifts'][day].append(shift)
        else:
            # Add a new entry for the employee
            transformed_data[emp_id] = {
                'name': name,
                'shifts': {day: [shift]}
            }

    return transformed_data