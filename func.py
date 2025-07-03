"""This module defines an Emp class and demonstrates how to create and display employee details."""
# pylint: disable=too-few-public-methods
class Emp:
    """A class representing an employee with name, age, salary, and job title."""

    #function employee
    def __init__(self, name, age, salary, job):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job


emp = Emp('veena', 25, 25000, 'QA')
emp1 = Emp('sita', 30, 30000, 'Dev')
print(emp.name, emp.age, emp.salary, emp.job)
print(emp1.name, emp1.age, emp1.salary, emp1.job)


#function to print employee details
def employee_details(employee):
    """Prints the details of an employee."""
    print(f"Name:{employee.name},Age:{employee.age},Salary:{employee.salary},Job:{employee.job}")


employee_details(emp)
employee_details(emp1)
