import databases.player_information
import functions.print_speed
from databases.items import axe, bow

data = databases.player_information
p = functions.print_speed

format_string_center = '{string:^43}'
format_string_right = '{string:>43}'


def search():
    from story_materials.enter_room import action_prompt
    if not data.current_room.items:
        string = "You rummage through the room and you find nothing."
        p.print_slow(format_string_center.format(string=string))
    else:
        string = "You rummage through  the room and you find:"
        p.print_slow(format_string_center.format(string=string))
        items = data.current_room.items
        count_items(items)
        for i in range(0, len(data.current_room.items)):
            if data.current_room.items[i] == "Axe":
                data.current_weapons.append(axe)
            elif data.current_room.items[i] == "Bow":
                data.current_weapons.append(bow)
            elif data.current_room.items[i] == "S.Ring":
                p.print_slow(format_string_center.format(string="\nYou find a Strength Ring that"
                                                                "permanently\nincreases your strength by 1."))
                data.strength += 1
            elif data.current_room.items[i] == "D.Necklace":
                p.print_slow(format_string_center.format(string="\nYou find a Defense Necklace that"
                                                                "permanently\nincreases your defense by 1."))
                data.defense += 1
            else:
                data.current_items.append(data.current_room.items[i])
        p.print_slow(format_string_center.format(string="\nAfter you collect  what you can,  "
                                                        "your  bag\nof items holds: "))
        print_bag()
        data.current_room.items.clear()


def print_bag():
    player_weapons = data.current_weapons
    p.print_fast(format_string_right.format(string="Items"))
    p.print_fast(format_string_right.format(string="-------"))
    count_items(data.current_items)
    print()
    p.print_fast(format_string_right.format(string="Weapons"))
    p.print_fast(format_string_right.format(string="-------"))
    for i in range(len(player_weapons)):
        weapon_str = "1 " + player_weapons[i].name
        p.print_slow(format_string_right.format(string=weapon_str))


def count_items(items):
    final_list = list(dict.fromkeys(items))
    length = len(final_list)
    for i in range(length):
        count = items.count(final_list[i])
        if count == 1:
            p.print_fast(format_string_right.format(string=(str(count) + " " + final_list[i])))
        else:
            p.print_fast(format_string_right.format(string=(str(count) + " " + final_list[i] + "s")))
