#  a method is different from a function in a sense that it can
#  only be called from within a class by the help of an object
class Human():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak_name(self):
        print("My name is ", self.name)

    def speak(self, text):
        print(text)

    def perform_math_task(self, math_operation, *args):
        print("{} performed a math operation, and the result was: {}".format(self.name, math_operation(*args)))


will = Human("William", "Male")

print(will.name)
print(will.gender)

will.speak_name()
will.speak("I love programming.")


#  The above wouldn't work if you remove 'self' from the method "speak()".
#  Self is an implied (implicit) argument which has to be given to a method.
#  If you remove self as an argument from the method, and try running above code
#  you will get an error like below.
#  will.speak("I love programming.")
#  TypeError: speak() takes 1 positional argument but 2 were given

def add(a, b, c, d):
    return a + b + c + d
ryan = Human("Ryan Stevens", "Male")
ryan.perform_math_task(add, 34, 6, 4, 10)

