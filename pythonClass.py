class Employee:

    raise_amount = 1.04
    #  here raise_amount is a class variable, can be shared among all the methods declared between the classes.
    #  For instance if we need to use '1.04' as a number within several of our methods declared in the class, but when
    #  for some reason we need to update that amount, we would have to individually go to every method where the number
    #  is used, and updated it. But if we declare that number with a class variable, we only need to update it in that
    #  one declaration. For example, if we wanted to give a 4% bonus to employees here, and say there are 3 methods
    #  that need this info; instead of using that 4% in 3 methods, we can declare it as a class variable, and when the
    #  time should come that we need to update the bonus % from 4 to 5, we would only have to update it at one place.
    #  NOTE: Class variables can only be access through the class, or an instance of it. E
    #  Example: Employee.raise_amount or self.raise_amount/emp_1.raise_amount/emp_2.raise_amount

    def __init__ (self, first, last, pay):
        #  __init__ method is basically a constructor.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def display_full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

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

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

Employee.raise_amount = 1.05

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# Above prints 1.05, 1.05, 1.05 respectively; because setting the raise_amount as 1.05 using the class means, its
# 1.05 for its instances as well, since emp_1.raise_amount means it accesses the class variable raise_amount through
# the instance, and the instance itself doesn't have the variable in it. You could check by printing (emp_1.__dict__)
# and compare with Employee.__dict__

emp_1.raise_amount = 1.08
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# this prints 1.05, 1.08, 1.05 respectively. If we are setting raise_amount a value through the class instance,
# the value only changes for that particular instance, and not the whole class.
# If we do print(emp_1.__dict__), it will show the 'raise_amount': 1.08 in it.

