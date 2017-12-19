class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.displayInfo()
    def sell(self):
        self.status = "sold"
        print "Status is now " + self.status
        return self
        # pass
    def addTax(self, tax):
        taxed = (self.price*tax)+self.price
        print "Taxed price is " + str(taxed)
        return self
        # pass
    def return_product(self, reason):
        self.status = reason
        if reason == "defective":
            self.price = "0"
        elif reason == "new":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price = float(self.price) * .80
        else:
            self.status = reason
        return self

        # pass
    def displayInfo(self):
        if self.price > 1:
            value = " dollars"
        elif self.price > .01:
            value = " cents"
        else:
            value = " cent"
        print "Price is " + str(self.price) + value
        print "Item name is " + str(self.item_name)
        print "Weight is " + str(self.weight) + " lbs"
        print "Brand is " + str(self.brand)
        print "Status is " + str(self.status)
        print ""
        return self
apple = Product(.50, "Apple", .5, "Natures best")
# apple.addTax(.09)
# apple.sell()
# apple.return_product("defective")
# apple.return_product("opened")
# apple.return_product("new")
# apple.displayInfo()
