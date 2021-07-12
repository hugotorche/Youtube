
# Python Object-Oriented Programming

# Tutorial 1: Classes and Instances

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Hugo', 'Torche', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1.email)
print(emp_2.email)

print()

print(emp_1.fullname())
print(Employee.fullname(emp_2))
