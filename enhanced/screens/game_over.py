from databases import player_information, rooms
from databases.characters import player
from functions.print_speed import print_slow
from story_materials.special_rooms import high_scores_display

format_string_left = '{string:<43}'
format_string_right = '{string:>43}'
format_string_center = '{string:^43}'


def game_over():

    from story_materials.enter_room import enter_room
    from screens.menus import title
    if player_information.total_points < 20:
        print("Your score: ", str(player_information.total_points))
        print_slow(format_string_left.format(string="You do not have enough points to restart."))
    else:
        print_slow(format_string_left.format(string="You died! Would you like to restart from this room?"))
        print_slow(format_string_left.format(string="It will dock 20 points from your final score."))
        user_input = input("> ").strip().lower()
        while user_input not in ["yes", "no"]:
            print_slow(format_string_left.format(string="Enter yes or no."))
            user_input = input("> ").strip().lower()
        if user_input == "yes":
            player_restart()
            player_information.total_points -= 20
            enter_room()
    print_slow(format_string_left.format(string="Choose an option:"))
    print_slow(format_string_left.format(string="Restart: start from the beginning with your current character."))
    print_slow(format_string_left.format(string="Title: start from the beginning before character creation."))
    print_slow(format_string_left.format(string="▶ Restart ◀"))
    print_slow(format_string_left.format(string="▶ Title ◀"))
    user_input = input("> ").strip().lower()
    while user_input not in ["restart", "title"]:
        print_slow(format_string_left.format(string="Please enter restart or title."))
        print_slow(format_string_left.format(string="Restart: start from the beginning with your current character."))
        print_slow(format_string_left.format(string="Title: start from the beginning before character creation."))
        user_input = input("> ").strip().lower()
    print("Your score: ", str(player_information.total_points))
    high_scores_display()
    characters_initialize()
    initialize_rooms()
    if user_input == "restart":
        player_restart()
        enter_room()
    else:
        player_initialize()
        title()


def player_restart():
    player.alive = True
    player.hp = player.max_hp


def player_initialize():
    player.name = "William"
    player.max_hp = 200
    player.hp = 200
    player.strength = 7
    player.defense = 6
    player.speed = 6
    player.skill = 7
    player.luck = 5
    player.magic = 4
    player.weapon = [sword, axe]
    player.weapon_equip = sword
    player.items = []
    player.boon = ""
    player.bane = ""
    player.alive = True


def characters_initialize():
    for i in range(0, len(enemy_list) - 1):
        enemy_list[i].hp = enemy_list[i].max_hp
        enemy_list[i].alive = True


def initialize_rooms():
    rooms.entry_hall = Room("Entry Hall", entry_hall_items, entry_hall_enemies, entry_hall_directions)
    rooms.ale = Room("Ale House", ale_items, ale_enemies, ale_directions)
    rooms.prisoner = Room("Prisoner Hold", prisoner_items, prisoner_enemies, prisoner_directions)
    rooms.armory = Room("Armory", armory_items, armory_enemies, armory_directions)
    rooms.training = Room("Training Room", training_items, training_enemies, training_directions)
    rooms.infirmary = Room("Infirmary", infirmary_items, infirmary_enemies, infirmary_directions)
    rooms.treasure = Room("Treasure Room", treasure_items, treasure_enemies, treasure_directions)
    rooms.dormitory = Room("Dormitory", dormitory_items, dormitory_enemies, dormitory_directions)
    rooms.razor = Room("Razorfang's Room", razor_items, razor_enemies, razor_directions)

