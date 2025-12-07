import sys
import pygame
import time
import json
from functions import print_speed
from functions.print_speed import *
from save_system import init_db, list_saves_by_name, get_save_by_name

format_string = '╎ {string:^48} ╎'
format_options = '{string:^52}'
top_border = "┍" + "-" * 50 + "┐"
bottom_border = "┕" + "-" * 50 + "┙"

audio1 = "music/tower_defense.mp3"
audio2 = "music/move_it_out.mp3"
audio3 = "music/our_mountain.mp3"

def title():
    from story_materials.start_game import start_game

    # Ensure DB exists at startup
    init_db()

    # Music setup
    pygame.mixer.init()
    pygame.mixer.music.load(audio1)
    pygame.mixer.music.play(-1, 0, 3000)
    time.sleep(2)

    while True:
        print(top_border)
        print_fast(format_string.format(string="Welcome to Heroes and Villains"))
        print_fast(format_string.format(string="Holly Renfrew's Final IT-140 Project"))
        print(bottom_border)
        print_fast(format_options.format(string="▶ Play ◀"))
        print_fast(format_options.format(string="▶ Continue ◀"))
        print_fast(format_options.format(string="▶ About ◀"))
        print_fast(format_options.format(string="▶ Settings ◀"))
        print_fast(format_options.format(string="▶ Quit ◀"))

        option = input("> ").lower().strip()

        if option == "play":
            start_game()  # new game
        elif option == "continue":
            continue_game_menu(start_game)
        elif option == "about":
            about()
        elif option == "settings":
            settings()
        elif option == "quit":
            sys.exit()
        else:
            print("Invalid command, please try again.")



def continue_game_menu(start_game_func):
    print(top_border)
    print_fast(format_string.format(string="Continue Game"))
    print(bottom_border)

    # List unique save names with last saved time
    rows = list_saves_by_name()
    if not rows:
        time.sleep(1)
        return  # back to title loop

    print_fast(format_options.format(string="Enter a save name to load,"))
    print_fast(format_options.format(string="or type 'Back' to return."))

    while True:
        name = input("> ").strip()
        if not name:
            continue

        if name.lower() == "back":
            return  # back to title loop

        slot = get_save_by_name(name)
        if slot is None:
            print_fast(format_string.format(
                string=f"No save slot named '{name}'. Try again or type 'Back'."
            ))
            continue

        save_id, save_name, created_at, data_json = slot

        # Show a small preview before loading
        try:
            state = json.loads(data_json)
        except json.JSONDecodeError:
            print_fast(format_string.format(
                string="Error reading save data. Cannot load this slot."
            ))
            time.sleep(1)
            return

        p = state.get("player", {})
        pi = state.get("player_info", {})
        room_name = pi.get("current_room", "Unknown")
        hp = p.get("hp", "?")
        max_hp = p.get("max_hp", "?")
        points = pi.get("total_points", "?")

        print_fast(format_string.format(string=f"Loading '{save_name}' ({created_at})"))
        print_fast(format_string.format(string=f"Room: {room_name}"))
        print_fast(format_string.format(string=f"HP: {hp}/{max_hp}"))
        print_fast(format_string.format(string=f"Points: {points}"))
        print_fast(format_string.format(string=""))
        print_fast(format_string.format(string="Is this the save you want to load? (Yes / No)"))

        confirm = input("> ").strip().lower()
        while confirm not in ["yes", "no"]:
            print_fast(format_string.format(string="Please enter Yes or No."))
            confirm = input("> ").strip().lower()

        if confirm == "no":
            print_fast(format_string.format(string="Okay, choose another save name or type 'Back'."))
            continue

        # At this point, we load the game
        # Either let start_game handle import_state(state),
        # or do it here and call start_game_func(loaded_state=None).
        start_game_func(loaded_state=state)
        # When game returns, we go back to title (the while loop in title())
        return


def about():
    print(top_border)
    print_fast(format_string.format(string="The World of Heroes and Villains:"))
    print_fast(format_string.format(string="Avalon and Camelot"))
    print(bottom_border)
    print_fast(format_options.format(string="▶ World ◀"))
    print_fast(format_options.format(string="▶ Battle ◀"))
    print_fast(format_options.format(string="▶ Scores ◀"))
    print_fast(format_options.format(string="▶ Back ◀"))
    print_fast(format_options.format(string="What would you like to learn more about?"))
    option = input("> ").lower().strip()
    if option == "world":
        about_world()
    elif option == "battle":
        about_battle()
    elif option == "back":
        title()
    elif option == "scores":
        scores()
    while option.lower() not in ["world", "battle", "scores", "back"]:
        print_fast("Invalid command, please try again.")
        option = input("> ").lower().strip()
        if option.lower() == "world":
            about_world()
        elif option.lower().strip() == "battle":
            about_battle()
        elif option.lower() == "back":
            title()
        elif option == "scores":
            scores()


