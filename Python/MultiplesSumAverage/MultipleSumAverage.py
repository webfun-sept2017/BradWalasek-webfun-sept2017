# This bit of code is to solve part 1 of the assignment
for count in range(0,1001):
    if count%2 != 0:
        print count

# This is to solve part 2 of the assignment
x=0
while x < 1000001:
    if x%5 == 0:
        print x, "is equal to 5 * ", x/5
    x += 1

# This will add all values in a list
a = [1,2,5,10,255,3]
count = 0
b = 0
for count in range(0, len(a)):
    b = b + a[count]
print b

# This will find the average of all the values in a list
a = [1,2,5,10,255,3]
count = 0
b = 0
for count in range(0, len(a)):
    b = b + a[count]
    c = b/len(a)
print c
