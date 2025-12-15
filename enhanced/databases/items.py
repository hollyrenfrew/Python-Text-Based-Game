
class Weapon:
    def __init__(self):
        self.name = ""
        self.might = 0
        self.hit = 100


class Magic:
    def __init__(self):
        self.name = ""
        self.might = 0
        self.hit = 100


electric = Magic()
electric.name = "Electric"
electric.might = 25
electric.hit = 55

ice = Magic()
ice.name = "Ice"
ice.might = 20
ice.hit = 75

fire = Magic()
fire.name = "Fire"
fire.might = 15
fire.hit = 95

sword = Weapon()
sword.name = "Sword"
sword.might = 5
sword.hit = 105

axe = Weapon()
axe.name = "Axe"
axe.might = 10
axe.hit = 75

bow = Weapon()
bow.name = "Bow"
bow.might = 2
bow.hit = 120

razor_axe = Weapon()
razor_axe.name = "Razorfang's Axe"
razor_axe.might = 8
razor_axe.hit = 85