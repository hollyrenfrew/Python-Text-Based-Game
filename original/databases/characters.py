import random
from databases.items import *

class Player:
    def __init__(self):
        self.name = "William"
        self.max_hp = 200
        self.hp = 200
        self.strength = 5
        self.defense = 6
        self.speed = 6
        self.skill = 7
        self.luck = 5
        self.magic = 4
        self.max_magic = 4
        self.weapons = [sword]
        self.weapon_equip = sword
        self.items = ["Bandage"]
        self.boon = ""
        self.bane = ""
        self.alive = True


class Enemy:
    def __init__(self, ename):
        self.name = ename
        self.max_hp = random.randint(15, 25)
        self.hp = self.max_hp
        self.strength = random.randint(4, 15)
        self.defense = random.randint(1, 4)
        self.speed = random.randint(4, 8)
        self.skill = random.randint(5, 8)
        self.luck = random.randint(2, 10)
        self.weapon = random.choice([axe, sword])
        self.alive = True


player = Player()
entry_1 = Enemy("Rodriguez")
ale_1 = Enemy("Ramirez")
ale_2 = Enemy("Remiel")
prisoner_1 = Enemy("Riley")
prisoner_2 = Enemy("Robert")
armory_1 = Enemy("Russell")
training_1 = Enemy("Ryder")
treasure_1 = Enemy("Ronan")
treasure_2 = Enemy("Remy")
dorm_1 = Enemy("Rafael")
dorm_2 = Enemy("Ryker")

# Boss Stats
razor_fang = Enemy("Razorfang")
razor_fang.max_hp = random.randint(35, 45)
razor_fang.hp = razor_fang.max_hp
razor_fang.strength = random.randint(10, 20)
razor_fang.defense = random.randint(7, 12)
razor_fang.speed = random.randint(5, 13)
razor_fang.skill = random.randint(5, 15)
razor_fang.luck = random.randint(15, 25)
razor_fang.weapon = razor_axe

enemy_list = (entry_1, ale_1, ale_2, prisoner_1, prisoner_2, armory_1,
              training_1, treasure_1, treasure_2, dorm_1, dorm_2, razor_fang)

