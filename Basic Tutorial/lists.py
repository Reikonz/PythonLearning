# python can use lists as a 1D array

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

# accessing out of bounds raises an exception

mylist = [1,2,3]
print(mylist[10])