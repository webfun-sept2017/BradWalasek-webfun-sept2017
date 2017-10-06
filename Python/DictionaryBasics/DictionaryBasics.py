# This was just an example to keep the functionality of dictionaries in my mind
# Brad = {"name": "Brad", "age": "26", "birthplace": "California"}
#
# for key, data in Brad.iteritems():
#     print key, data




def printData(di):
    # print "My name is " + di["name"]
    # print "My age is " + di["age"]
    # print "My country of birth is " + di["bp"]
    # print "My favorite language is " + di["la"]
    a = "My name is " + di["name"]
    b = "My age is " + di["age"]
    c = "My country of birth is " + di["bp"]
    d = "My favorite language is " + di["la"]
    ret = {"first_line": a, "second_line": b, "third_line": c, "fourth_line": d}
    return ret
Brad = {"name": "Brad", "age": "25", "bp":"California", "la":"Python"}
test = printData(Brad)
print test["first_line"]
print test["second_line"]
print test["third_line"]
print test["fourth_line"]
