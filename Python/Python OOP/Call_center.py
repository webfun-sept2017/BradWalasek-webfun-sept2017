class Call(object):
    def __init__(self, callid, name, number, time, reason):
        self.callid = callid
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
        self.callinfo = (
            [self.callid,
            self.name,
            self.number,
            self.time,
            self.reason]
            )
    def display(self):
        print self.callinfo
    def ret(self):
        return self.callinfo


class CallCenter(Call):
    def __init__(self, *calls):

        self.quesize = len(calls)
        self.callslist = []

        for x in range(0,self.quesize):
            self.callslist.append(calls[x])
    def show(self):
        # print self.callslist
        for item in self.callslist:
            print item[1], item[2]
        print self.quesize
    def add(self, call):
        self.callslist.append(call)
        self.quesize += 1
    def remove(self):
        self.callslist.pop(0)
        self.quesize -= 1

complaint1 = Call('caller 1', 'Joe somebody', '360-000-0000',"06/12",'Prank call')
complaint2 = Call('caller 2', 'Joe nobody', '360-000-0001',"06/13",'disgruntled guy')
complaint3 = Call('caller 3', 'Notjoe Everybody','300000000', "06/14", 'Guy calling in to work')

a = complaint1.ret()
b = complaint2.ret()
c = complaint3.ret()

masterlist = CallCenter(a,b)
masterlist.show()
masterlist.add(c)
masterlist.show()
masterlist.remove()
masterlist.show()

# complaint2.display()
# print complaint2.returnlist()
# print complaint1.returnlist()
# b = complaint2.returnlist()
# c = complaint1.returnlist()
# class exp(object):
#     def test(self, *call):
#         print call
#         print len(call)
#         return self
# a = exp()
# a.test(b, c)
