class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname  


class SalaryEmployee(Employee): 
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_salary(self):
        # Weekly salary
        return self.salary / 52


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
    
    def calculate_salary(self):
        return self.weekly_hours * self.hourly_rate
    

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, commission_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.commission_rate = commission_rate

    def calculate_salary(self):
        regular_salary = super().calculate_salary() 
        total_commission = self.sales_num * self.commission_rate
        return regular_salary + total_commission
