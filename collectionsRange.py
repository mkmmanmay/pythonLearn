print(range(5))
for i in range(5):
    print(i)

p = list(range(0, 5))
print(p)

q = list(range(5, 10))
print(q)

r = list(range(0, 10, 2))
print(r)

#  range(5) --- 5 is the stop argument
#  range(5, 10) --- 5 is start, 10 is stop, although the values move from 5 to 10 as 5,6,7,8,9
#  range(10, 20, 2) --- 10 is start, 20 is stop, and 2 is the step by which the range will increment at every loop
#  like, 10, 12, 14, 16, 18
t = [6, 23, 213, 1242, 12213]
for x in enumerate(t):
    print(x)

for i, v in enumerate(t):
    print("i={}, v={}".format(i, v))