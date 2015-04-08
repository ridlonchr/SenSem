from random import randint
import pygame
import d20.d20 as d20


class Soilder(object):

    def __init__(self, name):

        print "\n***rolling for stats***"
        self.name = name
        self.accuracy = randint(50,100)
        self.defense = randint(1,12)
        self.power = randint(1,12)
        self.alive = True
        self.health = 100
        self.ammo = 15
        self.armor = 60

        print "Accuracy: ", self.accuracy
        print "Defense: ", self.defense
        print "Power: ", self.power, "\n"


    def __str__(self):

        if self.alive:
            return "%s ( %i health, %i armor, %i shells)"%(self.name,self.health, self.armor, self.ammo)
        else:
            return "%s (DEAD)"%self.name

    def damage(self, enemy):

        # attack roll
        attack = randint(1,20)
        attack += self.power
        # defense roll
        defense = randint(1,20)
        defense += enemy.defense
        # check for damage
        if attack > defense:
            damage = attack - defense
            print damage
            #defense saving throw
            saving_roll = randint(1,20)
            if saving_roll <= 2:
                return -1
            else:
                return damage
        elif defense > attack:
            damage = 0
            # offense desperate shot
            shot = randint(1,20)
            if shot <= 2:
                return shot
            else:
                return damage


    def fire_at(self, enemy):

        hit_or_miss = randint(1,100)
        hit_or_miss -= enemy.defense

        if hit_or_miss <= self.accuracy:
            if self.ammo >= 1:
                self.ammo-= 1
                print self.name, "fires at", enemy.name
                damage = self.damage(enemy)
                enemy.hit(damage,enemy)
            else:
                print self.name, "has no ammo!"
        else:
            print self.name, " missed!"

    #def miss(self):
    #    print self.name, "missed!"


    def hit(self,damage,enemy):
        if damage == -1:
            print enemy.name, " dodged ", self.name, '!'
        elif damage == 0:
            print self.name, " missed ", enemy.name, '!'
        elif self.armor > 0:
            self.armor -= damage
            print self.name, "is hit, and lost ", damage, " armor!"
        else:
            self.health -= damage
            print self.name, "is hit, and lost ", damage, " health!"
        if self.health <= 0:
            self.die()

    def reload(self):
        self.ammo = 15


    def die(self):

        self.alive = False
        print self.name, "is down!"
