l = ['magical','unicorns']
count = 0
stringReturned = ""
numberReturned = 0
isString = False
isNumber = False
for count in range(0,len(l)):
    if isinstance(l[count], str) == True:
        stringReturned += " " + l[count]
        isString = True
    else:
        numberReturned += l[count]
        isNumber = True

if isString == True and isNumber == True:
    result = "mixed type."
if isString == True and isNumber == False:
    result = "String type."
else:
    result = "Integer Type."

print "The list you entered is of", result
print stringReturned
print "Sum", numberReturned
