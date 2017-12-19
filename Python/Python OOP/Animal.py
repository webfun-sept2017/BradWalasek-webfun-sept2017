class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog,self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init(self, name, health):
        super(Dragon,self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health():
        super(Dragon,self).display_health()
        return self




Desdemona = Animal("Dessi", 100)
Desdemona.walk().walk().walk().run().run().display_health()
nadiya = Dog("Nadiya", 0)
nadiya.walk().walk().walk().run().run().pet().display_health()
# nadiya.fly()
Seeth = Dragon('Seeth', 1)
# Seeth.display_health()
# .fly().display_health()
Shyguy = Animal("Shyguy", 100)
# Shyguy.pet()