def about_world():
    print(top_border)
    print_slowish(format_string.format(string="In the world of  Heroes  and  Villains, you play"))
    print_slowish(format_string.format(string="the  child of a  well  known  hero who  recently"))
    print_slowish(format_string.format(string="passed away.  With  your father's sword you take"))
    print_slowish(format_string.format(string="up a mission from your king. "))
    print_slowish(format_string.format(string=""))
    print_slowish(format_string.format(string="You live in the  country of Avalon,  where  King"))
    print_slowish(format_string.format(string="Arthur resides in the capital: Camelot. However,"))
    print_slowish(format_string.format(string="the kingdom is at war with  the Northern country"))
    print_slowish(format_string.format(string="known as  Midgard, who under their  newest king,"))
    print_slowish(format_string.format(string="Loki, invaded Camelot earlier this  year. Unable"))
    print_slowish(format_string.format(string="to  convince  Camelot's  allies,   Atlantis  and"))
    print_slowish(format_string.format(string="Arcadia to aid against the invasion, King Arthur"))
    print_slowish(format_string.format(string="leads the armies  of Camelot against  Midgardian"))
    print_slowish(format_string.format(string="troops personally."))
    print(bottom_border)
    time.sleep(1)
    about()


def settings():
    speed_string = "Current Message Speed is: " + str(print_speed.normal_speed)
    print_fast(top_border)
    print_slow(format_string.format(string=speed_string))
    print_slow(format_string.format(string="Would you like to change the speed?"))
    print_fast(bottom_border)
    answer = input("> ")
    while answer.lower().strip() != "yes" and answer.lower().strip() != "no":
        print_slow("Please enter yes or no.")
        answer = input("> ")
    if answer == "yes":
        print_fast(("What value would you like for the new speed? Current:", print_speed.normal_speed))
        new_speed = input("> ")
        while not (new_speed.isdigit() and int(new_speed) != 0):
            print_fast("Please enter a number greater than 0.")
            print_fast(("What value would you like for the new speed? Current: ", print_speed.normal_speed))
            new_speed = input("> ")
        new_speed = int(new_speed)
        saved_speed = print_speed.normal_speed
        print_speed.normal_speed = new_speed
        new_speed_string = "New message speed is: " + str(print_speed.normal_speed)
        print_fast(top_border)
        print_slow(format_string.format(string=new_speed_string))
        print_slow(format_string.format(string="Would you like to save this speed?"))
        print_fast(bottom_border)
        answer = input("> ")
        if answer == "yes":
            print_slow(format_options.format(string="Speed successfully changed."))
            print()
        else:
            print_speed.normal_speed = saved_speed
            print_slow(format_options.format(string="Speed not changed."))
            print()
    title()


def about_battle():
    print(top_border)
    print_slowish(format_string.format(string="What would you like to know about battles?"))
    print(bottom_border)
    print_fast(format_options.format(string="▶ Stats ◀"))
    print_fast(format_options.format(string="▶ Turns ◀"))
    print_fast(format_options.format(string="▶ Attacks ◀"))
    print_fast(format_options.format(string="▶ Magic ◀"))
    print_fast(format_options.format(string="▶ Back ◀"))
    option = input("> ")
    if option.lower().strip() == "stats":
        about_stats()
    elif option.lower().strip() == "turns":
        about_turns()
    elif option.lower().strip() == "attacks":
        about_attacks()
    elif option.lower().strip() == "magic":
        about_magic()
    elif option.lower().strip() == "back":
        about()
    while option.lower() not in ["stats", "turns", "attacks", "magic", "back"]:
        print_fast("Invalid command, please try again.")
        option = input("> ")
        if option.lower().strip() == "stats":
            about_stats()
        elif option.lower().strip() == "turns":
            about_turns()
        elif option.lower().strip() == "attacks":
            about_attacks()
        elif option.lower().strip() == "magic":
            about_magic()
        elif option.lower().strip() == "back":
            about()


