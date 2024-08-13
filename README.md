# RLSystem

### Objective:

Create a rule-based system for managing and validating a simplified employee scheduling system.
This assignment will test your ability to implement business rules, handle data processing, and
demonstrate your understanding of Python.

### Requirements:

Data Input:
- Create a CSV file named schedules.csv with the following columns (see a sample
attached for your reference):
    - EmployeeID (integer)
    - Name (string)
    - Day (string, e.g., "Monday", "Tuesday", etc.)
    - Shift (string, e.g., "Morning", "Afternoon", "Night")
- Rules:
- Each employee can only work one shift per day.
oEmployees cannot work more than 5 days in a week.
oThe shift "Night" cannot be assigned to an employee on two consecutive days.
oEmployees with the same EmployeeID should have consistent Name values.
3. Tasks:
o
Load Data:
▪
o
o
Write a function to load the schedule data from the schedules.csv file.
Validate Rules:
▪Implement functions to validate each of the rules mentioned above.
▪If a rule is violated, the function should return a descriptive error message.
Generate Report:
▪Write a function to generate a validation report summarizing all rule
violations for each employee.
▪The report should be saved to a file named validation_report.txt.
4. Output:
ovalidation_report.txt should list any rule violations with a clear explanation.
oExample format:
EmployeeID: 101, Name: John Doe