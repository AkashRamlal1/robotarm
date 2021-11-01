from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:

kleur = "white"
# Na jouw code wachten tot het sluiten van de window:
for blok in range(1):
    for blok in range(9):
        robotArm.moveRight();
    for blok in range(15):
        robotArm.grab()
        kleur = robotArm.scan()  # de command robotArm.scan controleert of he blokje de gewenste kleur is 
        print(kleur)
        if kleur == "white":
            robotArm.moveRight();
            robotArm.drop()
            robotArm.moveLeft();
        else:
            robotArm.drop()
            robotArm.moveLeft();
