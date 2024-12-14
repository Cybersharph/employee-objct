
# Start of Employee class

class Employee:

    # Constructor method
    def __init__(self, name, identity, department, role, salary, email, years_in_service):
        self.name = name
        self.identity = identity
        self.department = department
        self.role = role
        self.salary = salary
        self.email = email
        self.years_in_service = years_in_service
    
    # Method to display employee information
    def employee_info(self):
        print()
        print(f"Full Names: {self.name}")
        print(f"Employee ID: {self.identity}")
        print(f"Department: {self.department}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        print(f"Email address: {self.email}")
        print(f"Years in service: {self.years_in_service}")
        self.eligible_for_retirement()
        print("*" * 50)
        print()

    # Methond to check if employee is eligible for retirement
    def eligible_for_retirement(self):
        if int(self.years_in_service) >= 10:
            print("Eligible for retirement.")
        else:
            print("Not eligible for retirement.")

# End of Employee class
