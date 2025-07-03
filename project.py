# pylint: disable=unnecessary-newline
"""Project team member details module."""
# pylint: disable=too-few-public-methods

#imprting all functions from Emp class
from func import  emp1, emp,emp3,emp4

class Project:
    """ A class reprosents to project team mebers with name, age, salary, and job title."""

    @staticmethod
    def order_project(member):
        """ A class reprosents to project team mebers with name, age, salary, and job title."""
        print(f"Order team member details: {member.name}, {member.age}, {member.salary}, {member.job}")
    @staticmethod
    def inventory(member):
        """ A class reprosents to project team mebers with name, age, salary, and job title."""
        print(f"Inventory team member details: {member.name}, {member.age}, {member.salary}, {member.job}")
# Calling the order_project method with emp1 and emp
# This will print the details of the project team member emp1
order_d1 = Project.order_project(emp1)  # pylint: disable=invalid-name
order_t1=Project.order_project(emp3)# pylint: disable=invalid-name
inventory_d1=Project.inventory(emp)# pylint: disable=invalid-name   
inventory_t1=Project.inventory(emp4) # pylint: disable=invalid-name
