#  to define a function, type 'def' followed by the function name.
#  Example below:
import random
from random import *
from math import *


def func1():
    print("Hello World")
func1()


def func2(a):
    return a
func2(10)


def func3(a, b, c):
    d = b * a
    print(c + d)
    print(func2(d))
func3(2, 3, 4)

#  print(random.randint(1,10))
print(randint(19, 59))
print(random())
print(factorial(4))

# absolute function
ex1 = abs(-9)
print(ex1)

# type() function
t1 = type(1)
t2 = type(0.5)
t3 = type("strong")
t4 = type(True)
print(t1, t2, t3, t4)

# max() function; min() works similar to this
m1 = max(1, 14, 13, 21, 1.1)
m2 = max("a", "z", "y")
m3 = max("ax", "ac", "ag")
print(str(m1) + " " + m2 + " " + m3)

# List
list1 = ["egg", "lol", 1, "quick"]
print(list1[3])
#  append()
list1.append("hungry")
print(list1[4])
#  List slicing
slice1 = list1[:2]  # excludes index 2
slice2 = list1[2:4]  # includes index 2 excludes 4
slice3 = list1[1:]  # includes index 1
print(slice1, slice2, slice3)
#  index()
print(list1.index(1))
#  insert()
list1.insert(3, 23)
print(list1)
#  remove()
list1.remove("lol")
print(list1)
#  pop()
eggs = list1.pop(0)  # not giving any index with pop() removes the last element of the list.
print(eggs)
print(list1)
