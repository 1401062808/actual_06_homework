# coding=utf-8 
'''
猫狗大战加几个属性： ◦猫的闪避是10%，护甲是1
狗的护甲是3
老鼠的护甲是2
'''

import random
class Animal():
	"""docstring for Animal"""
	def __init__(self, name,blood,dps,armor,dodge):
		self.name = name
		self.blood = blood
		self.max_blood = blood
		self.dps = dps
		self.armor = armor
		self.dodge = dodge
	def attack(self,other):
		print '%s attack %s' %(self.name,other.name)

		attack_bool = True
		if other.dodge < 1 and other.dodge > 0:
			if random.randint(1,int(1/other.dodge)) == 1:
				attack_bool = False
		elif other.dodge >= 1:
			attack_bool = False

		if attack_bool == True:
			other.blood = other.blood - self.dps + other.armor
			if other.blood <= 0:
				print '%s is dead' %(other.name)
			else:
				other.report()
		else:
			print '%s dodge success !' %(other.name)
	def report(self):
		print '%s has %s blood left' %(self.name,self.blood)

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		Animal.__init__(self,'dog',100,20,3,0)

class Cat(Animal):
	"""docstring for Dog"""
	def __init__(self):
		Animal.__init__(self,'cat',100,30,1,0.1)

class Rat(Animal):
	"""docstring for Rat"""
	def __init__(self):
		Animal.__init__(self,'rat',40,5,2,0)
		self.cure_num = 15
	def cure(self,other):
		other.blood += self.cure_num
		if other.blood>other.max_blood:
			other.blood = other.max_blood
		other.report()


dog1 = Dog()
cat1 = Cat()
rat1 = Rat()

dog1.attack(cat1)
dog1.attack(cat1)
dog1.attack(cat1)
dog1.attack(cat1)
dog1.attack(cat1)
dog1.attack(cat1)
dog1.attack(cat1)
dog1.attack(cat1)
cat1.attack(dog1)
rat1.attack(cat1)
rat1.cure(dog1)


		