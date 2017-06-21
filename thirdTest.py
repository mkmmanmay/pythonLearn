#  a method is different from a function in a sense that it can
#  only be called from within a class by the help of an object
class Human():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak_name(self):
        print("My name is ", self.name)

    def speak(text):
        print(text)


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
