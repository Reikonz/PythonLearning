# python boolean conditionals

x = 2
print(x == 2)
print(x == 3)
print(x < 3)

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

#is operator
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

#not operator
print(not False)
print((not False) == (False))