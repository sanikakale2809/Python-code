# Create employee.py containing an Employee class. Import it into main.py and create three employee objects.

class Employee:
    def __init__(self, name, emp_id, department):
        """Initializes the employee attributes."""
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        """Prints the employee's details."""
        print(f"ID: {self.emp_id}")
        print(f"Name:{self.name}")
        print(f"Department:{self.department}")
