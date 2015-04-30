# Author: Christian Ridlon
# d20.py

from random import randint

"""
 This is a class representation of a d20 (copyright wizards of the coast)
 i modified the rule set to suit my needs but follows the basic pattern
 of the well known d20 system
"""
class d20_Combat(object):

    def __init__(self, attacker, defender):

        self.attacker = attacker
        self.defender = defender
        self.crit = False
        self.saving_thro = False
        self.attacker_roll = self.roll()
        self.defender_roll = self.roll()
        self.total_attack = 0
        self.total_defense = 0

        self.damage = 0

        self.attack_roll()
        self.defense_roll()
        self.total_damage()



    def attack_roll(self):
        """
        attack = attack role (d20) + attack bonus
        melee attack bonus = Base Weapon damage + strength modifier
        ranged attack bonus = Base attack bonus + Dexterity modifier + range penalty

        # size needs to be replaced with an appropiate attribute

        a natural roll of 20 = automatic hit, possible critical hit

        a natural roll of 1 = automatic miss
        """

        if self.attacker_roll <= 19:
            self.total_attack = self.attacker_roll + self.attacker.dexterity
        elif self.attacker_roll == 20:
            self.crit = self.critical_strike()
            if self.crit == True:
                self.total_attack = self.attacker_roll +int((self.attacker_roll*.5)) + self.attacker.dexterity
                self.crit == False

    def defense_roll(self):
        """
        Defense = dexterity + class bonus + equipment bonus + size modifier
        """

        if self.defender_roll <= 19:
            self.total_defense = self.defender_roll + self.attacker.strength
        elif self.defender_roll == 20:
            self.saving_throw = self.saving_throw()
            if self.saving_thro == True:
                self.defender_roll = -1
                self.self.saving_throw = False


    def saving_throw(self):
        saving_throw_roll = self.roll()

        if saving_throw_roll > self.attacker_roll:
            return True
        else:
            return False

    def critical_strike(self):
        """
        if a natural 20 is rolled by the attacker an oppertunity arrives for
        them to score a critical hit, to determine if it indeed the roll was a
        critical hit, the attacker makes another attack role and if it beets the
        prievously thrown defense roll, a critical hit is scored and a damage
        multiplier of x2 is applied
        Returns a bool T/F depending on if the critical strike was succesful
        """
        critical_strike_roll = self.roll()

        if critical_strike_roll > self.defender_roll:
            return True
        else:
            return False

    def total_damage(self):
        """
        determines if and how much damage is dealt
        """
        if self.total_defense == -1:
            self.damage = -1
        else:
            dmg = self.total_attack - self.total_defense
            if dmg <=0:
                self.damage = 0
            else:
                self.damage = dmg

    def roll(self):
        """
        rolls a 20 sided dice and returns the value
        """
        return randint(1,20)
