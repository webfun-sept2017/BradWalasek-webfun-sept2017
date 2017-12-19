class MathDojo(object):
    def __init__(self):
        self.value=0
    def add(self, num, *num1):
        if (num1):
            total = 0
            for x in range(0,len(num1)):
                print num1[x]
                try:
                    print sum(num1[x])
                    total = total + sum(num1[x])
                except:
                    total = num1[0]
            print str(total) + " is all in num1"
            self.value += total

        if isinstance(num, list):
            total = 0
            print num
            for x in range(0,len(num)):
                print num[x]
                total = total + num[x]
            print str(total) + " is all in num"
            self.value += total
        else:
            self.value+= num
        return self

    def subtract(self, num, *num1):
        if (num1):

            total = 0
            for x in range(0,len(num1)):
                print num1[x]
                try:
                    print sum(num1[x])
                    total = total + sum(num1[x])
                except:
                    total = num1[0]
            print str(total) + " is all in num1"
            self.value -= total

        if isinstance(num, list):
            total = 0
            print num
            for x in range(0,len(num)):
                print num[x]
                total = total + num[x]
            print str(total) + " is all in num"
            self.value -= total
        else:
            self.value-= num
        return self
    def result(self):
        print self.value
md = MathDojo()
# md.add(2).add(2).subtract(3).result()
# md.subtract(5,5).add(5,5).result()
# md.add([3,5,7,8], [2,4.3,1.25],[1,2,3]).result()
# md.subtract([3,5,7,8], [2,4.3,1.25],[1,2,3]).result()
# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()

# b = ([3,5,7,8], [2,4.3,1.25])
# print type(b[1])
# for x in range(0,len(b)):
#     print b[x]
#     print sum(b[x])
