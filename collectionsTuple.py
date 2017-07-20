#  Objects once added into a tuple can't be removed, changed. And, also, new elements cannot be added.
# Tuples are written with parenthesis.

tu = ('Norway', 0.5, 'Hungary', 3)
print(tu[0])
print(len(tu))

for item in tu:
    print(item)

print(tu + (23, 'xyz'))
print(tu*3)

# Since tuples can contain any object, it is possible to have nested tuples
a = (('xyz', 'pqr'), (123, 'People'), ('dirt', 8.6))
print(a[2])
print(a[1][1])

# Sometimes we need to make a tuple with single object; in that case, we can't write as say: b = (39)
# Here Python will pass it as type integer. In this case, we include a trailing comma. Example below:
h = (31)
print(type(h))
k = (341,)
print(type(k))

# For empty tuple, use empty parenthesis
# tuples are useful for multiple return values. We can assigned multiple return values to references as below:
def minmax(items):
    return min(items), max(items)

lower, upper = minmax([34, 31, 55, 123, 12, 155, 89])
print(lower)
print(upper)

(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a)
print(b)
print(c)
print(d)

a = 'jelly'
b = 'movie'
a, b = b, a
print(a)
print(b)

# WE can use tuple constructor to create tuples from other iterable series of objects

x = tuple([560, 1120, 1234, 4342])
print(x)

print(tuple("Carmen"))

# The 'in' and 'not in' operators can be used with tuples - and other collection types -
# for membership testing

w = 5 in (3, 4, 6, 2, 10)
print(w)

y = 5 not in (3, 4, 6, 2, 10)
print(y)