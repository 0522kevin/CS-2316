# 1/31

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_raise(self):
        self.salary *= 1.10

    def __repr__(self):
        return f"Employee: {self.name} makes {round(self.salary,2)}"

    def is_highly_paid(self):
        return self.salary > 8.0

class Manager(Employee):  # Manager inherits from Employee
    
    def __init__(self, name, salary):
        super().__init__(name,salary) # Inherits the attributes
        self.employees = []

    def hire(self, emp):
        self.employees.append(emp)

    def __repr__(self):
        return f"Manager: {self.name} makes {round(self.salary,2)} has {len(self.employees)} workers"

    def is_highly_paid(self):
        return self.salary > 20.0

pablo = Employee("Pablo", 9.75)
print(pablo)
pablo.get_raise()
print(pablo)

melinda = Manager("Melinda", 16.25)
melinda.hire(pablo)
print(melinda)

for e in melinda.employees:
    e.get_raise() # From Employee class
print(pablo)

print(pablo.is_highly_paid()) # True
print(melinda.is_highly_paid()) # False
