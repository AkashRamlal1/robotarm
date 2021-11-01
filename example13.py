from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:

# Na jouw code wachten tot het sluiten van de window:
for blok in range(0, 9):
    robotArm.grab()
    kleur = robotArm.scan()
    print(kleur)
    if kleur != "":
        for blokje in range(0, blok + 1):
            robotArm.moveRight();
        robotArm.drop()
        for blokje in range(0, blok + 1):
            robotArm.moveLeft();
            print("")
    elif kleur == "":
        break