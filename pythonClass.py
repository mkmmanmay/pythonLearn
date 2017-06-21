class Employee:
    def __init__(self, first, last, pay):
        #  __init__ method is basically a constructor.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def display_full_name(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Manmay", "Mohanty", 50000)
emp_2 = Employee("Test", "User", 40000)  # This declaration basically means emp_2 is an object of class Employee

#  print(emp_1)
#  print(emp_2)

print(emp_1.email)
print(emp_1.display_full_name())
print(Employee.display_full_name(emp_1))

#  NOTE: print(emp_1.display_full_name()) && print(Employee.display_full_name(emp_1)) are basically same thing.
#  But the difference is, in the first code, we don't need to pass any argument with the method, because the instance
#  that is 'emp_1' is passed automatically. But in the second case, we have to give the instance (emp_1) as argument
#  To let the program know which instance to work on.