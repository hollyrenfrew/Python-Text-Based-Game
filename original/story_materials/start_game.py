import time
import pygame

from databases import player_information
from databases.rooms import entry_hall
from functions.print_speed import print_fast, print_slow
from screens.game_over import player_initialize
from story_materials.enter_room import enter_room
from databases.characters import player
from functions.list_to_string import list_to_string

audio1 = "music/tower_defense.mp3"
audio2 = "music/move_it_out.mp3"
audio3 = "music/our_mountain.mp3"

def start_game():
    print_fast("Starting game....\n")
    character_creation()
    opening_letter()
    player_information.current_room = entry_hall
    enter_room()


def character_creation():
    pygame.mixer.music.fadeout(3000)
    pygame.mixer.music.load(audio1)
    pygame.mixer.music.play(-1, 0, 3000)
    time.sleep(2)
    format_string_center = '{string:^43}'
    format_string_left = '{string:<43}'
    character = False
    while not character:
        boon = ""
        bane = ""
        boon_list = {"Robust", "Clever", "Strong", "Deft", "Quick", "Lucky", "Sturdy"}
        bane_list = {"Sickly", "Dull", "Weak", "Clumsy", "Slow", "Unlucky", "Fragile"}
        print_slow(format_string_center.format(string="What is your character's name?"))
        name = input()
        player.name = name.capitalize().strip()
        creation_prompt = "Which of the following best describes your character:"
        print_slow(format_string_center.format(string=creation_prompt))
        while boon not in boon_list:
            print_slow(list_to_string(boon_list, ", "))
            boon = input()
            boon = boon.capitalize().strip()
            player.boon = boon
        if boon == "Robust":
            player.max_hp += 25
            player.hp += 25
            bane_list.remove("Sickly")
        if boon == "Clever":
            player.magic += 2
            player.max_magic += 2
            bane_list.remove("Dull")
        if boon == "Strong":
            player.strength += 2
            bane_list.remove("Weak")
        if boon == "Deft":
            player.skill += 2
            bane_list.remove("Clumsy")
        if boon == "Quick":
            player.speed += 2
            bane_list.remove("Slow")
        if boon == "Lucky":
            player.luck += 4
            bane_list.remove("Unlucky")
        if boon == "Sturdy":
            player.defense += 2
            bane_list.remove("Fragile")
        print_slow(creation_prompt)
        while bane not in bane_list:
            print_slow(format_string_center.format(string=(list_to_string(bane_list, ", "))))
            bane = input()
            bane = bane.capitalize().strip()
            player.bane = bane
            if bane == "Sickly":
                player.max_hp -= 15
                player.hp -= 15
            if bane == "Dull":
                player.magic -= 1
                player.max_magic -= 1
            if bane == "Weak":
                player.strength -= 1
            if bane == "Clumsy":
                player.skill -= 1
            if bane == "Slow":
                player.speed -= 1
            if bane == "Unlucky":
                player.luck -= 2
            if bane == "Fragile":
                player.defense -= 1
        print_slow(format_string_center.format(string="Are these parameters correct?"))
        print_slow(format_string_left.format(string=("Name: " + player.name)))
        print_slow(format_string_left.format(string=("HP:" + str(player.max_hp))))
        print_slow(format_string_left.format(string=("MAG:" + str(player.max_magic))))
        print_slow(format_string_left.format(string=("STR:" + str(player.strength))))
        print_slow(format_string_left.format(string=("SKL:" + str(player.skill))))
        print_slow(format_string_left.format(string=("SPD:" + str(player.speed))))
        print_slow(format_string_left.format(string=("LCK:" + str(player.luck))))
        print_slow(format_string_left.format(string=("DEF:" + str(player.defense))))
        answer = ""
        while (answer != "yes") and (answer != "no"):
            answer = input("Please enter yes or no.\n")
            answer = answer.lower().strip()
        if answer == "yes":
            character = True
        else:
            character = False
            player_initialize()
    print_slow(format_string_center.format(string="Character creation complete. Game beginning..."))
    print_slow(format_string_center.format(string=".  .  ."))


def opening_letter():
    pygame.mixer.music.fadeout(3000)
    pygame.mixer.music.load(audio2)
    pygame.mixer.music.play(-1, 0, 3000)
    format_string_left = '    |  {string:<33}  |'
    format_string_right = '    |  {string:>33}  |'
    format_string_center = '{string:>43}'
    print_fast("""
    .-.----------------------------------.-.
    ((o))                                    )
    \\U/_______          _____          ____/""")
    print_slow(format_string_left.format(string=("To " + player.name) + ","))
    print_fast(format_string_left.format(string=" "))
    print_slow(format_string_left.format(string="Long  ago,  your  father  was  a"))
    print_slow(format_string_left.format(string="protector in this country. Since"))
    print_slow(format_string_left.format(string="his death,  bandits have  become"))
    print_slow(format_string_left.format(string="bolder.  Before his  passing, he"))
    print_slow(format_string_left.format(string="mentioned   you  were   quite  a"))
    print_slow(format_string_left.format(string="warrior   yourself,  and  so  we"))
    print_slow(format_string_left.format(string="beseech  you  to help  us as  he"))
    print_slow(format_string_left.format(string="once did."))
    print_fast(format_string_left.format(string=" "))
    print_slow(format_string_left.format(string="A group of  bandits led by a  man"))
    print_slow(format_string_left.format(string="known as  Razorfang razed a small"))
    print_slow(format_string_left.format(string="town, Fayhaven, located near your"))
    print_slow(format_string_left.format(string="home. Our soldiers are  currently"))
    print_slow(format_string_left.format(string="occupied  in  the North  with the"))
    print_slow(format_string_left.format(string="war and so we will not be able to"))
    print_slow(format_string_left.format(string="send any assistance.  Please help"))
    print_slow(format_string_left.format(string="Fayhaven and its people."))
    print_fast(format_string_left.format(string=" "))
    print_slow(format_string_left.format(string="Ten people were taken hostage and"))
    print_slow(format_string_left.format(string="brought to  the bandit's hold  to"))
    print_slow(format_string_left.format(string="sell as slaves or  perhaps worse."))
    print_slow(format_string_left.format(string="If  you  can, please  save  these"))
    print_slow(format_string_left.format(string="hostages   while  you  take  care"))
    print_slow(format_string_left.format(string="of the bandits."))
    print_fast(format_string_left.format(string=" "))
    print_slow(format_string_left.format(string="Thank you for your consideration."))
    print_fast(format_string_left.format(string=" "))
    print_slow(format_string_right.format(string="Sincerely,"))
    print_slow(format_string_right.format(string="King Arthur"))
    print_fast("""    |______    _______    __  _____    ___|
    /A\\                                    \\
    ((o))                                   )
    '-'------------------------------------'
    """)
    print_slow(format_string_center.format(string="Do you accept this quest?"))
    answer = input("> ")
    answer = answer.strip().lower()
    while answer != "yes" and answer != "no":
        print_slow(format_string_center.format(string="Please enter yes or no."))
        answer = input("> ")
        answer = answer.strip().lower()
    if answer == "no":
        print_slow(format_string_center.format(string="You decided not to go on the quest."))
        time.sleep(1)
        print_slow(format_string_center.format(string="Game over."))
        time.sleep(1)
        input("Press enter to return to the title screen.")
        from screens.menus import title
        title()
