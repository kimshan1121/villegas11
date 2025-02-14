class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increased by ${amount}. New salary: ${self.salary}")

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: ${self.salary}")

# Create an employee and give a raise
employee = Employee("Ezra Silvestrece", "Marketing Manager", 10000)
employee.display_employee()
employee.give_raise(3000)
employee.display_employee()