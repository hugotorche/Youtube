# 1 Translate Tabs to Spaces (IDE settings)

nums = [11, 30, 44, 54]

for num in nums:
    square = num ** 2
    print(square)

# 2 Don't name a module as a python library
# 3 Don't name a variable as a python function

from math import radians, sin

rds = radians(90)

print(sin(rds))

# 4 Default parameter is applied only once (Use None + if statement)


def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


emps = ['John', 'Jane']

add_employee('Corey')
add_employee('John')
add_employee('Jane')

import time
from datetime import datetime


def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))


display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

# 5 Differences between Python2 and Python3 (zip iterator : use list)

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

identities = list(zip(names, heroes))

print(list(identities))

for identity in identities:
    print('{} is actually {}!'.format(identity[0], identity[1]))

# 6 Using an asterisk when importing modules is a bad practice

from html import escape as h_escape
from glob import escape as g_escape

print(help(h_escape))
print(help(g_escape))
