from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 2


# Jouw python instructies zet je vanaf hier
blokje=1



# Na jouw code wachten tot het sluiten van de window:
for blokje in range(5):
    for blokje in range(6):
        robotArm.moveRight();
        robotArm.grab()
        robotArm.moveLeft();
        robotArm.drop()
    for blokje in range(2):
        robotArm.moveRight();

