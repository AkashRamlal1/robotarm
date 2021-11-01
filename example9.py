
from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

 
# Na jouw code wachten tot het sluiten van de window:

for blok in range(4):
    for blok in range(4):
        robotArm.grab()
        for blok in range(4):
            robotArm.moveRight();
        robotArm.drop()
        for blok in range(4):
            robotArm.moveLeft();
    for blok in range(1):
            robotArm.moveRight();