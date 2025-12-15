from databases import player_information
from databases.rooms import direction_list, empty
from functions.print_speed import print_slow, print_slowish

format_string_left = '{string:<43}'
format_string_center = '{string:^43}'


def move():
    print_slowish(format_string_center.format(string="Which direction would you like to move?"))
    print_directions()
    move_direction = input("> ").capitalize().strip()
    while move_direction not in player_information.current_room.directions:
        print_slowish(format_string_center.format(string="Please enter one of the following options:"))
        print_directions()
        move_direction = input("> ").capitalize().strip()
    move_between_rooms(move_direction)


def move_between_rooms(direction):
    from story_materials import enter_room
    current_directions = empty
    for i in direction_list:
        if i.name == player_information.current_room.name:
            current_directions = i
    if direction != "Cancel":
        new_room = getattr(current_directions, direction)
        player_information.current_room = new_room
        prep_string = "\nYou walked " + direction + " to reach the " + player_information.current_room.name + ".\n"
        print_slow(format_string_left.format(string=prep_string))
        enter_room.enter_room()


def print_directions():
    for i in range(0, len(player_information.current_room.directions)):
        print_slowish(format_string_center.format(string=("▶ " + player_information.current_room.directions[i] + " ◀")))

