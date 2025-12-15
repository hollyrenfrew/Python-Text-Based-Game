from databases.rooms import *
from functions.print_speed import print_slowish


current_room = entry_hall
current_weapons = player.weapons
current_items = player.items
prisoners_free = False
civilian_healed = False

actions = ["Attack", "Magic", "Item"]
room_actions = ["Move", "Search", "Item", "Wait", "Save"]
total_points = 0

format_string_center = '{string:^43}'
def print_actions():
    for i in range(0, len(room_actions)):
        print_slowish(format_string_center.format(string=("▶ " + room_actions[i] + " ◀")))


