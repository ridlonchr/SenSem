from shooter import *

newGame = Game()
"""
soilders = { "1":Soilder("Christian", 90),
             "2":Soilder("Jeff",85),
             "3":Soilder("Charles",10) }
"""

aliveSoilders = len(newGame.soilders)

while aliveSoilders > 1:

"""
    for name in sorted(newGame.soilders.keys() ):
        print "\n", name, newGame.soilders[name]
"""

    first = int(raw_input("Who fires? "))
    second = int(raw_input("Who at? " ))


    try:
        first_soilder = newGame.soilders[first]
        second_soilder = newGame.soilders[second]
        # catch friendly fire

    except:
        print "No such soilder exits!"
        continue



    if not first_soilder.alive or not second_soilder.alive:
        print "One of those soilders is dead!"
        continue

    print
    print "******************************"

    first_soilder.fire_at(second_soilder)
    if not second_soilder.alive:
        aliveSoilders-= 1

    print "******************************"

for soilder in newGame.soilders.values():
    if soilder.alive:
        print soilder.name, "is the winner!"
        break
