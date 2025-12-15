import time
import pygame

from databases import player_information
from databases.player_information import room_actions, print_actions
from functions.battle_flow import three_battle, two_battle
from game_controls.move_between_rooms import move
from game_controls.search import search
from game_controls.use_item import use_item
from game_controls.wait import wait
from functions.print_speed import print_slow, print_fast, print_slowish
from story_materials import special_rooms

format_string_center = '{string:^43}'
audio1 = "music/tower_defense.mp3"
audio2 = "music/move_it_out.mp3"


def enter_room():
    pygame.mixer.music.fadeout(3000)
    pygame.mixer.music.load(audio1)
    pygame.mixer.music.play(-1, 0, 3000)
    time.sleep(2)
    print_slow(format_string_center.format(string=player_information.current_room.description))
    if not player_information.current_room.empty:
        print_slow(format_string_center.format(string=player_information.current_room.description_enemy))
        print_fast(format_string_center.format(string=""))
        print_fast(format_string_center.format(string=".  .  ."))
        print_fast(format_string_center.format(string=""))
        pygame.mixer.music.fadeout(3000)
        pygame.mixer.music.load(audio2)
        pygame.mixer.music.play(-1, 0, 3000)
        if len(player_information.current_room.enemies) > 1:
            three_battle()
        elif len(player_information.current_room.enemies) == 1:
            two_battle()
        pygame.mixer.music.fadeout(3000)
        pygame.mixer.music.load(audio1)
        pygame.mixer.music.play(-1, 0, 3000)
        time.sleep(2)
        player_information.current_room.empty = True
    print_fast(format_string_center.format(string=""))
    print_fast(format_string_center.format(string=".  .  ."))
    print_fast(format_string_center.format(string=""))
    print_slow(format_string_center.format(string=player_information.current_room.description_empty))
    print_fast(format_string_center.format(string=".  .  ."))
    print_fast(format_string_center.format(string=""))
    action_prompt()


def action_prompt():
    print_slow(
        format_string_center.format(string=("You are currently in " + player_information.current_room.name + ".")))
    special_room_check()
    print_slowish(format_string_center.format(string="What would you like to do?"))
    print_actions()
    user_input = input("> ").capitalize().strip()
    while user_input not in room_actions:
        print_slowish(format_string_center.format(string="Please enter one of the following choices:"))
        print_actions()
        user_input = input("> ").capitalize().strip()
    if user_input == "Move":
        move()
    elif user_input == "Search":
        search()
    elif user_input == "Item":
        use_item()
    elif user_input == "Wait":
        wait()
    action_prompt()


def special_room_check():
    room = player_information.current_room.name
    if room == "Prisoner Hold":
        special_rooms.special_prison()
    if room == "Dormitory":
        special_rooms.special_dormitory()
    if room == "Infirmary":
        special_rooms.special_infirmary()
    if room == "Razorfang's Room":
        special_rooms.boss_battle()
