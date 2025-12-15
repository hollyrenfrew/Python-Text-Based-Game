from databases import player_information
from databases.rooms import *
from functions.battle_calculations import *
from functions.list_to_string import list_to_string
from functions.print_speed import *
from game_controls.use_item import use_item


format_string_left = '{string:<43}'
format_string_right = '{string:>43}'
format_string_center = '{string:^43}'


def two_battle():
    time.sleep(2)
    enemy = player_information.current_room.enemies[0]
    while enemy.alive and player.alive:
        order = two_round(player, enemy)
        print_order = list_to_string(order, ", ")
        player_hp = (player.name + ":" + str(player.hp) + "/" + str(player.max_hp)
                     + " MAG:(" + str(player.magic) + "/" + str(player.max_magic) + ")")
        enemy_hp = enemy.name + ":" + str(enemy.hp) + "/" + str(enemy.max_hp)
        print_fast(format_string_center.format(string="New round beginning now..."))
        print_fast(format_string_center.format(string="--------------------------"))
        # Print Turn Order so Player can see
        print_fast(format_string_right.format(string="Turn Order:"))
        print_fast(format_string_right.format(string=print_order))
        print_fast(format_string_right.format(string=""))

        # Print HP MP so player can keep track
        print_fast(format_string_left.format(string=player_hp))
        print_fast(format_string_left.format(string=enemy_hp))

        while order:
            if order[0] == player.name:
                player_turn()
            else:
                enemy_attack(enemy)
            order.pop(0)
            check(player)
            check(enemy)
            if not player.alive or not enemy.alive:
                if not player.alive:
                    from screens.game_over import game_over
                    game_over()
                else:
                    print("You won!")
                    player_information.current_room.enemies.pop(0)
                    player_information.current_room.empty = True
                    player_information.total_points += 10
                    break
                break


def three_battle():
    enemy1 = player_information.current_room.enemies[0]
    enemy2 = player_information.current_room.enemies[1]
    while enemy1.alive and enemy2.alive and player.alive:
        order = three_round(player, enemy1, enemy2)
        print_order = list_to_string(order, ", ")
        player_hp = (player.name + ":" + str(player.hp) + "/" + str(player.max_hp)
                     + " (" + str(player.magic) + "/" + str(player.max_magic) + ")")
        enemy1_hp = enemy1.name + ":" + str(enemy1.hp) + "/" + str(enemy1.max_hp)
        enemy2_hp = enemy2.name + ":" + str(enemy2.hp) + "/" + str(enemy2.max_hp)
        print_fast(format_string_center.format(string="New round beginning now..."))
        print_fast(format_string_center.format(string="--------------------------"))

        # Print Turn Order so Player can see
        print_fast(format_string_right.format(string="Turn Order:"))
        print_fast(format_string_right.format(string=print_order))
        print_fast(format_string_right.format(string=""))

        # Print HP so player can keep track
        print_fast(format_string_left.format(string=player_hp))
        print_fast(format_string_left.format(string=enemy1_hp))
        print_fast(format_string_left.format(string=enemy2_hp))
        while order:
            if order[0] == player.name:
                player_turn()
            elif order[0] == enemy1.name:
                enemy_attack(enemy1)
            elif order[0] == enemy2.name:
                enemy_attack(enemy2)
            order.pop(0)
            check(enemy1)
            check(enemy2)
            check(player)
            if not player.alive or not enemy1.alive or not enemy2.alive:
                if not player.alive:
                    from screens.game_over import game_over
                    game_over()
                elif not enemy1.alive:
                    player_information.current_room.enemies.pop(0)
                    player_information.total_points += 10
                    two_battle()
                elif not enemy2.alive:
                    player_information.current_room.enemies.pop(1)
                    player_information.total_points += 10
                    two_battle()
                break


def check(character):
    if character.hp <= 0:
        character.alive = False


