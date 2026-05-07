from pandas import DataFrame

# Required main function
def run(df):

    # Filter IT employees
    it_employees = df[df['Department'] == 'IT'].copy()

    # Average salary of all employees
    avg_salary = df['Salary'].mean()

    # Oldest employee
    oldest_employee = df.loc[df['Age'].idxmax()]

    oldest_name = oldest_employee['Employee_Name']
    oldest_department = oldest_employee['Department']

    # Add new columns
    it_employees['Average_Salary_All_Employees'] = avg_salary
    it_employees['Oldest_Employee_Name'] = oldest_name
    it_employees['Oldest_Employee_Department'] = oldest_department

    return it_employees


# REQUIRED for Tableau Prep
def get_output_schema():

    return DataFrame({
        'Employee_ID': prep_string(),
        'Employee_Name': prep_string(),
        'Department': prep_string(),
        'Age': prep_int(),
        'Salary': prep_decimal(),
        'Average_Salary_All_Employees': prep_decimal(),
        'Oldest_Employee_Name': prep_string(),
        'Oldest_Employee_Department': prep_string()
    })