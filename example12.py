from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

kleur = "red"
# Na jouw code wachten tot het sluiten van de window:

for blok in range(9):
    robotArm.moveRight();
for blok in range(9): # hoeveel blokken zijn er? geen 27!
    robotArm.grab()
    kleur = robotArm.scan()
    print(kleur)
    if kleur == "red":
        for i in range(blok + 2): # gebruik hier niet de var blok
            robotArm.moveRight();
        robotArm.drop()
        for i in range(blok + 3): 
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft();