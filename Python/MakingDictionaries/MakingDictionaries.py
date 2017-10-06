name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def dictCreate(arra, arrb):
    # return dictionary created
    ret = {}
    # for each item in the dictionary
    for count in range(0,len(arra)):
        # print arra[count], arrb[count]
        # this was coded to ensure the values were matching pulled properly

        # this sets the key (array a) to have the corresponding value at the same count in array b
        ret[arra[count]] = arrb[count]
    return ret
a = dictCreate(name, favorite_animal)
for keys, values in a.iteritems():
    print keys, values
