class employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def update_empdetails(self):
        self.emp_id = int(self.emp_id + 10)


obj1 = employee(23, "Nithya", 1700)
obj2 = employee(24, "Lakshmi", 2000)

print(obj1.__dict__)
print(obj2.__dict__)
obj2.update_empdetails()
print(obj2.__dict__)
