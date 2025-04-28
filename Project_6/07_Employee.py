# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

#____________________________ Example usage
emp = Employee("Alice", 50000, "123-45-6789")
print(f"Public name: {emp.name}")
print(f"Protected salary: {emp._salary}")
try:
    print(emp.__ssn)
except AttributeError:
    print("Cannot access private variable __ssn directly.")