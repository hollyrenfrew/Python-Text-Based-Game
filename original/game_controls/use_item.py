from databases.characters import player
from databases.player_information import current_items
from functions.print_speed import print_slow, print_fast
from game_controls.search import print_bag

format_string_center = '{string:^43}'
format_string_left = '{string:<43}'
format_string_right = '{string:>43}'



def use_item():
    unusable_items = ["Arrow", "Arrows", "Key", "Keys", "BossKey", "BossKeys"]
    while current_items:
        print_bag()
        print_slow(
            format_string_center.format(string="What item would you like to use? \n(Enter exit to leave this menu)"))
        item = input("> ").capitalize().strip()
        while item != "Exit":
            if item not in current_items:
                print_slow(format_string_left.format(string="Please enter an item from your bag:"))
                print_bag()
                item = input("> ").capitalize().strip()
            if item == "Bandage" or item == "Bandages":
                health = player.hp
                if player.hp >= player.max_hp - 10:
                    new_health = player.max_hp
                else:
                    new_health = player.hp + 10
                print_slow(format_string_center.format(string="Your health before you use a bandage:"))
                print_slow(format_string_center.format(string=(str(health) + "/" + str(player.max_hp))))
                print_slow(format_string_center.format(string="Your health after you use a bandage:"))
                print_slow(format_string_center.format(string=(str(new_health) + "/" + str(player.max_hp))))
                print_slow(format_string_center.format(string="Are you sure you want to use this item?"))
                answer = input("> ").lower().strip()
                while answer not in ["yes", "no"]:
                    print_slow(format_string_center.format(string="Please enter yes or no."))
                    answer = input("> ").lower().strip()
                if answer == "yes":
                    player.hp = new_health
                    current_items.remove("Bandage")
                break
            elif item in unusable_items:
                print_fast(format_string_center.format(string=".  .  ."))
                print_slow(format_string_center.format(string="You cannot use that item right now."))
                print_fast(format_string_center.format(string=".  .  ."))
                item = ""
            elif item == "Bead":
                magic = player.magic
                if player.magic >= player.max_magic - 1:
                    new_magic = player.max_magic
                else:
                    new_magic = player.magic + 1
                print_slow(format_string_center.format(string="Your magic points before you use a magic bead:"))
                print_slow(format_string_center.format(string=(str(magic) + "/" + str(player.max_magic))))
                print_slow(format_string_center.format(string="Your health after you use a bandage:"))
                print_slow(format_string_center.format(string=(str(new_magic) + "/" + str(player.max_magic))))
                print_slow(format_string_center.format(string="Are you sure you want to use this item?"))
                answer = input("> ").lower().strip()
                while answer not in ["yes", "no"]:
                    print_slow(format_string_center.format(string="Please enter yes or no."))
                    answer = input("> ").lower().strip()
                if answer == "yes":
                    player.magic = new_magic
                    current_items.remove("Magic Bead")
                break
        break
    if not current_items:
        print_fast(format_string_center.format(string="Your bag is empty."))
    print_fast(format_string_center.format(string=".  .  ."))


