# databases/game_state.py
from databases import characters
from databases import rooms
from databases import player_information
from databases import items as items_module


# Map weapon/magic names back to their objects
WEAPON_MAP = {
    items_module.sword.name: items_module.sword,
    items_module.axe.name: items_module.axe,
    items_module.bow.name: items_module.bow,
    items_module.razor_axe.name: items_module.razor_axe,
}

MAGIC_MAP = {
    items_module.electric.name: items_module.electric,
    items_module.ice.name: items_module.ice,
    items_module.fire.name: items_module.fire,
}

ROOM_MAP = {room.name: room for room in rooms.room_list}
ENEMY_MAP = {e.name: e for e in characters.enemy_list}


def export_state() -> dict:
    """Create a JSON-friendly snapshot of the current game state."""
    player = characters.player

    state = {
        "player": {
            "name": player.name,
            "max_hp": player.max_hp,
            "hp": player.hp,
            "strength": player.strength,
            "defense": player.defense,
            "speed": player.speed,
            "skill": player.skill,
            "luck": player.luck,
            "magic": player.magic,
            "max_magic": player.max_magic,
            "weapons": [w.name for w in player.weapons],
            "weapon_equip": player.weapon_equip.name if player.weapon_equip else None,
            "items": list(player.items),
            "boon": player.boon,
            "bane": player.bane,
            "alive": player.alive,
        },

        "player_info": {
            "current_room": player_information.current_room.name,
            "prisoners_free": player_information.prisoners_free,
            "civilian_healed": player_information.civilian_healed,
            "total_points": player_information.total_points,
        },

        # Room-specific info that can change (items taken, room cleared, etc.)
        "rooms": {
            room.name: {
                "items": list(room.items),
                "empty": room.empty,
            }
            for room in rooms.room_list
        },

        # Enemy stats can change during combat
        "enemies": {
            e.name: {
                "max_hp": e.max_hp,
                "hp": e.hp,
                "strength": e.strength,
                "defense": e.defense,
                "speed": e.speed,
                "skill": e.skill,
                "luck": e.luck,
                "weapon": e.weapon.name if hasattr(e, "weapon") and e.weapon else None,
                "alive": e.alive,
            }
            for e in characters.enemy_list
        },
    }

    return state


def import_state(state: dict):
    """Apply a previously saved state back onto the live objects."""
    player = characters.player

    # --- Player ---
    p = state.get("player", {})
    player.name = p.get("name", player.name)
    player.max_hp = p.get("max_hp", player.max_hp)
    player.hp = p.get("hp", player.hp)
    player.strength = p.get("strength", player.strength)
    player.defense = p.get("defense", player.defense)
    player.speed = p.get("speed", player.speed)
    player.skill = p.get("skill", player.skill)
    player.luck = p.get("luck", player.luck)
    player.magic = p.get("magic", player.magic)
    player.max_magic = p.get("max_magic", player.max_magic)
    player.boon = p.get("boon", player.boon)
    player.bane = p.get("bane", player.bane)
    player.alive = p.get("alive", player.alive)

    # Rebuild weapons & equipped weapon from names
    weapon_names = p.get("weapons", [])
    player.weapons = [WEAPON_MAP[name] for name in weapon_names if name in WEAPON_MAP]

    equip_name = p.get("weapon_equip")
    if equip_name in WEAPON_MAP:
        player.weapon_equip = WEAPON_MAP[equip_name]
    elif player.weapons:
        player.weapon_equip = player.weapons[0]

    # Items are just strings
    player.items = list(p.get("items", player.items))

    # --- Player-level info ---
    pi = state.get("player_info", {})
    room_name = pi.get("current_room", player_information.current_room.name)
    if room_name in ROOM_MAP:
        player_information.current_room = ROOM_MAP[room_name]

    player_information.prisoners_free = pi.get("prisoners_free", player_information.prisoners_free)
    player_information.civilian_healed = pi.get("civilian_healed", player_information.civilian_healed)
    player_information.total_points = pi.get("total_points", player_information.total_points)

    # Keep these synced
    player_information.current_weapons = player.weapons
    player_information.current_items = player.items

    # --- Rooms ---
    rooms_state = state.get("rooms", {})
    for room_name, r_state in rooms_state.items():
        room_obj = ROOM_MAP.get(room_name)
        if not room_obj:
            continue
        room_obj.items = list(r_state.get("items", room_obj.items))
        room_obj.empty = r_state.get("empty", room_obj.empty)

    # --- Enemies ---
    enemies_state = state.get("enemies", {})
    for enemy_name, e_state in enemies_state.items():
        enemy_obj = ENEMY_MAP.get(enemy_name)
        if not enemy_obj:
            continue

        enemy_obj.max_hp = e_state.get("max_hp", enemy_obj.max_hp)
        enemy_obj.hp = e_state.get("hp", enemy_obj.hp)
        enemy_obj.strength = e_state.get("strength", enemy_obj.strength)
        enemy_obj.defense = e_state.get("defense", enemy_obj.defense)
        enemy_obj.speed = e_state.get("speed", enemy_obj.speed)
        enemy_obj.skill = e_state.get("skill", enemy_obj.skill)
        enemy_obj.luck = e_state.get("luck", enemy_obj.luck)
        enemy_obj.alive = e_state.get("alive", enemy_obj.alive)

        w_name = e_state.get("weapon")
        if w_name in WEAPON_MAP:
            enemy_obj.weapon = WEAPON_MAP[w_name]
