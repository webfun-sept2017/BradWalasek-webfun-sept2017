import random





def toss(num):
    heads = 0
    tails = 0
    details = ""
    for count in range(0,num):
        t = random.randint(1,2)
        if t == 1:
            heads+= 1
            details = "head"

        if t == 2:
            tails+= 1
            details = "tail"
        print "Attempt #" + str(count) + " Throwing a coin... It's a "+ details +" ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
    print "Ending the program, Thank you!"
    # I think the intention was for me to round a number given from random.random,
    # I decided to go a different route and I think it works out better



toss(100000)
