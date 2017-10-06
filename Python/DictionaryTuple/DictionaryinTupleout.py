my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

# I have a few prints left inside for testing purposes, but it returns everything as it should!
def tupleR(dicto):
    ret = []
    count = 0
    for keys, values in dicto.iteritems():
        # print keys, values
        x = (keys, values)
        # print x
        ret.append(x)
        count += 1
    return ret
a = tupleR(my_dict)
print a
