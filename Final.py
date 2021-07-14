import random


print("Welcome! Choose below to select two mythical creatures!")
print("The Mythical creatures will be combined once chosen!")
print("The new hybrid creature will also come with statistsics and a description!")


print("\n -+- Menu -+- ")
print("\n    Zombie")
print("    Robot")
print("    Hydra")
print("    Yeti")
print("    Dragon")
print("    Phoenix")
print("    Griffin")

creatureOne = str(input("Which creature would you like to combine? "))
creatureTwo = str(input("Choose your second creature in which you are combining: "))


#zombie combinations with other creatures
zombieRobot = {
    "Zombot": 75,
    "Zombdra": 50
}
zombieHydra = {
    "Zombdra": 45,
    "Hybot": 65
}
zombieYeti = {
    "Zombti": 48,
    "Yetbie": 33
}
zombieDragon = {
    "Zragon": 85,
    "Dragbie": 77
}
zombiePhoenix = {
    "Zombix": 48,
    "Phoebix": 21
}
zombieGriffin = {
    "Zombfin": 88,
    "Griffbie": 26
}
#Robot combinations with other creatures except zombie since that was already included above
robotHydra = {
    "Rodra": 27,
    "Hybot": 63
}
robotYeti = {
    "Roti": 99,
    "Yetbot": 32
}
robotDragon = {
    "Robogon": 53,
    "Dragbot": 32
}
robotPhoenix = {
    "Robonix": 31,
    "Phoebot": 61
}
robotGriffin = {
    "Robofin": 77,
    "Griffbot": 32
}
#Hydra combinations excluding zombie and robot
hydraYeti = {
    "Hydrati": 104,
    "Yetdra": 53
    }
hydraDragon = {
    "Hydgon": 82,
    "Dragdra": 145
}
hydraPhoenix = {
    "Hydenix": 77,
    "Phoendra": 10,
}
hydraGriffin = {
    "Hydriffin": 33,
    "Griffdra": 21
}
#Dragon combinations excluding zombie,robot, and hydra
dragonYeti = {
    "Dragti": 88,
    "Yetdra": 73
}
dragonPhoenix = {
    "Phoegon": 73,
    "Dragnix": 33
}
dragonGriffin = {
    "Dragfin": 21,
    "Grifgon": 83
}
#Phoenix combinations excluding zombie, robot, hydra, and dragon
phoenixYeti = {
    "Phoeti": 38,
    "Yetnix": 89
}
phoenixGriffin = {
    "Phoeffin": 99,
    "Griffix": 81
}
#Griffin and Yeti combination
griffinYeti = {
    "Grifti": 182,
    "Yetfin": 88
}


griffinYetiKey = random.choice(list(griffinYeti))
phoenixGriffinKey = random.choice(list(phoenixGriffin))
phoenixYetiKey = random.choice(list(phoenixYeti))
dragonGriffinKey = random.choice(list(dragonGriffin))
dragonPhoenixKey = random.choice(list(dragonPhoenix))
dragonYetiKey = random.choice(list(dragonYeti))
hydraGriffinKey = random.choice(list(hydraGriffin))
hydraPhoenixKey = random.choice(list(hydraPhoenix))
hydraDragonKey = random.choice(list(hydraDragon))
hydraYetiKey = random.choice(list(hydraYeti))
robotGriffinKey = random.choice(list(robotGriffin))
robotPhoenixKey = random.choice(list(robotPhoenix))
robotDragonKey = random.choice(list(robotDragon))
robotYetiKey = random.choice(list(robotYeti))
robotHydraKey = random.choice(list(robotHydra))
zombieGriffinKey = random.choice(list(zombieGriffin))
zombiePhoenixKey = random.choice(list(zombiePhoenix))
zombieDragonKey = random.choice(list(zombieDragon))
zombieYetiKey = random.choice(list(zombieYeti))
zombieHydraKey = random.choice(list(zombieHydra))
zombieRobotKey = random.choice(list(zombieRobot))
#Griffin & Yeti
if creatureOne == "Griffin" and creatureTwo == "Yeti" or creatureOne == "Yeti" and creatureTwo == "Griffin":
    print ("Your hybrid creature is", griffinYetiKey, "and has",  griffinYeti[griffinYetiKey], "HP")
#Zombie & Yeti
elif creatureOne == "Zombie" and creatureTwo == "Yeti" or creatureOne == "Yeti" and creatureTwo == "Zombie":
    print ("Your hybrid creature is", zombieYetiKey, "and has",  zombieYeti[zombieYetiKey], "HP")
#Zombie & Hydra
elif creatureOne == "Zombie" and creatureTwo == "Hydra" or creatureOne == "Hydra" and creatureTwo == "Zombie":
    print ("Your hybrid creature is", zombieHydraKey, "and has",  zombieHydra[zombieHydraKey], "HP")
#Zombie & Robot
elif creatureOne == "Zombie" and creatureTwo == "Robot" or creatureOne == "Robot" and creatureTwo == "Zombie":
    print ("Your hybrid creature is", zombieRobotKey, "and has",  zombieRobot[zombieRobotKey], "HP")
