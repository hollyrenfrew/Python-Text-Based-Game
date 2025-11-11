import os

from databases import player_information
from databases.characters import player, razor_fang
from databases.rooms import dormitory, razor
from functions.battle_flow import two_battle
from functions.print_speed import print_slow, print_fast

format_string_center = '{string:^43}'

def special_prison():
    if not player_information.prisoners_free:
        prisoners = ("There seems  to be five people  behind bars,\n"
                     "but you cannot  seem to open the  gateway to\n"
                     "free them.  Perhaps you need  a key to  open\n"
                     "the door.\n")

    else:
        prisoners = ("There  is  an  empty  cell.   You freed  the\n"
                     "prisoners from here before.\n")
    print_slow(format_string_center.format(string=prisoners))
    if "Prison Key" in player_information.current_items:
        use_key = ("You have the prison  key, do you use it to\n"
                   "free the prisoners?\n")
        print_slow(format_string_center.format(string=use_key))
        answer = input("> ").lower().strip()
        while answer not in ["yes", "no"]:
            print_slow(format_string_center.format(string="Please enter yes or no."))
            answer = input("> ").lower().strip()
        free_prisoners = ""
        if answer == "yes":
            player_information.current_items.remove("Prison Key")
            player_information.prisoners_free = True
            free_prisoners = ("You use the prison  key on the jail cell and\n"
                              "it creaks open. The  five prisoners  look at\n"
                              "you before hurrying out. One stays behind to\n"
                              "shake your hand.\n\n"
                              "\"Thank you,\" the old  man says  with a small\n"
                              "smile and a twinkle  in his  eyes. \"I  heard\n"
                              "the guards  talking earlier.  If you're here\n"
                              "for Razorfang, you'll have  to find a key to\n"
                              "enter his room. I think  they mentioned that\n"
                              "the... second in command?  -  That's right!\"\n\n"
                              "\"They  said the  second  had the  key to the\n"
                              "room and no one was to disturb him while  he\n"
                              "planned another assault on Fayhaven.  I fear\n"
                              "we won't be safe unless you take care of him\n"
                              "for  us. Thank  you  again...  I think their\n"
                              "second was 'counting gold'  so maybe  you'll\n"
                              "find him in a  treasure  room of some sort.\"\n\n"
                              "The old  man gives you  one last look before\n"
                              "leaving  you  with   one  more   statement.\n\n"
                              "\"You remind  me a lot of  your father.  Keep\n"
                              "up the  good  work and  you'll be one of the\n"
                              "best  warriors  around,  just  like  he  had\n"
                              "been.\"  Then,  the old  man  leaves  without\n"
                              "another word.\n")
            player_information.total_points += 50
        elif answer == "no":
            free_prisoners = "You  decided  not  to  free  the  prisoners.\n"
        print_slow(format_string_center.format(string=free_prisoners))


def special_dormitory():
    if "Boss Key" not in player_information.current_items:
        door_message = ("There is a door to the east that seems to be\n"
                        "locked. Perhaps you need a key...")
    else:
        door_message = ("You have  the key to the room to the east if\n"
                        "you wish to go that way.")
        dormitory.directions.append("East")
        dormitory.directions.remove("Cancel")
        dormitory.directions.append("Cancel")
    print()
    print_slow(format_string_center.format(string=door_message))
    print()


def special_infirmary():
    if player_information.civilian_healed:
        civ = "The civilians you helped  earlier  has left."
    else:
        civ = ("There seems to be two civilians on a cot who\n"
               "seem to be heavily injured...  if  you had a\n"
               "bandage, maybe you could help them.\n")
    print_slow(format_string_center.format(string=civ))
    if not player_information.civilian_healed:
        if "Bandage" not in player_information.current_items:
            print_slow(format_string_center.format(string="It's too bad you don't have a bandage."))
        else:
            bandage = ("You do  have a bandage on you.  Will you use\n"
                       "it to help the civilians?")
            print_slow(format_string_center.format(string=bandage))
            answer = input("> ").strip().lower()
            while answer not in ["yes", "no"]:
                print_slow(format_string_center.format(string="Please enter yes or no."))
                answer = input("> ").strip().lower()
            if answer == "yes":
                player_information.current_items.remove("Bandage")
                player_information.civilian_healed = True
                player_information.current_items.append("Magic Bead")
                player_information.total_points += 20
                message = ("As you walk up to offer your bandage, one of\n"
                           "the injured looks up and notices you. A wave\n"
                           "of relief  seems  to wash  over their  face.\n"
                           "\"Oh, thank  you  so   much.   When  we  were\n"
                           "separated from the others, I thought we were\n"
                           "goners. They just threw us in here.  I think\n"
                           "they forgot about us, but  we're too injured\n"
                           "to escape on our own...\"\n\n"
                           "\"Oh, my name is Phillip, by the way. And you\n"
                           "are called...?\"\n\n"
                           "\"Ah, " + player.name + " that's a great name. Once  more,\n"
                                                    "thank you. I should  be able to  patch myself\n"
                                                    "and my sister  here up with this.  We'll  try\n"
                                                    "to get out  as soon as  possible.  Take this,\n"
                                                    "it'll help.\"\n\n"
                                                    "Phillip  hands  you one  Magic  Bead that you\n"
                                                    "tuck into your bag.\n\n"
                                                    "After you make sure that Phillip and his sister\n"
                                                    "are  able to  leave on  their own,  you prepare\n"
                                                    "yourself  for  the  rest  of  your   journey...\n")
            else:
                message = "You decide to ignore the civilian and move on."
            print_slow(format_string_center.format(string=message))


