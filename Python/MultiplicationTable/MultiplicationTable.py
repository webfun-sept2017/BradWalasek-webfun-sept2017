length = 12
count = 0
altcount = 0
for altcount in range(0,length+1):
    display = "x"
    if altcount == 0:
        for count in range(1,length+1):
            display+= " " +str(count)
        print display

    else:
        display = str(altcount)
        for count in range(1,length+1):

            display += " " + str(altcount * count)
        print display
