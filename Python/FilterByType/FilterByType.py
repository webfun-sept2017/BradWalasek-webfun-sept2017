x = [1,2,3,4,5,6,7,8,9, 10]
if isinstance(x, int) == True:
    if x >= 100:
        print "That's a big number!"
    else:
        print "That's a small number"
if isinstance(x,str) == True:
    if len(x) >= 100:
        print "Long Sentence."
    else:
        print "Short Sentence."
if isinstance(x,list) == True:
    if len(x) >= 10:
        print "Big List!"
    else:
        print "Short List"
