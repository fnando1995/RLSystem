# RLSystem

### Objective:

Create a rule-based system for managing and validating a simplified employee scheduling system.
This assignment will test your ability to implement business rules, handle data processing, and
demonstrate your understanding of Python.

### Requirements:

Data Input:
- Create a CSV file named schedules.csv with the following columns (see a sample attached for your reference):
    - EmployeeID (integer)
    - Name (string)
    - Day (string, e.g., "Monday", "Tuesday", etc.)
    - Shift (string, e.g., "Morning", "Afternoon", "Night")
- Rules:
    - Each employee can only work one shift per day.
    - Employees cannot work more than 5 days in a week.
    - The shift "Night" cannot be assigned to an employee on two consecutive days.
    - Employees with the same EmployeeID should have consistent Name values.
- Tasks:
    - Load Data: Write a function to load the schedule data from the schedules.csv file.
    - Validate Rules:
        - Implement functions to validate each of the rules mentioned above.
        - If a rule is violated, the function should return a descriptive error message.
    - Generate Report:
        - Write a function to generate a validation report summarizing all rule violations for each employee.
        - The report should be saved to a file named validation_report.txt.
- Output:
    - Validation_report.txt should list any rule violations with a clear explanation.
    - Example format:
        EmployeeID: 101, Name: John Doe 
        - Worked more than one shift on Monday.
        - Worked more than 5 days in the week.
        EmployeeID: 102, Name: Jane Smith
        - Worked the night shift on both Monday and Tuesday

### Installation

- Clone repository
- (optional) create and activate python virtual environment
    ```
    python3 -m venv env
    source env/bin/activate
    ```
- Install requirements
    ```
    pip install -r requirements
    ```

### Functionality

To execute the app for validate the schedules you must execute the python file `app.py`:

To check on argument options you can use 
```
python app.py --help

options:
  -h, --help       show this help message and exit
  --file FILE      filepath of the csv schedule file
  --report REPORT  filepath of the validation file
```

#### DEMO

```
python app.py --file data/schedules.csv --report data/validation_report.txt
```

```
EmployeeID: 101, Name: John Doe
- Worked more than one shift on Monday
- Worked more than 5 days in the week.
- Worked the night shift on both Tuesday and Wednesday.
- Worked the night shift on both Wednesday and Thursday.
- Worked the night shift on both Thursday and Friday.
- Worked the night shift on both Friday and Saturday.
EmployeeID: 102, Name: Jane Smith
- Worked the night shift on both Monday and Tuesday.

```

### Notes

- The app has default arguments.
    - --file = 'data/schedules.csv'
    - --report = 'data/validation_report.txt'

- If the rule #4 is broken (Employees with the same EmployeeID should have consistent Name values.), the execution will stop. Having a single id with different names in the csv should be fixed manually to retry.
    - ```
        python app.py --file data/schedules-error.csv --report data/validation_report.txt
        
        You are trying to name 101 as Jane Smith, but 101 already has name: John Doe. Check line #7 in csv.
      ``` 
- You can also check on an extended schedule file to test, named `schedules-extended.csv`. Result:

```
EmployeeID: 101, Name: John Doe
- Worked more than one shift on Monday
- Worked more than 5 days in the week.
- Worked the night shift on both Tuesday and Wednesday.
- Worked the night shift on both Wednesday and Thursday.
- Worked the night shift on both Thursday and Friday.
- Worked the night shift on both Friday and Saturday.
EmployeeID: 102, Name: Jane Smith
- Worked the night shift on both Monday and Tuesday.
EmployeeID: 103, Name: Emmanuel moran
EmployeeID: 104, Name: Andrea Boscan
- Worked more than one shift on Tuesday
- Worked the night shift on both Saturday and Sunday.

```