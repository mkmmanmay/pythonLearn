s = "show how to index into sequences".split()
print(s)

#  Slicing extracts parts of a list
#  slice = seq[start:stop]
print(s[1:4])
print(s[3:])  # slices all elements from 3 index to the last.
print(s[:3])  # slices all elements from the first to 2 (not including the index given.

#  slicing all elements by omitting both start and end indices essentially gives us a copy of the list.

full_slice = s[:]
print(full_slice is s)
print(full_slice == s)

# there are other ways to copy a list, too. Like, using the copy() method, or the list(list_to_copy_from) method.
u = s.copy()
print(u)
v = list(s)
print(v)