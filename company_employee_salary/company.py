from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees:")
        for i in self.employees:
            print(f"{i.fname} {i.lname}, Weekly Pay: {i.calculate_salary():.2f}")
        print("--------------------")
    
    def pay_employees(self):
        print("Paying Employees:")
        for i in self.employees:
            print(f"Paying {i.fname} {i.lname}: {i.calculate_salary():.2f} per week")
        print("--------------------")

def main():
    my_company = Company()
    emp1 = SalaryEmployee("Alice", "Hess", 50000)
    emp2 = HourlyEmployee("Bob", "Marley", 25, 50)
    emp3 = CommissionEmployee("Alice", "Borderland", 60000, 50, 20)

    my_company.add_employee(emp1)
    my_company.add_employee(emp2)
    my_company.add_employee(emp3)

    my_company.display_employees()
    my_company.pay_employees()

if __name__ == "__main__":
    main()

            
