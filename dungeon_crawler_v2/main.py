import random
#  Race, Class, Att, Str, Def, Con, Int, Dex, Cha  
player = ['h', 'w', '10', '10', '10', '10', '10', '10', '10']

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

def player_stats_screen(n1, n2, n3, n4, n5, n6, n7, n8, n9):
    print(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |      Stat points to allocate     |
             |                                  |""")
    print(f"             |            {n1:02d} {n2:02d} {n3:02d} {n4:02d}           |")
    print(f"             |             {n5:02d} {n6:02d} {n7:02d}             |", end = "")
    return input(r"""
             |                                  |
             |     (a) att (s) str (d) def      |
             |                                  |
             | (c) con (i) int (x) dex (h) cha  |
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
             |        Att:{player[2]:02d}      Str:{player[3]:02d}        |
             |                                  |
             |        Def:{player[4]:02d}      Con:{player[5]:02d}        |
             |                                  |
             |        Int:{player[6]:02d}      Dex:{player[7]:02d}        |
             |                                  |
             |              Cha:{player[8]:02d}              |
             |                                  |""", end="")
    return input(r"""
             |     Press enter to continue...   |
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
    #  dungeon()
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
    att_chosen = False
    str_chosen = False
    def_chosen = False
    cons_chosen = False
    int_chosen = False
    char_chosen = False
    dex_chosen = False
    num1, num2, num3, num4, num5, num6, num7, num8, num9 = dice(20), dice(20), dice(20), dice(20), dice(20), dice(20), dice(20), dice(20), dice(20)
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6, num7, num8, num9)
        if stat_choice == 'a' and att_chosen != True:
            player[2] = num1 
            att_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[5] = num1 
            cons_chosen = False
            break
        elif stat_choice == 's' and str_chosen != True:
            player[3] = num1 
            str_chosen = True
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[4] = num1 
            def_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[6] = num1 
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[7] = num1 
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[8] = num1 
            char_chosen = True
            break
        else:
            continue
    num1 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6, num7, num8, num9)
        if stat_choice == 'a' and att_chosen != True:
            player[2] = num2 
            att_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[5] = num2
            cons_chosen = False
            break
        elif stat_choice == 's' and str_chosen != True:
            player[3] = num2
            str_chosen = True
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[4] = num2
            def_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[6] = num2
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[7] = num2
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[8] = num2
            char_chosen = True
            break
        else:
            continue
    num2 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6, num7, num8, num9)
        if stat_choice == 'a' and att_chosen != True:
            player[2] = num3 
            att_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[5] = num3
            cons_chosen = False
            break
        elif stat_choice == 's' and str_chosen != True:
            player[3] = num3 
            str_chosen = True
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[4] = num3
            def_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[6] = num3
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[7] = num3
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[8] = num3
            char_chosen = True
            break
        else:
            continue
    num3 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6, num7, num8, num9)
        if stat_choice == 'a' and att_chosen != True:
            player[2] = num4
            att_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[5] = num4
            cons_chosen = False
            break
        elif stat_choice == 's' and str_chosen != True:
            player[3] = num4
            str_chosen = True
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[4] = num4
            def_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[6] = num4
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[7] = num4
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[8] = num4
            char_chosen = True
            break
        else:
            continue
    num4 = 00
    while True:  
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6, num7, num8, num9)
        if stat_choice == 'a' and att_chosen != True:
            player[2] = num5
            att_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[5] = num5
            cons_chosen = False
            break
        elif stat_choice == 's' and str_chosen != True:
            player[3] = num5
            str_chosen = True
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[4] = num5
            def_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[6] = num5
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[7] = num5
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[8] = num5
            char_chosen = True
            break
        else:
            continue
    num5 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6, num7, num8, num9)
        if stat_choice == 'a' and att_chosen != True:
            player[2] = num6
            att_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[5] = num6
            cons_chosen = False
            break
        elif stat_choice == 's' and str_chosen != True:
            player[3] = num6
            str_chosen = True
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[4] = num6
            def_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[6] = num6
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[7] = num6
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[8] = num6
            char_chosen = True
            break
        else:
            continue
    num6 = 00
    while True:
        stat_choice = player_stats_screen(num1, num2, num3, num4, num5, num6, num7, num8, num9)
        if stat_choice == 'a' and att_chosen != True:
            player[2] = num7 
            att_chosen = True
            break
        elif stat_choice == 'c' and cons_chosen != True:
            player[5] = num7
            cons_chosen = False
            break
        elif stat_choice == 's' and str_chosen != True:
            player[3] = num7 
            str_chosen = True
            break
        elif stat_choice == 'd' and def_chosen != True:
            player[4] = num7
            def_chosen = True
            break
        elif stat_choice == 'i' and int_chosen != True:
            player[6] = num7
            int_chosen = True
            break
        elif stat_choice == 'x' and dex_chosen != True:
            player[7] = num7
            dex_chosen = True
            break
        elif stat_choice == 'h' and char_chosen != True:
            player[8] = num7
            char_chosen = True
            break
        else:
            continue
    num7 = 00
    print(player) 

def dice(n):
    return random.randint(1, n)

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
