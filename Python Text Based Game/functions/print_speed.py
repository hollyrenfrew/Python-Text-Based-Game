import random
import time


normal_speed = 7500


def print_slow(string):
    speed = normal_speed
    for char in string:
        print(char, end='', flush=True)
        time.sleep(random.random() * 10.0 / (10 * speed))
    print('')


def print_slowish(string):
    speed = normal_speed * 2
    for char in string:
        print(char, end='', flush=True)
        time.sleep(random.random() * 10.0 / (10 * speed))
    print('')


def print_fast(string):
    speed = normal_speed * 10
    for char in string:
        print(char, end='', flush=True)
        time.sleep(random.random() * 10.0 / (10 * speed))
    print('')


