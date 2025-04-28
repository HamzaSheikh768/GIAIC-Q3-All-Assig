# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a 
# reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

#____________________________ Example usage
emp = Employee("Alice")
dept = Department("HR", emp)
print(f"Department: {dept.name}, Employee: {dept.employee.name}")