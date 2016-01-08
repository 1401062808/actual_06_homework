#coding:utf-8
import random

class Animal():
    def __init__(self, name, blood, dps, shield, dodge):
        self.name = name
        self.blood = blood
        self.maxblood = blood
        self.dps = dps
        self.shield = shield
        self.dodge = dodge

    def attack(self, another):
        if self.blood <= 0:
            print '%s is dead, quit...' %self.name
            return -1

        print '\33[44m%s attack %s\33[0m' %(self.name, another.name)
        dodge = random.random()
        if another.dodge <= dodge:
            another.blood = another.blood - self.dps + another.shield
        else:
            print '%s has dodge this attack!' %another.name
        if another.blood <= 0:
            print '%s is dead...' %another.name
        else:
            another.report()

    def report(self):
        print '%s has %s blood left' %(self.name, self.blood)

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, 'cat', 80, 20, 1, 0.1)

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, 'dog', 100, 10, 3, 0.05)

class Rat(Animal):
    def __init__(self):
        Animal.__init__(self, 'rat', 40, 5, 2, 0.2)

    def cure(self, another):
        if self.blood <= 0:
            print '%s is dead, quit...' %self.name
            return -1
        if another.blood <= 0:
            print '%s is dead, quit...' %another.name
            return -1

        print '\33[45m%s cure %s\33[0m' %(self.name, another.name)
        self.cure = 5
        another.blood += self.cure
        if another.blood >= another.maxblood:
            another.blood = another.maxblood
        another.report()

if __name__ == '__main__':
    cat01 = Cat()
    dog01 = Dog()
    rat01 = Rat()

    dog01.attack(cat01)
    dog01.attack(cat01)
    dog01.attack(rat01)
    dog01.attack(rat01)
    dog01.attack(cat01)
    cat01.attack(dog01)
    cat01.attack(rat01)
    cat01.attack(rat01)
    rat01.attack(dog01)
    rat01.attack(dog01)
    rat01.cure(cat01)
