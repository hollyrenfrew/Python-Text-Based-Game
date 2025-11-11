import math
from random import randint


def two_round(player, enemy):
    player_turn = player.speed + randint(1, 10)
    enemy_turn = enemy.speed + randint(1, 10)
    while player_turn == enemy_turn:
        player_turn = player.speed + randint(1, 10)
        enemy_turn = enemy.speed + randint(1, 10)
    if player_turn > enemy_turn:
        return [player.name, enemy.name]
    else:
        return [enemy.name, player.name]


def three_round(player, enemy1, enemy2):
    player_turn = player.speed + randint(1, 10)
    enemy1_turn = enemy1.speed + randint(1, 10)
    enemy2_turn = enemy2.speed + randint(1, 10)
    while player_turn in [enemy1_turn, enemy2_turn]:
        player_turn = player.speed + randint(1, 10)
        enemy1_turn = enemy1.speed + randint(1, 10)
        enemy2_turn = enemy2.speed + randint(1, 10)
    initiatives = {
        enemy1.name: enemy1_turn,
        enemy2.name: enemy2_turn,
        player.name: player_turn
    }
    order = [enemy2.name, enemy1.name, player.name]
    order = sorted(order, key=lambda x: initiatives[x])
    order.reverse()
    return order


def attack(hit_chance):
    hit_roll = (randint(1, 100) + randint(1, 100)) / 2
    if hit_chance >= hit_roll:
        return True
    else:
        return False


def hit_rate(attacker, defender, weapon):
    hit_rate = (attacker.skill * 1.5) + attacker.luck * 0.5 + weapon.hit
    avoid = (defender.speed * 3 + defender.luck) / 2
    hit_chance = hit_rate - avoid
    return hit_chance


def hit_rate_display(hit_rate_given):
    if hit_rate_given >= 100:
        return 100
    elif hit_rate_given <= 0:
        return 0
    else:
        return int(math.floor(hit_rate_given))


def damage(attacker, defender, weapon):
    total_damage = (attacker.strength + weapon.might) - defender.defense
    return total_damage


def critical_rate(attacker, defender):
    critical_chance = (attacker.skill / 2 + 10) - defender.luck
    return critical_chance


def crit_rate_display(crit_rate_given):
    if crit_rate_given >= 100:
        return 100
    elif crit_rate_given <= 0:
        return 0
    else:
        return int(math.floor(crit_rate_given))


def critical(critical_chance):
    critical_roll = randint(1, 100)
    if critical_chance >= critical_roll:
        return True
    else:
        return False


def crit_damage(normal_damage):
    critical_damage = normal_damage * 3
    return critical_damage


def magic_damage(magic):
    return magic.might
