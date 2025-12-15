from databases.characters import *

class Room:
    def __init__(self, name, items, enemies, directions, description="", description_empty="", description_enemy=""):
        self.name = name
        self.items = items
        self.enemies = enemies
        self.directions = directions
        self.description = description
        self.description_empty = description_empty
        self.description_enemy = description_enemy
        self.empty = False


# Entry_Hall
entry_hall_items = ["Bandage"]
entry_hall_directions = ["North", "South", "East", "Cancel"]
entry_hall_enemies = [entry_1]
eh_description = ("The Entry Hall  is a small room  at the entrance\n"
                  "to the bandit hold.  The wooden walls are barely\n"
                  "holding together.  It could make one  wonder how\n"
                  "it  is  still  holding  together.   It  is  also\n"
                  "probably  hard for  bandits to  find someone  to\n"
                  "repair buildings for them, which is why it is in\n"
                  "such disrepair.\n")

eh_description_empty = "There is  a dead  bandit  in the  middle of  the\nroom now."
eh_description_enemy = "There is a bandit in the middle of the room.  He\nattacks you!"

# Ale House
ale_items = ["Bandage", "Arrow", "Arrow", "Arrow", "Arrow", "Axe"]
ale_directions = ["South", "East", "Cancel"]
ale_enemies = [ale_1, ale_2]
ale_description = ("The Ale  House seems to be a dining area for the\n"
                   "bandits  in the hold.  There are  several  round\n"
                   "tables, some with  scattered plates  and cups on\n"
                   "them.  In the corner,  there is a  target  which\n"
                   "is  held  up  by  several   worn  out   daggers.")
ale_description_empty = ("After  defeating " + ale_1.name + " and "
                         + ale_2.name + " they  lay on\nthe ground unconscious.")
ale_description_enemy = ("Two  angry looking  bandits  look up from  their\n"
                         "table  and  notice  you.   They  brandish  their\n"
                         "weapons and attack!")

# Prisoner Hold
prisoner_items = ["Prison Key"]
prisoner_enemies = [prisoner_1, prisoner_2]
prisoner_directions = ["West", "Cancel"]
prisoner_description = ("As you enter  the prisoner  hold,  immediately a\n"
                        "putrid scent assaults your senses.  Spoiled food\n"
                        "sits  in  the  corner,  just out of  reach of a \n"
                        "skeleton's  hand  hanging  over one of the bars.\n"
                        "The bandits seem  to have held  people in  here,\n"
                        "before but it seems you're too late for that one\n"
                        "at least.\n")
prisoner_description_empty = ("The two  guards you  fought  earlier are  on the\n"
                              "ground unconscious.\n")
prisoner_description_enemy = ("You see two guards chatting with each other, but\n"
                              "the sound of you opening  the door cause them to\n"
                              "look at you. One sighs and says  'Let's get this\n"
                              "over with...'\n")

# Armory
armory_items = ["Bow", "Arrow", "Arrow", "Arrow", "Arrow"]
armory_enemies = [armory_1]
armory_directions = ["South", "East", "West", "Cancel"]
armory_description = ("The armory is  a storage  room full  of weapons\n"
                      "which don't seem to be in good shape. Maybe one\n"
                      "could find  a couple of  things worth grabbing,\n"
                      "but it seems the bandits are using all of their\n"
                      "limited resources already.")
armory_description_empty = "The enemy you defeated earlier is on the ground\nunconscious."
armory_description_enemy = "An enemy rushes at you!"

# Training Room
training_items = ["Bandage", "Bandage", "Bandage", "Magic Bead"]
training_enemies = [training_1]
training_directions = ["West", "Cancel"]
training_description = ("The training room seems to be just that - there\n"
                        "are targets littered  with arrows  around them,\n"
                        "only a  few   hitting the center.   Broken  and\n"
                        "dulled weapons are discarded near the entrance.")
training_description_empty = "The enemy you defeated earlier is on the ground\nunconscious."
training_description_enemy = "A single  enemy  spots you  and  comes  at  you\nbrandishing his weapon.."

# Infirmary
infirmary_items = ["D.Necklace"]
infirmary_enemies = []
infirmary_directions = ["North", "South", "East", "Cancel"]
infirmary_description = ("The infirmary is a mishmash of various items in\n"
                         "an attempt to create an area for healing. There\n"
                         "are blood stains on the barely holding together\n"
                         "beds and there  seems to be a dearth of medical\n"
                         "supplies.")
infirmary_description_empty = ""
infirmary_description_enemy = ""

# Treasure Room
treasure_items = ["Arrow", "Arrow", "Magic Bead", "Bandage", "Bandage", "Boss Key"]
treasure_enemies = [treasure_1, treasure_2]
treasure_directions = ["North", "West", "Cancel"]
treasure_description = ("Treasure room might be  a misnomer, as when you\n"
                        "enter the room there is only a couple of chests\n"
                        "with a few coins in them. There are a few piles\n"
                        "of clothes, pillaged off corpses or  civilians,\n"
                        "but only  a couple of gems,  and not  even ones\n"
                        "with much value.\n")