def about_stats():
    print(top_border)
    print_slowish(format_string.format(string="Stats"))
    print_slowish(format_string.format(string="------------------------------------------------"))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="HP:  Health Points.  Once  this  hits  zero, the"))
    print_slowish(format_string.format(string="character  dies.  If your character  hits  zero,"))
    print_slowish(format_string.format(string="game over."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="MAG: Magic  Points. This is  how many times  the"))
    print_slowish(format_string.format(string="character can use magic. If your hero's MAG hits"))
    print_slowish(format_string.format(string="zero,  you  cannot  use  magic  until  restored."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="STR:  Strength. This is  how hard the  character"))
    print_slowish(format_string.format(string=" hits."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="SKL:  Skill.  How  skilled  the character  is at"))
    print_slowish(format_string.format(string="fighting  in  general.   Affects  hit  rate  and"))
    print_slowish(format_string.format(string="critical rate."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="SPD: Speed. How  fast the character is.  Affects"))
    print_slowish(format_string.format(string="turn order and hit rate."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="LCK:  Luck.  How  much  fortune  smiles  on  the"))
    print_slowish(format_string.format(string="character. Affects critical rate."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="DEF: Defense.  How hard of a  hit the  character"))
    print_slowish(format_string.format(string="can take."))
    print_fast(format_string.format(string=""))
    print(bottom_border)
    time.sleep(1)
    about_battle()


