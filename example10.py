from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

afstand = 10
# Na jouw code wachten tot het sluiten van de window:
for blok in range(5):
    afstand = afstand - 1
    for blok in range(afstand):
        robotArm.grab()
        robotArm.moveRight();
    robotArm.drop()
    for blok in range(afstand):
        robotArm.moveLeft();