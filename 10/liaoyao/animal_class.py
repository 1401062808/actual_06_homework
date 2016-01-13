#!/usr/bin/env python

class Animal():
	def __init__(self,name,blood,dps):
		self.name =  name
		self.blood = blood
		self.max_blood = blood
		self.dps = dps

	def attack(self,other):
		print '%s attack %s' % (self.name,other.name)
		other.blood -= self.dps
		if other.blood <= 0:
			print '%s is dead' % other.name
		else:
			other.report()
	def report(self):
		print '%s has %s blood left' % (self.name,self.blood)

class Dog(Animal):
	def __init__(self):
		Animal.__init__(self,'dog',100,20)

class Cat(Animal):
	def __init__(self):
		Animal.__init__(self,'cat',80,30)

class Rat(Animal):
	def __init__(self):
		Animal.__init__(self,'rat',50,5)
		self.cure_num = 15
	
	def cure(self,other):
		other.blood += self.cure_num
		if other.blood > other.max_blood:
			other.blood = other.max_blood
		other.report()

dog1 = Dog()
cat1 = Cat()
rat1 = Rat()

dog1.attack(cat1)
cat1.attack(dog1)
rat1.attack(cat1)
at1.cure(dog1)
