import math
from databases.characters import player
from databases import player_information
format_string_center = '{string:^43}'


def wait():
    from random import randint
    from functions.print_speed import print_slowish
    points = "Points: " + str(player_information.total_points)
    if player_information.total_points < 5:
        print_slowish(format_string_center.format(string="You need 5 points to wait."))
        print_slowish(format_string_center.format(string=points))
        print_slowish(format_string_center.format(string=".  .  ."))
    else:
        print_slowish(format_string_center.format(string="Do you wish to wait and spend 5 points?"))
        print_slowish(format_string_center.format(string=points))
        print_slowish(format_string_center.format(string=".  .  ."))
        answer = input("> ").lower().strip()
        while answer not in ["yes", "no"]:
            print_slowish(format_string_center.format(string="Please enter yes or no."))
            print_slowish(format_string_center.format(string=points))
            answer = input("> ").lower().strip()
        if answer == "yes":
            player_information.total_points -= 5
            percent = randint(5, 15)
            percent = percent / 100
            heal = math.ceil(player.max_hp * percent)
            print_slowish(format_string_center.format(string=("You rest and wait, healing " + str(heal) + " health.")))
            if player.hp >= player.max_hp - heal:
                player.hp = player.max_hp
            else:
                player.hp += heal
            print_slowish(
                format_string_center.format(string=(player.name + ": " + str(player.hp) + "/" + str(player.max_hp))))