def about_turns():
    print(top_border)
    print_slowish(format_string.format(string="When  combat  starts,  each  character  involved"))
    print_slowish(format_string.format(string="has  a randomized  number added to  their  speed"))
    print_slowish(format_string.format(string="then  these values are  compared to  each other."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Turn  Order  =  Speed  +  Random  Number  1 - 10"))
    print_slowish(format_string.format(string="Highest value goes first."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="If the  player ties with  an enemy, the order is"))
    print_slowish(format_string.format(string="rerolled  until there is no tie.  If enemies tie"))
    print_slowish(format_string.format(string="with each  other, they will simply  go one after"))
    print_slowish(format_string.format(string="another."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Once every character involved has had a turn, or"))
    print_slowish(format_string.format(string="a character involved dies the order is rerolled."))
    print(bottom_border)
    time.sleep(1)
    about_battle()


def about_attacks():
    print(top_border)
    print_slowish(format_string.format(string="When an attack is declared,  several numbers are"))
    print_slowish(format_string.format(string="calculated and  used to  determine the  outcome:"))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Hit Rate = (SKL * 1.5) + (LCK * 0.5) + Hit"))
    print_fast(format_string.format(string="---"))
    print_slowish(format_string.format(string="Hit  is a  number  attached to the  weapon being"))
    print_slowish(format_string.format(string="used.  For  example, Sword  has  a  hit  of  95."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Avoid = (D.SPD * 3 + D.LCK) / 2"))
    print_fast(format_string.format(string="---"))
    print_slowish(format_string.format(string="Avoid  uses  the defender's  stats  and  is used"))
    print_slowish(format_string.format(string="in  order  to  determine if the attack connects."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Hit Chance = Hit Rate - Avoid"))
    print_slowish(format_string.format(string="Hit Roll = Average of 2 random numbers (1 - 100)"))
    print_fast(format_string.format(string="---"))
    print_slowish(format_string.format(string="If the Hit  Roll is equal to or  lower than  the"))
    print_slowish(format_string.format(string="Hit Chance, the attack connects."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Damage = Might + STR - D.DEF"))
    print_fast(format_string.format(string="---"))
    print_slowish(format_string.format(string="Might is  a stat attached  to the weapon  being"))
    print_slowish(format_string.format(string="used and the strength  is the strength  of  the"))
    print_slowish(format_string.format(string="attacker.  Defense is the  defense  stat of the"))
    print_slowish(format_string.format(string="defender."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Critical Chance = SKL / 2 + 10 - D.LCK"))
    print_slowish(format_string.format(string="Critical Roll = Random Number 1 - 100"))
    print_slowish(format_string.format(string="Critical Damage = Damage * 3"))
    print_fast(format_string.format(string="---"))
    print_slowish(format_string.format(string="Critical Chance is only determined if the attack"))
    print_slowish(format_string.format(string="hits the target. If the Critical Roll  is  lower"))
    print_slowish(format_string.format(string="than the Critical  Chance, the attack  will deal"))
    print_slowish(format_string.format(string="the Critical Damage."))
    print_fast(format_string.format(string=""))
    print(bottom_border)
    time.sleep(1)
    about_battle()


def scores():
    print(top_border)
    print_fast(format_string.format(string="▶ What are points? ◀"))
    print_slowish(format_string.format(string="In  the game,  you earn  points  doing  various"))
    print_slowish(format_string.format(string="things,  such  as  defeating  enemies. To  your"))
    print_slowish(format_string.format(string="character, this is the gold you  are awarded at"))
    print_slowish(format_string.format(string="the end of the mission. You  can also  lose  or"))
    print_slowish(format_string.format(string="spend your points during the mission in various"))
    print_slowish(format_string.format(string="ways detailed below."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string="▶ Earning Points ◀"))
    print_slowish(format_string.format(string="▶ For  each enemy  defeated, you earn 10 points."))
    print_slowish(format_string.format(string="▶ For each civilian saved,  you earn  10 points."))
    print_slowish(format_string.format(string="▶ Defeating the boss  will earn  you 100 points."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string="▶ Spending Points ◀"))
    print_slowish(format_string.format(string="Wait: 5 Points."))
    print_slowish(format_string.format(string="In return,  you spend a  small  amount  of  time"))
    print_slowish(format_string.format(string="recovering  health.  After the  wait,  you  will"))
    print_slowish(format_string.format(string="from 5% to  15% of your health, up  to max  HP."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Retry: 20 points"))
    print_slowish(format_string.format(string="If you fall in battle you can spend 20 points to"))
    print_slowish(format_string.format(string="revive with full hp at the  same point you fell."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=".  .  ."))
    print_fast(format_string.format(string=""))
    print_scores_menu()
    print(bottom_border)
    time.sleep(1)
    about()


def print_scores_menu():
    with open("save_data/high_scores.txt", "r") as filestream:
        scores = []
        for line in filestream:
            currentline = line.split("\n")
            for i in range(0, len(currentline) - 1):
                scores.append(currentline[i])
        from databases import player_information
        scores.append(str(player_information.total_points))
        scores.sort(reverse=True)
        if len(scores) >= 5:
            range_max = 5
        else:
            range_max = len(scores) - 1
        if range_max == 1:
            print_slow(format_string.format(string=("Top " + str(range_max) + " Previous High Score:")))
        elif range_max == 0:
            print_slow(format_string.format(string="There are no recorded previous scores."))
        else:
            print_slow(format_string.format(string=("Top " + str(range_max) + " Previous High Scores:")))
        for i in range(0, range_max):
            print_slow(format_string.format(string=(str(i + 1) + ": " + scores[i])))


def about_magic():
    print(top_border)
    print_slowish(format_string.format(string="Magic attacks differ from  regular attacks  in a"))
    print_slowish(format_string.format(string="couple of ways:"))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Total Damage = Total Magical Might"))
    print_fast(format_string.format(string="---"))
    print_slowish(format_string.format(string="Defense plays no part in damage calculations. No"))
    print_slowish(format_string.format(string="matter what, if the magic hits, it will deal the"))
    print_slowish(format_string.format(string="same amount of damage each time it is used."))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Hit Chance is the  same as with  weapon attacks."))
    print_slowish(format_string.format(string="Each magic has its own hit rate, which varies on"))
    print_slowish(format_string.format(string="which spell you choose to cast."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Cost"))
    print_fast(format_string.format(string="------"))
    print_slowish(format_string.format(string="Every time  you cast magic,  you  use one  magic"))
    print_slowish(format_string.format(string="point.  You have a  maximum amount of  magic you"))
    print_slowish(format_string.format(string="can  have  at  any  given  time,  determined  in"))
    print_slowish(format_string.format(string="character creation. Only items can restore magic"))
    print_slowish(format_string.format(string="not even death...."))
    print_fast(format_string.format(string=""))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Spells: Electric"))
    print_fast(format_string.format(string="----------------"))
    print_slowish(format_string.format(string="Might: 25"))
    print_slowish(format_string.format(string="Hit Rate: 65"))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Spells: Ice"))
    print_fast(format_string.format(string="-----------"))
    print_slowish(format_string.format(string="Might: 20"))
    print_slowish(format_string.format(string="Hit Rate: 75"))
    print_fast(format_string.format(string=""))
    print_slowish(format_string.format(string="Spells: Fire"))
    print_fast(format_string.format(string="------------"))
    print_slowish(format_string.format(string="Might: 15"))
    print_slowish(format_string.format(string="Hit Rate: 95"))
    print_fast(format_string.format(string=""))
    print(bottom_border)
    time.sleep(1)
    about_battle()

