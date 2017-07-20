# String concatenation using join() command is more efficient for concatenating larger strings than using the
# '+' sign.
import math

colors = ';'.join(['#fff000', '#cffffd', '#ff5959'])
print(colors)
print(colors.split(';'))

# Without an argument, split() divides on whitespace
# joining on an empty separator is an important, and fast way of concatenating a collection of strings

x = ''.join(['New', 'Zea', 'Land'])
print(x)

# partition() method divides thg string into three around a separator: prefix, separator, suffix.

print("unforgettable".partition("forget"))

# tuple unpacking is useful to destructure the result from a partition.
departure, separator, arrival = "New Delhi:Mumbai".partition(":")
print(departure)
print(arrival)

# format() is used to insert values into strings
print("The age of {0} is {1}".format("Jimmy", 24))
print("The age of {0} is {1}. {0}'s birthday is on {2}".format("Caramel", 23, "January 1, 1994"))
print("The movie {} was released in {}".format("Dunkirk", 2017))

# The last example (number 3) can only be used if none of the format arguments
# are to be repeated, and only used exactly once.
# Also, named fields are matched with keyword arguments.

print("Current position {latitude} {longitude}".format(latitude='60N', longitude='5E'))
pos = (65.4, 23.1, 82.2) # tuple
print("Galactic position x={pos[0]} y{pos[1]} z={pos[2]}".format(pos=pos))

# Access sttributes using dot in the replacement field i.e., within { }
print("Math constants: pi={m.pi} e={m.e}".format(m=math))
print("Math constants: pi={m.pi:.3f} e={m.e:.3f}".format(m=math))

# More str commands below
print(help(str))