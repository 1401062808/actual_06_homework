# coding:utf-8
import random

# 猫狗大战
# class小游戏，加入护甲，闪避的概率
#     cat 闪避的概率 10% 护甲1
#     dog 狗皮比较厚 护甲是3
#     rat 奶妈 的护甲是 2
# 护甲 armour 1~10级  减少伤害10% -- 100%
# 闪避概率 dodge_rate 0~100%

class Animal():
    def __init__(self, name, blood, dps, armour=0, dodge_rate=0):
        self.name = name
        self.blood = blood
        self.max_blood = blood
        self.dps = dps
        
        # if armour >= 0 and armour <= 10:
        #     self.dodge_rate = dodge_rate_func(dodge_rate)
        # else:
        #     self.dodge_rate = 0

        dodge_rate_func = lambda dodge_rate: (dodge_rate >= 0 and dodge_rate <= 1) * dodge_rate
        self.dodge_rate = dodge_rate_func(dodge_rate)

        # print "%s dodge_rate %f" % (self.name, self.dodge_rate)

        armour_func = lambda armour: (armour >= 0 and armour <= 10) * armour
        self.armour = armour_func(armour)
        # self.armour = armour_func(armour)
        # self.critical_strike_rate

    def attack(self, other):
        # self attack other
        # dead man can't attack other
        if self.blood <= 0:
            print '%s is dead' % (self.name)
            return 1
            
        print "%s attacks %s" %(self.name, other.name)

        # 闪避 
        if random.random() > other.dodge_rate:
            # armour 
            other.blood -= self.dps * ( 1- other.armour / 10.0)
        else:
            print "%s has dodged %s's attacking" % (other.name, self.name)

        if other.blood <= 0:
            print '%s is dead.' % (other.name)
            # print "Game over!!"
            return 1
        else:
            other.report()

    def report(self):
        print "%s has %s blood left" % (self.name, self.blood)


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, name='dog', blood=100, dps=20, armour=3)


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, name='cat', blood=80, dps=30, armour=1, dodge_rate=0.1)


class Rat(Animal):
    # 奶妈 dps 少 具备cure回血功能
    def __init__(self):
        Animal.__init__(self, name='rat', blood=40, dps=5, armour=2)
        self.cure_num = 15

    def cure(self, other):
        # if other.blood + self.rcure_num >= other.max_blood:
        #     other.blood = other.max_blood
        # else:
        #     other.blood += self.cure_num

        # 防止奶妈救活私人
        if other.blood <= 0:
            print "%s is dead and can't be saved." % (other.name)
            return 1

        print "%s cure %s of %d blood" % (self.name, other.name, self.cure_num)
        other.blood += self.cure_num
        if other.blood >= other.max_blood:
            other.blood = other.max_blood

        other.report()

# 还可以做暴击，闪避等功能，用random，控制概率
# random.random()>0.7 闪避和暴击实现

dog1 = Dog()
cat1 = Cat()
rat1 = Rat()

while dog1.blood > 0 and cat1.blood > 0:
    dog1.attack(cat1)
    cat1.attack(dog1)
    if dog1.blood > dog1.max_blood / 4:
        rat1.attack(cat1)
    else:
        rat1.cure(dog1)

# dog1.attack(cat1)
# cat1.attack(dog1)
# rat1.attack(cat1)
# rat1.cure(dog1)
# rat1.cure(dog1)
# rat1.cure(dog1)

