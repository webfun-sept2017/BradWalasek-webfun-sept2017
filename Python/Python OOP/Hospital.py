class Patient(object):
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.bed = ""
        self.id = ""

        self.info = [
        self.name,
        self.allergies,
        self.bed,
        self.id
        ]

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.checked_in = 0
        self.staying = []
        self.bedarrangement = []
        self.ids = 1
        for x in range(0, capacity):
            self.bedarrangement.append("Unoccupied")
    def admit(self,patient):
        if self.checked_in >= self.capacity:
            print "Hospital full, cannot admit " + patient[0] + "."
            print ""
        else:
            patient[3]= self.ids
            self.ids += 1
            self.checked_in += 1
            self.staying.append(patient)
            c = False
            x=0
            while (c == False):
                if self.bedarrangement[x] == "Unoccupied":
                    c = True
                    patient[2]= x
                    self.bedarrangement.pop(x)
                    self.bedarrangement.insert(x, "Occupied")
                else:
                    x += 1
    def discharge(self, discharged):
        print discharged[0] + " is being discharged."
        self.staying.remove(discharged)
        self.checked_in -= 1
        self.bedarrangement[discharged[2]] = "Unoccupied"
        print ""

    def show(self):
            for p in self.staying:
                print str(p[0]) + " is patient " + str(p[3]) + ", staying in bed " + str(p[2])+ " and is allergic to " + str(p[1]) + "."
            print ""
            print self.bedarrangement

rochelle = Patient('Rochelle', 'bites from the undead')
bill = Patient("Bill", "Bee stings")
ellis = Patient("Ellis", "Lactose")
louis = Patient("Louis", "Soy")
brad = Patient("Brad", "Pet Dander")
kate = Patient("Kate", "Lactose")
mercy = Hospital("Mercy", 4)
# mercy.show()
mercy.admit(bill.info)
mercy.admit(ellis.info)
mercy.admit(louis.info)
mercy.admit(rochelle.info)
mercy.show()
mercy.discharge(bill.info)
mercy.show()
mercy.admit(brad.info)
mercy.show()
mercy.admit(kate.info)
mercy.discharge(louis.info)
mercy.admit(kate.info)
mercy.show()
