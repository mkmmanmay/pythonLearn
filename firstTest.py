print("Hello World")
i = 10
print(i**2)

"""
Multi line comment
is here
"""
stroke = "A frog jumped out to say, \"What do you fear?\" A baffled human replied, \"A talking frog.\"."
print(stroke)

#Getting a character from a string
str1 = "movement"
print(str1[0])

#String slicing
str2 = "pineapple"
ex1 = str2[:3]  #0-2 (excludes last index)
ex2 = str2[2:5]  #2-4 (excludes the last index)
ex3 = str2[3:]  #3-last (includes first index)
print(ex1)
print(ex2)
print(ex3)

#String Methods
string = "escape"
print(len(string))
print(string.__len__())

num = 9
strnumber = str(num)  #str() turns integer/float types into String
print(strnumber)

move = "MovIe"
print(move.lower())
print(move.upper())

# %s operator
city = "Delhi"
country = "India"
print("%s of the country %s is the most polluted city in the World." %(city, country))

# input()
occupation = input("What's your occupation?")
company = input("Which company do you work for?")
print("Your occupation is %s, and you work for %s." %(occupation, company))

# if-else-elif
if 5!=6:
    print("Lmao")
elif 6!=6:
    print("rofl")
else:
    print("pagle")
