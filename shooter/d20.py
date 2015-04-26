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
        crit = False

    def attack_roll(self, attacker):
        """
        attack = attack role (d20) + attack bonus
        melee attack bonus = Base Weapon damage + strength modifier
        ranged attack bonus = Base attack bonus + Dexterity modifier + range penalty

        # size needs to be replaced with an appropiate attribute

        a natural roll of 20 = automatic hit, possible critical hit

        a natural roll of 1 = automatic miss
        """

        roll = randint(1,20)

        if roll == 20:
            self.crit = self.critical_strike()




    def defense_roll(self):
        """
        Defense = dexterity + class bonus + equipment bonus + size modifier
        """
        pass
    def saving_throw(self):
        pass

    def critical_strike(self, defense_roll):
        """
        if a natural 20 is rolled by the attacker an oppertunity arrives for
        them to score a critical hit, to determine if it indeed the roll was a
        critical hit, the attacker makes another attack role and if it beets the
        prievously thrown defense roll, a critical hit is scored and a damage
        multiplier of x2 is applied
        Returns a bool T/F depending on if the critical strike was succesful
        """
        critical_strike_roll = self.attacker.attack_roll()

        if critical_strike_roll > defense_roll:
            return true
        else:
            return false

    def damage(self):
        """
        determines if and how much damage is dealt
        """
        # get attack roll
        attck = self.attacker.attack_roll()

        # get defense roll
        dfnse = self.defender.defense_roll()



    def roll_d20(self):
        """
        rolls a 20 sided dice and returns the value
        """
        return randint(1,20)
