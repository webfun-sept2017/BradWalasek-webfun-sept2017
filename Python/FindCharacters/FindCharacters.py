word_list = ['hello','world','my','name','is','Anna']
new_list = []
char = 'o'
count = 0
for count in range(0, len(word_list)):
    var = word_list[count]
    # print var.find(char)
    if var.find(char) != -1:
        new_list.append(var)
print new_list

# This required 6 loops through since I didn't have to create a secondary loop
# to individually search through the words for a match. The .find method helped
# quite a bit.