def player_turn():
    action_list = player_information.actions
    action_string = list_to_string(player_information.actions, ", ")
    print_slow(format_string_center.format(string="What would you like to do?"))
    print_slow(format_string_center.format(string=action_string))
    action = input("> ")
    action = action.strip().capitalize()
    while action not in action_list:
        print_slow(format_string_center.format(string="Please enter one of the following options:"))
        print_slow(format_string_center.format(string=action_string))
        action = input("> ")
        action = action.strip().capitalize()
    if action == "Attack":
        if len(player_information.current_room.enemies) == 1:
            enemy = player_information.current_room.enemies[0]
            # returns damage calculated attacking enemy at index 0
            attack_single_target(enemy)
        else:
            enemy1 = player_information.current_room.enemies[0]
            enemy2 = player_information.current_room.enemies[1]
            attack_multiple_target(enemy1, enemy2)
    elif action == "Magic":
        if not check_magic():
            player_turn()
        else:
            if len(player_information.current_room.enemies) == 1:
                enemy = player_information.current_room.enemies[0]
                magic_attack(enemy)
            else:
                enemy1 = player_information.current_room.enemies[0]
                enemy2 = player_information.current_room.enemies[1]
                magic_multiple_enemies(enemy1, enemy2)
    elif action == "Item":
        use_item()


def attack_single_target(enemy):
    # check to see if the player has more than 1 weapon
    if len(player.weapons) > 1:
        weapon_string = ""
        weapon_list = []
        # create a display list and list to compare weapon names to user input
        for i in range(0, len(player.weapons) - 1):
            weapon_string = weapon_string + getattr(player.weapons[i], "name") + ", "
            weapon_list.append(getattr(player.weapons[i], "name"))
        weapon_string = weapon_string + getattr(player.weapons[len(player.weapons) - 1], "name")
        weapon_list.append(getattr(player.weapons[len(player.weapons) - 1], "name"))
        print_slow(format_string_center.format(string="Which weapon will you use?"))
        print_slow(format_string_center.format(string=weapon_string))
        print_slow(format_string_center.format(string="(back)"))
        equip_weapon = input("> ")
        equip_weapon = equip_weapon.strip().capitalize()
        if equip_weapon == "Bow":
            if not check_arrows():
                equip_weapon = ""
        while equip_weapon not in weapon_list and equip_weapon != "Back":
            print_slow(format_string_center.format(string="Please enter one of the following:"))
            print_slow(format_string_center.format(string=weapon_string))
            print_slow(format_string_center.format(string="(back)"))
            equip_weapon = input("> ")
            equip_weapon = equip_weapon.strip().capitalize()
            if equip_weapon == "Back":
                player_turn()
            if equip_weapon == "Bow":
                if not check_arrows():
                    equip_weapon = ""
        # assigns equip weapon to the weapon object with the same name attribute
        player.weapon_equip = next((i for i in player.weapons if i.name == equip_weapon), None)
    else:
        # else weapon is first weapon
        player.weapon_equip = player.weapons[0]
        equip_weapon = player.weapon_equip.name
    # display chosen weapon for player
    print_slow(
        format_string_center.format(string=("You attacked " + enemy.name + " with your " + equip_weapon.lower() + "!")))
    print_slow(format_string_center.format(string=""))
    if player.weapon_equip.name == "Bow":
        player_calculations(enemy)
    player_calculations(enemy)


