
# Start of Employee class

class Employee:

    # Constructor method
    def __init__(self, name, identity, department, role, salary, email):
        self.name = name
        self.identity = identity
        self.department = department
        self.role = role
        self.salary = salary
        self.email = email
    
    # Method to display employee information
    def employee_info(self):
        print()
        print(f"Full Names: {self.name}")
        print(f"Employee ID: {self.identity}")
        print(f"Department: {self.department}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        print(f"Email address: {self.email}")
        print("*" * 50)
        print()

# End of Employee class
