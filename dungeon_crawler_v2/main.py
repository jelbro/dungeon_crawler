#  Race, Class, Cons, Att, Str, Def, Int, Dex, Cha  
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

def new_game():
    race_select()
    class_select()
    dungeon()
    death_screen()
    save_score()
    show_highscores()
    return 1

def saved_game():
    pass

def highscores():
    pass

def race_select():
    

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
