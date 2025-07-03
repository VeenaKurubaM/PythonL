"""This module defines an Emp class and demonstrates how to create and display employee details."""
# pylint: disable=too-few-public-methods
class Emp:
    """A class representing an employee with name, age, salary, and job title."""
    d_count=0
    t_count=0
    #function employee
    def __init__(self, name, age, salary, job):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job


emp = Emp('seena', 25, 25000, 'QA')
emp1 = Emp('rita', 30, 30000, 'Dev')
emp3 = Emp('deena', 25, 25000, 'QA')
emp4 = Emp('meeta', 30, 30000, 'Dev')
print(emp.name, emp.age, emp.salary, emp.job)
print(emp1.name, emp1.age, emp1.salary, emp1.job)



#function to add teams
def add_dev_teams(dev_team):
    """Adding dev team members"""
    if dev_team.job=='Dev':
        Emp.d_count=Emp.d_count+1
        print(f"Developer count: {Emp.d_count}")
        print(f"Develpers details:{dev_team.name}, {dev_team.age}, {dev_team.salary}, {dev_team.job}") 

    else:
        Emp.t_count=Emp.t_count+1
        print(f"total testers{Emp.t_count}")
        print(f"Testers details:{dev_team.name}, {dev_team.age}, {dev_team.salary}, {dev_team.job}") 

    return Emp.d_count, Emp.t_count
        
devt=add_dev_teams(emp1)
testt=add_dev_teams(emp)
devt1=add_dev_teams(emp4)
testt2=add_dev_teams(emp3)

#employee_details(emp1)
print(f"total developers:{Emp.d_count},total esters:{Emp.t_count}")
