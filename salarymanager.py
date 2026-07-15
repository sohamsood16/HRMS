
class SalaryManager:
    def __init__(self):
        self.salaries = {}   # stores employee_id : salary

    def add_salary(self, emp_id, salary):
        self.salaries[emp_id] = salary

    def get_salary(self, emp_id):
        if emp_id in self.salaries:
            return self.salaries[emp_id]
        return "Employee not found"

    def update_salary(self, emp_id, new_salary):
        if emp_id in self.salaries:
            self.salaries[emp_id] = new_salary
            return "Updated"
        return "Employee not found"

    def remove_salary(self, emp_id):
        if emp_id in self.salaries:
            del self.salaries[emp_id]
            return "Removed"
        return "Employee not found"

    def show_all(self):
        return self.salaries


# ----------- simple demo -----------

manager = SalaryManager()

manager.add_salary("E101", 30000)
manager.add_salary("E102", 40000)

print(manager.show_all())

print(manager.get_salary("E101"))

print(manager.update_salary("E101", 35000))

print(manager.remove_salary("E102"))

print(manager.show_all())