def player_calculations(enemy):
    # calculate percentages
    hit_chance = hit_rate(player, enemy, player.weapon_equip)
    crit_rate = critical_rate(player, enemy)

    # round and prepare for display for player
    hit_chance_rate = hit_rate_display(hit_chance)
    crit_rate_display(crit_rate)

    # display percentages for player
    print_slow(format_string_center.format(string=("Hit Rate: " + str(hit_chance_rate) + "%")))
    print_slow(format_string_center.format(string=("Critical Rate: " + str(crit_rate) + "%")))
    print_slow(format_string_center.format(string=""))
    print_slow(format_string_center.format(string=".  .  ."))
    print_slow(format_string_center.format(string=""))
    if attack(hit_chance):
        # if hit, display and calculate damage
        total_damage = damage(player, enemy, player.weapon_equip)
        # only if the player lands the hit, critical hit is determined
        if critical(crit_rate):
            print_slow(format_string_center.format(string="Lining  up  your  strike,  you"))
            print_slow(format_string_center.format(string="manage to hit a critical spot!"))
            # update total damage for critical damage
            total_damage = crit_damage(total_damage)
        else:
            # not critical, displays a simple hit message.
            print_slow(format_string_center.format(string=("You hit " + enemy.name + "!")))
        print_slow(format_string_center.format(string=("You dealt " + str(total_damage) + " to " + enemy.name + "!")))
        print_slow(format_string_center.format(string=""))
        print_slow(format_string_center.format(string=".  .  ."))
        print_slow(format_string_center.format(string=""))
    else:
        print_slow(format_string_center.format(string=("You missed " + enemy.name + "!")))
        print_slow(format_string_center.format(string=""))
        print_slow(format_string_center.format(string=".  .  ."))
        print_slow(format_string_center.format(string=""))
        total_damage = 0
    enemy.hp = enemy.hp - total_damage


def attack_multiple_target(enemy1, enemy2):
    print_slow(format_string_center.format(string="Which enemy would you like to attack?"))
    print_slow(format_string_center.format(string="1: " + enemy1.name + " (HP: " + str(enemy1.hp) + ")"))
    print_slow(format_string_center.format(string="2: " + enemy2.name + " (HP: " + str(enemy2.hp) + ")"))
    print_fast(format_string_center.format(string=""))
    choice = input("> ").strip().lower()
    while choice not in ["1", "2"]:
        print_slow(format_string_center.format(string="Please enter a single number."))
        print_slow(format_string_center.format(string="1: " + enemy1.name + " (HP: " + str(enemy1.hp) + ")"))
        print_slow(format_string_center.format(string="2: " + enemy2.name + " (HP: " + str(enemy2.hp) + ")"))
        print_fast(format_string_center.format(string=""))
        choice = input("> ").strip().lower()
    if choice == "1":
        attack_single_target(enemy1)
    if choice == "2":
        attack_single_target(enemy2)


def enemy_attack(enemy):
    print(enemy.name + " attacked!")
    # calculate percentages
    hit_chance = hit_rate(enemy, player, enemy.weapon)
    crit_rate = critical_rate(enemy, player)

    # round and prepare for display for player
    hit_chance_rate = hit_rate_display(hit_chance)
    crit_rate_display(crit_rate)

    # display percentages for player
    print_slow(format_string_center.format(string=("Hit Rate: " + str(hit_chance_rate) + "%")))
    print_slow(format_string_center.format(string=("Critical Rate: " + str(crit_rate) + "%")))
    print_slow(format_string_center.format(string=""))
    print_slow(format_string_center.format(string=".  .  ."))
    print_slow(format_string_center.format(string=""))
    if attack(hit_chance):
        # if hit, display and calculate damage
        total_damage = damage(enemy, player, enemy.weapon)
        # only if the player lands the hit, critical hit is determined
        if critical(crit_rate):
            print_slow(format_string_center.format(string="With  a flash  of  light,  the"))
            print_slow(format_string_center.format(string="enemy's weapon hits a critical"))
            print_slow(format_string_center.format(string="spot  and wounds you  greatly!"))
            # update total damage for critical damage
            total_damage = crit_damage(total_damage)
        else:
            # not critical, displays a simple hit message.
            print_slow(format_string_center.format(string=(enemy.name + " slashes at you!")))
        print_slow(format_string_center.format(string=("They dealt " + str(total_damage) + " to you!")))
        print_slow(format_string_center.format(string=""))
        print_slow(format_string_center.format(string=".  .  ."))
        print_slow(format_string_center.format(string=""))
    else:
        print_slow(format_string_center.format(string=(enemy.name + " swung to hit you and missed!")))
        print_slow(format_string_center.format(string=""))
        print_slow(format_string_center.format(string=".  .  ."))
        print_slow(format_string_center.format(string=""))
        total_damage = 0
    player.hp = player.hp - total_damage


