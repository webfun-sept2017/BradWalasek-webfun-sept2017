class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        # pass
        print "price is " + self.price
        print "max speed is " + self.max_speed
        print "It has " + str(self.miles)  + " miles on it."
    def ride(self):
        # pass
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        # pass
        print "Reverse"
        self.miles += -5
        if self.miles < 0:
            self.miles = 0
        return self

newBike1 = Bike("40", "20")
newBike2 = Bike("100", "40")
newBike3 = Bike("500", "80")
# newBike1.displayinfo()
newBike1.ride().ride().ride().reverse().displayinfo()
newBike2.ride().ride().reverse().reverse().displayinfo()
newBike3.reverse().reverse().reverse().displayinfo()
