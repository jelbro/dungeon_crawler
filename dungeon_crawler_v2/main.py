import random
#        Race, Class, Str, Def,  Con,  Int,  Dex,  Cha  
player = ['h', 'w', '10', '10', '10', '10', '10', '10']
#           Str,   Def,   Con,  Int,  Dex,  Cha
stat_mods = []
# [[[item name][skill type][combat die][equipable]]]

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

def player_stats_screen(stat_numbers):
    print(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |      Stat points to allocate     |
             |                                  |""")
    print(f"             |             {stat_numbers[0]:02d} {stat_numbers[1]:02d} {stat_numbers[2]:02d}             |")
    print(f"             |             {stat_numbers[3]:02d} {stat_numbers[4]:02d} {stat_numbers[5]:02d}             |", end = "")
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

def display_player_stats(player, stat_mods):
    print(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |                                  |
             |          Your stats are:         |
             |                                  |""", end ="")
    print(f"""
             |   Str:{player[2]:02d}({stat_mods[0]:02d})      Def:{player[3]:02d}({stat_mods[1]:02d})     |
             |                                  |
             |   Con:{player[4]:02d}({stat_mods[2]:02d})      Int:{player[5]:02d}({stat_mods[3]:02d})     |
             |                                  |
             |   Dex:{player[6]:02d}({stat_mods[4]:02d})      Cha:{player[7]:02d}({stat_mods[5]:02d})     |
             |                                  |
             |                                  |""", end="")
    return input(r"""
             |     Press enter to continue...   |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'
            """)

def display_player_inventory(player_inventory):
    print(r"""          
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |                                  |
             |    Item Name:  Stat:  Hit die:   |
             |                                  |""", end ="")
    print("""
             |""", end="")
    name_length = len(player_inventory[0])
    stat_length = len(player_inventory[1])
    hit_length = len(str(player_inventory[2]))
    front_spacing = ((36 - (name_length + stat_length + hit_length + 6)) // 2)
    for i in range(front_spacing):
        print(" ", end="")
    print(f"{player_inventory[0]}   {player_inventory[1]}   {player_inventory[2]}")
    for i in range(front_spacing):
        if i == (front_spacing - 1):
            print("|")
        else:
            print(" ", end="")
    
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
    player_inventory = []
    player[0] = race_select()
    player[1] = class_select()
    get_player_stats()
    get_modifiers(stat_mods, player)
    display_player_stats(player, stat_mods)
    player_inventory = give_player_items(player_inventory, player)
    display_player_inventory(player_inventory)
    dungeon(player, stat_mods)
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
    str_chosen, def_chosen, cons_chosen, int_chosen, char_chosen, dex_chosen = False, False, False, False, False, False
    num1, num2, num3, num4, num5, num6 = roll_for_attribute(), roll_for_attribute(), roll_for_attribute(), roll_for_attribute(), roll_for_attribute(), roll_for_attribute()
    stat_numbers = [num1, num2, num3, num4, num5, num6]
    for i in range(6): 
        while True:
            stat_choice = player_stats_screen(stat_numbers)
            if stat_choice == 's' and str_chosen != True:
                player[2] = stat_numbers[i] 
                str_chosen = True 
                stat_numbers[i]  = 00
                break
            elif stat_choice == 'd' and def_chosen != True:
                player[3] = stat_numbers[i]
                def_chosen = True
                stat_numbers[i]  = 00
                break
            elif stat_choice == 'c' and cons_chosen != True:
                player[4] = stat_numbers[i]
                cons_chosen = True
                stat_numbers[i]  = 00
                break
            elif stat_choice == 'i' and int_chosen != True:
                player[5] = stat_numbers[i]
                int_chosen = True
                stat_numbers[i]  = 00
                break
            elif stat_choice == 'x' and dex_chosen != True:
                player[6] = stat_numbers[i]
                dex_chosen = True
                stat_numbers[i]  = 00
                break
            elif stat_choice == 'h' and char_chosen != True:
                player[7] = stat_numbers[i] 
                char_chosen = True
                stat_numbers[i]  = 00
                break
            else:
                continue

def get_modifiers(stat_mods, player): 
    for i in range(2, 8):
        stat_mods.append((player[i] - 10) // 2)
        i = i + 1

def give_player_items(player_inventory, player):
    mage_items = ["m",["Magic Staff","int", 6, True]]
    warrior_items = ["w",["Long Sword","str", 6, True]]
    ranger_items = ["r",["Short Bow","dex", 6, True]]
    bard_items = ["b",["Lute","cha", 6, True]]
    starting_items = [mage_items, warrior_items, ranger_items, bard_items]
    for i in range(len(starting_items)):
        if starting_items[i][0] == player[1]:
            player_inventory = starting_items[i][1]
    return player_inventory
    
def dungeon(player, stat_mods):
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
            display_player_stats(player, stat_mods)
            dungeon(player, stat_mods)
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
