# This counts to 2000 printing odd or even based on whether or not 2 divides into the number without a remainder
def odd_even():
    # count = 0
    for count in range(1,2001):
        if count%2 == 0:
            print count, "is even"
        else:
            print count, "is odd"


# Multiply function
def multiply(arr,num):
    for count in range(0, len(arr)):
        arr[count] *= num
    return arr

# Hacker Challenge
def layered_multiples(arr):
    new_arr = []
    for x in arr:

        count = 0
        var = []
        for count in range(0, x):
            var.append(1)

        new_arr.append(var)
    print new_arr





    return 0
x = layered_multiples(multiply([2,4,5],3))
