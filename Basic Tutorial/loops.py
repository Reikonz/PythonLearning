#********for loops
primes = [2,3,5,7]
for prime in primes:
    print(prime)

#prints out 0,1,2,3,4
for x in range(5):
    print(x)

#prints out 3,4,5
for x in range(3,6):
    print(x)

#prints out 3,5,7
for x in range(3,8,2):
    print(x)

#********while loops
count = 0
while count < 5:
    print(count)
    count += 1

#break and continue statements
# prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

#*******else with loops
count = 0
# prints out 0,1,2,3,4 and then prints "count value reach __"
while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))

# prints out 1,2,3,4
for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")