#Zombie & Dragon
elif creatureOne == "Zombie" and creatureTwo == "Dragon" or creatureOne == "Dragon" and creatureTwo == "Zombie":
    print ("Your hybrid creature is", zombieDragonKey, "and has",  zombieDragon[zombieDragonKey], "HP")
#Zombie & Phoenix
elif creatureOne == "Zombie" and creatureTwo == "Phoenix" or creatureOne == "Phoenix" and creatureTwo == "Zombie":
    print ("Your hybrid creature is", zombiePhoenixKey, "and has",  zombiePhoenix[zombiePhoenixKey], "HP")
#Zombie & Griffin
elif creatureOne == "Zombie" and creatureTwo == "Griffin" or creatureOne == "Griffin" and creatureTwo == "Zombie":
    print ("Your hybrid creature is", zombieGriffinKey, "and has",  zombieGriffin[zombieGriffinKey], "HP")
#Robot & Hydra
elif creatureOne == "Robot" and creatureTwo == "Hydra" or creatureOne == "Hydra" and creatureTwo == "Robot":
    print ("Your hybrid creature is", robotHydraKey, "and has",  robotHydra[robotHydraKey], "HP")
#Robot & Yeti
elif creatureOne == "Robot" and creatureTwo == "Yeti" or creatureOne == "Yeti" and creatureTwo == "Robot":
    print ("Your hybrid creature is", robotYetiKey, "and has",  robotYeti[robotYetiKey], "HP")
elif creatureOne == "Robot" and creatureTwo == "Dragon" or creatureOne == "Dragon" and creatureTwo == "Robot":
    print ("Your hybrid creature is", robotDragonKey, "and has",  robotDragon[robotDragonKey], "HP")
elif creatureOne == "Robot" and creatureTwo == "Griffin" or creatureOne == "Griffin" and creatureTwo == "Robot":
    print ("Your hybrid creature is", robotGriffinKey, "and has",  robotGriffin[robotGriffinKey], "HP")
elif creatureOne == "Robot" and creatureTwo == "Phoenix" or creatureOne == "Phoenix" and creatureTwo == "Robot":
    print ("Your hybrid creature is", robotPhoenixKey, "and has",  robotPhoenix[robotPhoenixKey], "HP")
elif creatureOne == "Hydra" and creatureTwo == "Yeti" or creatureOne == "Yeti" and creatureTwo == "Hydra":
    print ("Your hybrid creature is", hydraYetiKey, "and has",  hydraYeti[hydraYetiKey], "HP")
elif creatureOne == "Hydra" and creatureTwo == "Dragon" or creatureOne == "Dragon" and creatureTwo == "Hydra":
    print ("Your hybrid creature is", hydraDragonKey, "and has",  hydraDragon[hydraDragonKey], "HP")
elif creatureOne == "Hydra" and creatureTwo == "Phoenix" or creatureOne == "Phoenix" and creatureTwo == "Hydra":
    print ("Your hybrid creature is", hydraPhoenixKey, "and has",  hydraPhoenix[hydraPhoenixKey], "HP")    
elif creatureOne == "Hydra" and creatureTwo == "Phoenix" or creatureOne == "Phoenix" and creatureTwo == "Hydra":
    print ("Your hybrid creature is", hydraPhoenixKey, "and has",  hydraPhoenix[hydraPhoenixKey], "HP")
elif creatureOne == "Hydra" and creatureTwo == "Griffin" or creatureOne == "Griffin" and creatureTwo == "Hydra":
    print ("Your hybrid creature is", hydraGriffinKey, "and has",  hydraGriffin[hydraGriffinKey], "HP")
elif creatureOne == "Dragon" and creatureTwo == "Yeti" or creatureOne == "Yeti" and creatureTwo == "Dragon":
    print ("Your hybrid creature is", hydraPhoenixKey, "and has",  hydraPhoenix[hydraPhoenixKey], "HP")
elif creatureOne == "Dragon" and creatureTwo == "Phoenix" or creatureOne == "Phoenix" and creatureTwo == "Dragon":
    print ("Your hybrid creature is", dragonPhoenixKey, "and has",  dragonPhoenix[dragonPhoenixKey], "HP")
elif creatureOne == "Dragon" and creatureTwo == "Griffin" or creatureOne == "Griffin" and creatureTwo == "Dragon":
    print ("Your hybrid creature is", dragonGriffinKey, "and has",  dragonGriffin[dragonGriffinKey], "HP")
elif creatureOne == "Phoenix" and creatureTwo == "Yeti" or creatureOne == "Yeti" and creatureTwo == "Phoenix":
    print ("Your hybrid creature is", phoenixYetiKey, "and has",  phoenixYeti[phoenixYetiKey], "HP")
elif creatureOne == "Phoenix" and creatureTwo == "Griffin" or creatureOne == "Griffin" and creatureTwo == "Phoenix":
    print ("Your hybrid creature is", phoenixGriffinKey, "and has",  phoenixGriffin[phoenixGriffinKey], "HP")
elif creatureOne or creatureTwo != "Zombie" and creatureOne or creatureTwo != "Robot" and creatureOne or creatureTwo != "Hydra" and creatureOne or creatureTwo != "Yeti" and creatureOne or creatureTwo != "Dragon" and creatureOne or creatureTwo != "Phoenix" and "Griffin":
    print("Please select only from the menu and remember that each item is case sensative!")

    