treasure_description_empty = "Two enemies lay on the ground, defeated."
treasure_description_enemy = ("When you enter  the Treasure  Room you see  two\n"
                              "strong  looking  bandits.  A  glint  off  a key\n"
                              "catches your eye - its  a key to enter  a  room\n"
                              "somewhere in the hold... maybe even  the boss's\n"
                              "room  where  he hides.  If  you beat  them  and\n"
                              "search the room,  maybe your  journey  could be\n"
                              "near its end...")

# Dormitory
dormitory_items = ["S.Ring", "Bandage"]
dormitory_enemies = [dorm_1, dorm_2]
dormitory_directions = ["North", "Cancel"]
dormitory_description = ("The dormitory is a room filled with beds lining\n"
                         "the walls,  a few stacked  on each  other.  The\n"
                         "beds are  nothing more  than some  wood holding\n"
                         "together some hay.\n\n"
                         "The bandits  seem quite poor, so  how did  they\n"
                         "raid Fayhaven as well as they did? Perhaps  the\n"
                         "bandits here were not the entire force.")
dormitory_description_empty = "Both bandits from before lay on the ground.\n"
dormitory_description_enemy = ("As you first enter the room, one bandits sleeps\n"
                               "on his bed,  and another  spots you, waking his\n"
                               "friend to attack you together.")

# Leader's Room
razor_items = []
razor_enemies = [razor_fang]
razor_directions = ["West", "Cancel"]
razor_description = ""
razor_description_empty = ""
razor_description_enemy = ""

# Room Objects
empty = Room(
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty",
    "Empty"
)

entry_hall = Room(
    "Entry Hall",
    entry_hall_items,
    entry_hall_enemies,
    entry_hall_directions,
    eh_description,
    eh_description_empty,
    eh_description_enemy,
)

ale = Room(
    "Ale House",
    ale_items,
    ale_enemies,
    ale_directions,
    ale_description,
    ale_description_empty,
    ale_description_enemy
)

prisoner = Room(
    "Prisoner Hold",
    prisoner_items,
    prisoner_enemies,
    prisoner_directions,
    prisoner_description,
    prisoner_description_empty,
    prisoner_description_enemy

)

armory = Room(
    "Armory",
    armory_items,
    armory_enemies,
    armory_directions,
    armory_description,
    armory_description_empty,
    armory_description_enemy
)

training = Room(
    "Training Room",
    training_items,
    training_enemies,
    training_directions,
    training_description,
    training_description_empty,
    training_description_enemy
)

infirmary = Room(
    "Infirmary",
    infirmary_items,
    infirmary_enemies,
    infirmary_directions,
    infirmary_description,
    infirmary_description_empty,
    infirmary_description_enemy
)

treasure = Room(
    "Treasure Room",
    treasure_items,
    treasure_enemies,
    treasure_directions,
    treasure_description,
    treasure_description_empty,
    treasure_description_enemy
)

dormitory = Room(
    "Dormitory",
    dormitory_items,
    dormitory_enemies,
    dormitory_directions,
    dormitory_description,
    dormitory_description_empty,
    dormitory_description_enemy
)

razor = Room(
    "Razorfang's Room",
    razor_items,
    razor_enemies,
    razor_directions,
    razor_description,
    razor_description_empty,
    razor_description_enemy
)


class Room_Directions:
    def __init__(self, name, north=entry_hall, south=entry_hall, east=entry_hall, west=entry_hall):
        self.name = name
        self.North = north
        self.South = south
        self.East = east
        self.West = west


room_list = [entry_hall, ale, prisoner, armory, training, infirmary, treasure, dormitory, razor]

# assigns each direction to a room to enter
eh_directions = Room_Directions("Entry Hall", ale, infirmary, armory, empty)
ah_directions = Room_Directions("Ale House", empty, entry_hall, prisoner, empty)
p_directions = Room_Directions("Prisoner Hold", empty, empty, empty, ale)
a_directions = Room_Directions("Armory", empty, treasure, training, entry_hall)
tra_directions = Room_Directions("Training Room", empty, empty, empty, armory)
i_directions = Room_Directions("Infirmary", entry_hall, dormitory, treasure, empty)
tre_directions = Room_Directions("Treasure Room", armory, empty, empty, infirmary)
d_directions = Room_Directions("Dormitory", infirmary, empty, razor, empty)
r_directions = Room_Directions("Razorfang's Room", empty, empty, empty, dormitory)

direction_list = [eh_directions, ah_directions, a_directions, p_directions,
                  tra_directions, i_directions, tre_directions, d_directions,
                  r_directions]
