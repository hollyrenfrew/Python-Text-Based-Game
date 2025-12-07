import time

import json
import pygame

from databases import player_information
from databases.characters import player
from databases.player_information import room_actions, print_actions
from functions.battle_flow import three_battle, two_battle
from game_controls.move_between_rooms import move
from game_controls.search import search
from game_controls.use_item import use_item
from game_controls.wait import wait
from functions.print_speed import print_slow, print_fast, print_slowish
from story_materials import special_rooms
from save_system import save_game, get_save_by_name, update_save
from databases.game_state import export_state

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
    elif user_input == "Save":
        # --- CONFIRM SAVE & QUIT ---
        print_slowish(format_string_center.format(
            string="Are you sure you want to save and quit? (Yes / No)"
        ))
        confirm = input("> ").strip().lower()

        while confirm not in ["yes", "no"]:
            print_slowish(format_string_center.format(
                string="Please enter Yes or No."
            ))
            confirm = input("> ").strip().lower()

        if confirm == "no":
            print_slowish(format_string_center.format(string="Save cancelled."))
            time.sleep(0.5)
            action_prompt()
            return

        # --- SHOW PREVIEW OF CURRENT STATE ---
        current_state = export_state()
        curr_room = player_information.current_room.name
        curr_hp = player.hp
        curr_max_hp = player.max_hp
        curr_points = player_information.total_points

        print_fast(format_string_center.format(string="Current game preview:"))
        print_fast(format_string_center.format(
            string=f"Room: {curr_room}"
        ))
        print_fast(format_string_center.format(
            string=f"HP: {curr_hp}/{curr_max_hp}"
        ))
        print_fast(format_string_center.format(
            string=f"Points: {curr_points}"
        ))
        print_fast(format_string_center.format(string=""))

        # --- CHOOSE SAVE SLOT NAME ---
        save_name = input("Choose a save slot name (blank = 'Autosave'): ").strip()
        if not save_name:
            save_name = "Autosave"

        # --- CHECK IF THIS SLOT ALREADY EXISTS ---
        existing = get_save_by_name(save_name)

        if existing:
            existing_id, existing_name, existing_created, existing_data_json = existing
            try:
                existing_state = json.loads(existing_data_json)
            except json.JSONDecodeError:
                existing_state = None

            print_fast(format_string_center.format(string=""))
            print_fast(format_string_center.format(string=f"Slot '{existing_name}' already exists."))
            print_fast(format_string_center.format(
                string=f"Last saved: {existing_created}"
            ))

            # Show a brief preview of the existing slot, if we could decode it
            if existing_state:
                ex_p = existing_state.get("player", {})
                ex_pi = existing_state.get("player_info", {})
                ex_room = ex_pi.get("current_room", "Unknown")
                ex_hp = ex_p.get("hp", "?")
                ex_max_hp = ex_p.get("max_hp", "?")
                ex_points = ex_pi.get("total_points", "?")

                print_fast(format_string_center.format(string="Existing slot preview:"))
                print_fast(format_string_center.format(
                    string=f"Room: {ex_room}"
                ))
                print_fast(format_string_center.format(
                    string=f"HP: {ex_hp}/{ex_max_hp}"
                ))
                print_fast(format_string_center.format(
                    string=f"Points: {ex_points}"
                ))

            print_fast(format_string_center.format(string=""))
            print_slowish(format_string_center.format(
                string="Overwrite this save slot? (Yes / No)"
            ))
            overwrite = input("> ").strip().lower()

            while overwrite not in ["yes", "no"]:
                print_slowish(format_string_center.format(
                    string="Please enter Yes or No."
                ))
                overwrite = input("> ").strip().lower()

            if overwrite == "no":
                print_slowish(format_string_center.format(string="Save cancelled."))
                time.sleep(0.5)
                action_prompt()
                return

            # Overwrite existing slot
            update_save(existing_id, current_state, save_name)
            print_slowish(format_string_center.format(
                string=f"Slot '{save_name}' overwritten. Returning to title..."
            ))
        else:
            # Fresh save slot
            save_game(current_state, save_name)
            print_slowish(format_string_center.format(
                string=f"Game saved as '{save_name}'. Returning to title..."
            ))

        time.sleep(1)

        # Avoid circular imports at file top
        from screens.menus import title
        title()
        return
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
