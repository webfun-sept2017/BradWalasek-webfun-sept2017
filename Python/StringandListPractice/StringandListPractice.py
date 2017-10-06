words = "It's thanksgiving day. It's my birthday,too!"
print words
print words.find("day")
wordschanged = words.replace("day", "month")
print wordschanged

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y = ["hello", 2, 54, -2, 12, 98, "world"]
print y[0]
print y[len(y)-1]


z=[19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
z.sort()
# print z
k = z[0:len(z)/2]
for count in range(0, len(z)/2):

    z.pop(0)
# print z
# print k
z.insert(0, k)
print z
