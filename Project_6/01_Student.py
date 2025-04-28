# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor.
#  Add a method display() that prints student details.

print("Python OOP Assignments Demo")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

#____________________________ Example usage
student = Student("Alice", 85)
student.display()