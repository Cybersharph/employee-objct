# Import the Employee class.
# Class comes from the employee module.
from employee import Employee

# Create a list of employees.
# Each employee is an instance of the Employee class.
employees = [
    Employee("Muyivu Shafiq", "3341", "IT", "Security Auditor", "100000", "cybersharph@gmail.com" , "5"),
    Employee("Sarah Johnson", "2234", "Finance", "Financial Analyst", "95000", "sarah.johnson@example.com" , "3"),
    Employee("James Williams", "4455", "IT", "Software Developer", "105000", "james.williams@company.com", "11"),
    Employee("Emma Brown", "6677", "Marketing", "Marketing Coordinator", "88000", "emma.brown@company.com", "2"),
    Employee("Liam Smith", "8899", "Sales", "Sales Executive", "102000", "liam.smith@sales.com", "6"),
    Employee("Olivia Davis", "1122", "Operations", "Operations Manager", "110000", "olivia.davis@company.com", "12"),
    Employee("Noah Miller", "3344", "HR", "Recruitment Specialist", "97000", "noah.miller@hr.com", "1"),
    Employee("Ava Thompson", "5566", "IT", "Network Engineer", "108000", "ava.thompson@tech.com", "8"),
    Employee("William Anderson", "7788", "Logistics", "Logistics Supervisor", "95000", "william.anderson@logistics.com", "15"),
]

# Loop through the list of employee instances.
for employee in employees:
    employee.employee_info()