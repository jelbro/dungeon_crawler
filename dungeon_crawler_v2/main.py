import random
#        Race, Class, Str, Def,  Con,  Int,  Dex,  Cha  
player = ['h', 'w', '10', '10', '10', '10', '10', '10']

def main_menu():
    return input(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |                                  |
             |      Welcome to the dungeon!     |
             |                                  |
             |           (n) new game           |
             |                                  |
             |           (c) continue           |
             |                                  |
             |           (h) highscores         |
             |                                  |
             |           (e) exit               |
             |                                  |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'
            """)

def race_select_menu(): 
    return input(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |                                  |
             |      Please select your race     |
             |                                  |
             |           (h) human              |
             |                                  |
             |           (o) orc                |
             |                                  |
             |           (e) elf                |
             |                                  |
             |           (d) dwarf              |
             |                                  |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'
            """)

def class_select_menu(): 
    return input(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |                                  |
             |      Please select your class    |
             |                                  |
             |           (w) warrior            |
             |                                  |
             |           (m) mage               |
             |                                  |
             |           (r) ranger             |
             |                                  |
             |           (b) bard               |
             |                                  |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'
            """)

def player_stats_screen(n1, n2, n3, n4, n5, n6):
    print(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |      Stat points to allocate     |
             |                                  |""")
    print(f"             |             {n1:02d} {n2:02d} {n3:02d}             |")
    print(f"             |             {n4:02d} {n5:02d} {n6:02d}             |", end = "")
    return input(r"""
             |                                  |
             |     (s) Str (d) Def (c) Cons     |
             |                                  |
             |     (i) Int (x) Dex (h) Cha      |
             |                                  |
             | Stats are allocated from left to |
             |   right. Please select the stat  |
             |        you wish to allocate.     |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'
            """)

def display_player_stats(player):
    print(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |                                  |
             |          Your stats are:         |
             |                                  |""", end ="")
    print(f"""
             |        Str:{player[2]:02d}      Def:{player[3]:02d}        |
             |                                  |
             |        Cons:{player[4]:02d}     Int:{player[5]:02d}        |
             |                                  |
             |        Dex:{player[6]:02d}      Cha:{player[7]:02d}        |
             |                                  |
             |                                  |""", end="")
    return input(r"""
             |     Press enter to continue...   |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'
            """)

def dungeon_entrance():
    return input(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |                                  |
             |    You walk up to the enterance  |
             |  of the dungeon, what do you do? |
             |                                  |
             |      (k) kick down the door      |
             |                                  |
             |      (l) listen at the door      |
             |                                  |
             |              (r) run             |
             |                                  |
             |    (i) inventory   (s) stats     |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'
            """)


def new_game():
    player[0] = race_select()
    player[1] = class_select()
    get_player_stats()
    display_player_stats(player) 
    dungeon(player)
    #  death_screen()
    #  save_score()
    #  show_highscores()
    return 1

def saved_game():
    pass

def highscores():
    pass

def race_select():
    while True:
       race_choice = race_select_menu()
       if race_choice.lower() == 'h' or race_choice.lower() == 'o' or race_choice.lower() == 'e' or race_choice.lower() == 'd':
           return race_choice
       else:
           continue

def class_select():
    while True:
       class_choice = class_select_menu()
       if class_choice.lower() == 'w' or class_choice.lower() == 'm' or class_choice.lower() == 'r' or class_choice.lower() == 'b':
           return class_choice 
       else:
           continue

def get_player_stats():
    str_chosen = False
    def_chosen = False
    cons_chosen = False
    int_chosen = False
    char_chosen = False
    dex_chosen = False
    num1, num2, num3, num4, num5, num6 = roll_for_attribute(), roll_for_attribute(), roll_for_attribute(), roll_for_attribute(), roll_for_attribute(), roll_for_attribute()
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6)
        if stat_choice == 's' and str_chosen != True:
            player[2] = num1 
            str_chosen = False
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[3] = num1 
            def_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[4] = num1 
            cons_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[5] = num1 
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[6] = num1 
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[7] = num1 
            char_chosen = True
            break
        else:
            continue
    num1 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6)
        if stat_choice == 's' and str_chosen != True:
            player[2] = num2
            str_chosen = False
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[3] = num2
            def_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[4] = num2
            cons_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[5] = num2
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[6] = num2
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[7] = num2
            char_chosen = True
            break
        else:
            continue
    num2 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6)
        if stat_choice == 's' and str_chosen != True:
            player[2] = num3
            str_chosen = False
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[3] = num3 
            def_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[4] = num3
            cons_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[5] = num3
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[6] = num3
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[7] = num3
            char_chosen = True
            break
        else:
            continue
    num3 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6)
        if stat_choice == 's' and str_chosen != True:
            player[2] = num4
            str_chosen = False
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[3] = num4
            def_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[4] = num4
            cons_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[5] = num4
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[6] = num4
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[7] = num4
            char_chosen = True
            break
        else:
            continue
    num4 = 00
    while True:  
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6)
        if stat_choice == 's' and str_chosen != True:
            player[2] = num5
            str_chosen = False
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[3] = num5
            def_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[4] = num5
            cons_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[5] = num5
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[6] = num5
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[7] = num5
            char_chosen = True
            break
        else:
            continue
    num5 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6)
        if stat_choice == 's' and str_chosen != True:
            player[2] = num6
            str_chosen = False
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[3] = num6
            def_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[4] = num6
            cons_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[5] = num6
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[6] = num6
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[7] = num6
            char_chosen = True
            break
        else:
            continue
    num6 = 00
    print(player) 

def dungeon(player):
    player_choice = dungeon_entrance()
    while True:
        if player_choice.lower() == 'k':
            kick_door()
            break
        elif player_choice.lower() == 'l':
            listen_door()
            break
        elif player_choice.lower() == 'r':
            run()
            break
        elif player_choice.lower() == 'i':
            show_invent()
            break
        elif player_choice.lower() == 's':
            display_player_stats(player)
            dungeon(player)
        else:
            continue

def dice(n):
    return random.randint(1, n)

def roll_for_attribute():
    dice1, dice2, dice3, dice4 = dice(6), dice(6), dice(6), dice(6)
    final_number = 0
    final_dice_set = []
    dice_set = [dice1, dice2, dice3, dice4]
    sorted_dice_set = sorted(dice_set)
    for j in range(1, 4):
        final_dice_set.append(sorted_dice_set[j])
    for i in range(len(final_dice_set)):
            final_number += final_dice_set[i]
    return final_number

while True:
    menu_choice = main_menu()
    if menu_choice.lower() == 'n':
        new_game()
    elif menu_choice.lower() == 'c':
        saved_game()
    elif menu_choice.lower() == 'h':
        highscores()
    elif menu_choice.lower() =='e':
        break
    else:
        continue