def check_arrows():
    arrows = player.items.count("Arrow")
    arrow_string = "You have " + str(arrows) + " arrows in your bag."
    print_slow(format_string_center.format(string=arrow_string))
    if arrows < 2:
        print_slow(format_string_center.format(string="You need 2 arrows to use your bow."))
        print_slow(format_string_center.format(string="You don't have enough arrows.\n"))
        print_fast(format_string_center.format(string=".  .  ."))
        return False
    else:
        player.items.remove("Arrow")
        player.items.remove("Arrow")
        return True


def check_magic():
    if player.magic <= 0:
        print_slow(format_string_center.format(string="You're out of magic points! You can't use magic now.\n"))
        return False
    else:
        return True


def magic_attack(enemy):
    known_magic = ["Ice", "Fire", "Electric"]
    list_magic = list_to_string(known_magic, ", ")
    print_slow(format_string_center.format(string="Choose which spell you would like to use:"))
    print_slow(format_string_center.format(string=list_magic))
    print_slow(format_string_center.format(string="(back)"))
    magic_choice = input("> ").capitalize().strip()
    while magic_choice not in known_magic and magic_choice != "Back":
        print_slow(format_string_center.format(string="Choose which spell you would like to use:"))
        print_slow(format_string_center.format(string=list_magic))
        print_slow(format_string_center.format(string="(back)"))
        magic_choice = input("> ").capitalize().strip()
    if magic_choice == "Back":
        player_turn()
    else:
        player.magic -= 1
        if magic_choice == "Ice":
            magic_choice = ice
        elif magic_choice == "Electric":
            magic_choice = electric
        elif magic_choice == "Fire":
            magic_choice = fire
        else:
            print_slow(format_string_center.format(string="An error occurred. Returning to player turn start..."))
            player_turn()
        hit_chance = hit_rate(player, enemy, magic_choice)
        hit_chance_rate = hit_rate_display(hit_chance)
        print_slow(format_string_center.format(string=("Hit Rate: " + str(hit_chance_rate) + "%")))
        print_slow(format_string_center.format(string=""))
        print_slow(format_string_center.format(string=".  .  ."))
        print_slow(format_string_center.format(string=""))
        if attack(hit_chance):
            # if hit, display and calculate damage
            total_damage = magic_damage(magic_choice)
            print_slow(format_string_center.format(string=("You hit " + enemy.name + " with your "
                                                           + magic_choice.name + " attack!")))
            print_slow(format_string_center.format(string=("You dealt " + str(total_damage)
                                                           + " to " + enemy.name + "!")))
            print_slow(format_string_center.format(string=""))
            print_slow(format_string_center.format(string=".  .  ."))
            print_slow(format_string_center.format(string=""))
        else:
            print_slow(format_string_center.format(string=("You missed " + enemy.name + "!")))
            print_slow(format_string_center.format(string=""))
            print_slow(format_string_center.format(string=".  .  ."))
            print_slow(format_string_center.format(string=""))
            total_damage = 0
        enemy.hp = enemy.hp - total_damage


def magic_multiple_enemies(enemy1, enemy2):
    print_slow(format_string_center.format(string="Which enemy would you like to attack?"))
    print_slow(format_string_center.format(string="1: " + enemy1.name + " (HP: " + str(enemy1.hp) + ")"))
    print_slow(format_string_center.format(string="2: " + enemy2.name + " (HP: " + str(enemy2.hp) + ")"))
    print_fast(format_string_center.format(string=""))
    choice = input("> ").strip().lower()
    while choice not in ["1", "2"]:
        print_slow(format_string_center.format(string="Please enter a single number."))
        print_slow(format_string_center.format(string="1: " + enemy1.name + " (HP: " + str(enemy1.hp) + ")"))
        print_slow(format_string_center.format(string="2: " + enemy2.name + " (HP: " + str(enemy2.hp) + ")"))
        print_fast(format_string_center.format(string=""))
        choice = input("> ").strip().lower()
    if choice == "1":
        magic_attack(enemy1)
    if choice == "2":
        magic_attack(enemy2)
