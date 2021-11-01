from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
blok = 1

# Na jouw code wachten tot het sluiten van de window:
for blok in range (7):
    for blok in range (9):
        robotArm.moveRight();
        robotArm.grab()
    robotArm.drop()
    for blok in range (8):
        robotArm.moveLeft();
    robotArm.grab()