# creating objects in python

# basic class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

# assigning class to object
myobjectx = MyClass()
myobjecty = MyClass()

# accessing object
myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()