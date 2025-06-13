# Problem 1 - Department Highest Salary (https://leetcode.com/problems/department-highest-salary/ )
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Join Employee and Department Table via Inner Join
    df = employee.merge(department, left_on = 'departmentId', right_on = 'id', how = 'inner')
    # Compute Maximum Salary Per Department
    max_salary = df.groupby('departmentId')['salary'].transform('max')
    # Filter only those rows where salary is equal to max_salary
    df = df[df['salary'] == max_salary]
    # Return final dataframe with renamed columns
    return df[['name_y', 'name_x', 'salary']].rename(columns = {'name_y' : 'Department', 'name_x' : 'Employee'})