def boss_battle():
    player_information.current_room = razor
    string = """
As you enter the  final room of your journey, 
you see  a large man  standing before you. He
stands at least two feet taller  than you and
he  sports a  nasty  looking  scar across his
face. This  man, Razorfang,  presumably,  has
definitely been in his fair share of battles.

"Heh,  I was  wondering  when you'd  make  it
here,  kid." Razorfang hoists  up his massive
axe, holding it over his shoulder, a grin on
his  face. "So, you  want to fight  or what?"
"""
    print_slow(format_string_center.format(string=string))
    print_slow(format_string_center.format(string="Begin the fight?"))
    answer = input("> ").strip().lower()
    while answer not in ["yes", "no"]:
        print_slow(format_string_center.format(string="Enter yes or no."))
    if answer == "yes":
        battle_boss()
    else:
        string = """
"Eh? What's  the matter?  Scared?"  Razorfang
looks over you with a curious look.
"""
        print_slow(format_string_center.format(string=string))
        print_slow(format_string_center.format(string="What do you say in reply?"))
        print_slow(format_string_center.format(string="1) Never-mind, let's fight!"))
        print_slow(format_string_center.format(string="2) Why are you doing this?"))
        answer = str(input("> "))
        while answer not in ["1", "2"]:
            print_slow(format_string_center.format(string="Enter 1 or 2."))
            answer = input("> ")
        if answer == "1":
            battle_boss()
        if answer == "2":
            string = """
"Ha!  I  knew  you were itchin' for a  fight!
"Why  does a  bandit  do anythin', huh?  What
would you know?"
.  .  .
Razorfang  frowns  and  rolls  his shoulders,
causing a distinct cracking noise.  "Fayhaven
was poor, sure, we we're worse off.  I'm sure
you noticed the mess we're in. To be fair, he
didn't think a single person could defeat all
of us... but if you think you'll get past me,
you're wrong. I got more  at stake here  than
the pittance we got from Fayhaven." 

There  was a  pause as Razorfang  watches you 
for any hostile action. You ask what he means
by  that, and he  chuckles lowly. "I  suppose 
it won't  matter since  you'll be  dead.  You
weren't supposed to come. It  was supposed to
some  soldiers. Take away  from the battle up
north.  After I  deal with  you, the  king is 
going to have to send some men,  then Midgard
will try to take down your king."

"Let's  get to this,  kid.  Prepare to  die!"
"""
            print_slow(format_string_center.format(string=string))
            two_battle()


def battle_boss():
    string = """
"Ha!  I  knew  you were itchin' for a  fight!
Come at me!"
    """
    print_slow(format_string_center.format(string=string))
    two_battle()
    if not razor_fang.alive:
        player_information.total_points += 90
        string = """ 
You feel your heart beating faster as you 
finish  Razorfang  off.  You'll  need  to
report everything  to the king - how many
people were saved, how many died, and all
information  you might  have  gathered on 
your journey. 

However, what you want  to do most of all
is get home. So, you pack up your  things
and you quickly  leave the  bandit  hold, 
successful in your mission. When  you get
back  home,  the  people of Fayhaven  had 
come to greet you and celebrate your  job
well done.
"""
        print_slow(format_string_center.format(string=string))
        top_border = "┍" + "-" * 50 + "┐"
        bottom_border = "┕" + "-" * 50 + "┙"
        format_string = '╎ {string:^48} ╎'
        points = "Your score: " + str(player_information.total_points)
        print(top_border)
        print_fast(format_string.format(string="Congratulations you finished the game!"))
        print_fast(format_string.format(string=points))
        print(bottom_border)
        from screens import game_over
        game_over.high_scores_display()
        game_over.characters_initialize()
        game_over.initialize_rooms()
        game_over.player_initialize()
        player_information.total_points = 0
        from screens.menus import title
        title()


def high_scores_display():
    # write score to file
    score_updated = str(player_information.total_points) + ", " + player.name + "\n"
    write_scores(score_updated)
    high_scores = read_scores()
    print_scores(high_scores)


def read_scores():
    scores_file = "save_data/high_scores.txt"
    # create empty file if it was deleted somehow
    if not os.path.isfile(scores_file):
        write_scores([])
        return []
    with open(scores_file, 'r') as file:
        scores = file.readlines()
    count = 0
    for line in scores:
        scores[count] = line[:-1]
        count += 1
    scores.sort(reverse=True)
    return scores[:5]


def write_scores(scores):
    scores_file = "save_data/high_scores.txt"
    with open(scores_file, 'a') as file:
        file.write(scores)


def print_scores(scores):
    score_split = []
    for i in range(0, len(scores)):
        score_split.append(scores[i].split(", "))
    for i in range(0, len(score_split)):
        score = score_split[i][0]
        score_name = score_split[i][1].strip()
        print("{}: {}, {} points".format(i + 1, score_name, score))
