import random
from colorama import init, Fore, Style

play_game = True


def dice(low_dice, high_dice):  # dice function you give it the low side and high side of the dice e.g. 1, 6 for a d6
    dice_roll = random.randint(low_dice, high_dice)
    print("You rolled", Fore.GREEN, dice_roll, Style.RESET_ALL)
    return dice_roll


def dm_dice(dm_low_side, dm_high_side):  # same as before but doesn't display the roll
    dm_roll = random.randint(dm_low_side, dm_high_side)
    return dm_roll


def race_picker():  # function to ask player to select their race
    while True:  # race selection while loop will repeat until valid race is picked
        race_picked = input('What is your Race? ([D]warf, [E]lf, [O]gre) ')
        if race_picked.lower() == 'd':
            race_picked = 'a Dwarf'
            return race_picked
        elif race_picked.lower() == 'e':
            race_picked = 'an Elf'
            return race_picked
        elif race_picked.lower() == 'o':
            race_picked = 'an Ogre'
            return race_picked
        else:
            print('Invalid race picked, please use a single character input')


def class_picker():  # functions to ask player to select their class
    while True:  # race selection while loop will repeat until valid race is picked
        class_picked = input('What is your Class? ([W]arrior, [M]age, [B]ard) ')
        if class_picked.lower() == 'w':
            class_picked = 'Warrior'
            return class_picked
        elif class_picked.lower() == 'm':
            class_picked = 'Mage'
            return class_picked
        elif class_picked.lower() == 'b':
            class_picked = 'Bard'
            return class_picked
        else:
            print('Invalid Class Picked')


def strong_mods(race_str, class_str):  # takes player's race and class and return's the hidden strength mod not sure
    # if this is working properly and combining both class and race mods
    str_mod = 0
    if race_str == 'a Dwarf':
        str_mod += 2
    elif race_str == 'an Elf':
        str_mod -= 2
    elif race_str == 'an Ogre':
        str_mod += 5
    else:
        str_mod += 0
    if class_str == 'Warrior':
        str_mod += 2
    elif class_str == 'Mage':
        str_mod -= 3
    elif class_str == 'Bard':
        str_mod -= 1
    else:
        str_mod += 0
    return str_mod


def cha_mods(race_cha, class_cha):  # takes player's race and class and return's the hidden charisma mod not sure
    # if this is working properly and combining both class and race mods
    char_mod = 0
    if race_cha == 'a Dwarf':
        char_mod += 2
    elif race_cha == 'an Elf':
        char_mod -= 2
    elif race_cha == 'an Ogre':
        char_mod -= 5
    else:
        char_mod += 0
    if class_cha == 'Warrior':
        char_mod -= 2
    elif class_cha == 'Mage':
        char_mod += 2
    elif class_cha == 'Bard':
        char_mod += 5
    else:
        char_mod += 0
    return char_mod


def intel_mods(race_intel, class_intel):  # takes player's race and class and return's the hidden strength mod not sure
    # if this is working properly and combining both class and race mods
    int_mod = 0
    if race_intel == 'a Dwarf':
        int_mod += 2
    elif race_intel == 'an Elf':
        int_mod += 2
    elif race_intel == 'an Ogre':
        int_mod += 5
    if class_intel == 'Warrior':
        int_mod -= 3
    elif class_intel == 'Mage':
        int_mod += 5
    elif class_intel == 'Bard':
        int_mod += 1
    return int_mod


def hp_calc(race_hp, class_hp):  # calculates the player's hitpoints using race and class mods
    input("Roll for Hit Points.")
    hp_roll = dice(10, 20)
    if race_hp == 'a Dwarf':
        hp_roll += 2
    elif race_hp == 'an Elf':
        hp_roll -= 3
    elif race_hp == 'an Ogre':
        hp_roll += 5
    if class_hp == 'Warrior':
        hp_roll += 2
    elif class_hp == 'Mage':
        hp_roll -= 3
    elif class_hp == 'Bard':
        hp_roll -= 1
    return hp_roll


def def_calc(race_def, class_def):  # calculates the player's defence using race and class mods
    input("Roll for Defence.")
    def_roll = dice(7, 9)
    if race_def == 'a Dwarf':
        def_roll += 2
    elif race_def == 'an Elf':
        def_roll -= 2
    elif race_def == 'an Ogre':
        def_roll += 3
    if class_def == 'Warrior':
        def_roll += 3
    elif class_def == 'Mage':
        def_roll -= 3
    elif class_def == 'Bard':
        def_roll -= 1
    return def_roll


def strong_calc():  # calculates players strength
    input("Roll for Strength.")
    str_calc_roll = dice(1, 10)
    return str_calc_roll


def cha_calc():  # calculates players charisma
    input("Roll for Charisma.")
    cha_calc_roll = dice(1, 10)
    return cha_calc_roll


def intel_calc():  # calculates players intelligence
    input("Roll for Intelligence.")
    intel_calc_roll = dice(1, 10)
    return intel_calc_roll


def monster_generator():  # rolls a die to see which monster is generated
    monster_name_roll = dm_dice(1, 5)
    if monster_name_roll == 1 or monster_name_roll == 2:
        gen_monster_name = "Goblin"
        return gen_monster_name
    if monster_name_roll == 3 or monster_name_roll == 4:
        gen_monster_name = "Skeleton"
        return gen_monster_name
    if monster_name_roll == 5:
        gen_monster_name = "Beholder"
        return gen_monster_name


def monster_def_calc(monster_def_name):  # calculates monsters defence based on monsters name
    if monster_def_name == "Goblin":
        calc_monster_def = 12
        return calc_monster_def
    elif monster_def_name == "Skeleton":
        calc_monster_def = 15
        return calc_monster_def
    elif monster_def_name == "Beholder":
        calc_monster_def = 20
        return calc_monster_def


def monster_attk_calc(monster_attk_name):  # calculates monsters attack based on monsters name
    if monster_attk_name == "Goblin":
        calc_monster_attk = 8
        return calc_monster_attk
    elif monster_attk_name == "Skeleton":
        calc_monster_attk = 9
        return calc_monster_attk
    elif monster_attk_name == "Beholder":
        calc_monster_attk = 16
        return calc_monster_attk


def monster_health_calc(monster_health_name):  # calculates monsters health based on monsters name
    if monster_health_name == "Goblin":
        calc_monster_health = 13
        return calc_monster_health
    elif monster_health_name == "Skeleton":
        calc_monster_health = 11
        return calc_monster_health
    elif monster_health_name == "Beholder":
        calc_monster_health = 40
        return calc_monster_health


def display_stats(display_hp_total, display_strong, display_cha, display_intel,
                  display_player_defence):  # prints players stats
    print("Your Stats are:")
    print(f"{display_hp_total} Hit points")
    print(f"{display_player_defence} Defence")
    print(f"{display_strong} Strength")
    print(f"{display_cha} Charisma")
    print(f"{display_intel} Intelligence")


def player_attack(attk_dungeon_class, attk_strong_mod, attk_cha_mod, attk_strong, attk_cha, attk_intel, attk_intel_mod,
                  attk_monster_defence, attk_monster_health):  # main player attack loop
    input("Roll to hit")
    hit_roll = dice(1, 20)
    if attk_dungeon_class == "Warrior":
        if hit_roll == 20:
            print("It's a critical hit!")
            input("Roll for damage")
            dmg_roll = (dice(1, 10)) * 2
            print("Your sword slices the creature for", Fore.GREEN, dmg_roll, Style.RESET_ALL, "damage!")
            attk_monster_health -= dmg_roll
            return attk_monster_health
        elif hit_roll == 1:
            print("You swing your sword...and completely miss the beast!")
            attk_monster_health += 0
            return attk_monster_health
        elif (hit_roll + attk_strong_mod + attk_strong) >= attk_monster_defence \
                and (hit_roll + attk_strong_mod + attk_strong) != 20 \
                and (hit_roll + attk_strong_mod + attk_strong) != 1:
            print("You swing your sword at the creature, it hits!")
            input("Roll for damage")
            dmg_roll = dice(1, 10)
            print("Your sword slices the creature for", Fore.GREEN, dmg_roll, Style.RESET_ALL, "damage!")
            attk_monster_health -= dmg_roll
            return attk_monster_health
        else:
            print("The Creature blocks the attack!")
            return attk_monster_health
    elif dungeon_class == "Bard":
        if hit_roll == 20:
            print("It's a critical hit!")
            input("Roll for damage")
            dmg_roll = (dice(1, 10)) * 2
            print("Your spell echo's around the room and hits the beast for", Fore.GREEN, dmg_roll, Style.RESET_ALL,"damage!")
            attk_monster_health -= dmg_roll
            return attk_monster_health
        elif hit_roll == 1:
            print("You strum your lute, maybe you should have tuned first...")
            attk_monster_health += 0
            return attk_monster_health
        elif (hit_roll + attk_cha_mod + attk_cha) > monster_defence \
                and (hit_roll + attk_cha_mod + cha_mod) != 20 \
                and (hit_roll + attk_cha_mod + cha_mod) != 1:
            print("You strum your lute and send a spell right at the creature!")
            input("Roll for damage")
            dmg_roll = dice(1, 10)
            print("Your spell hits the creature for", Fore.GREEN, dmg_roll, Style.RESET_ALL, "damage!")
            attk_monster_health -= dmg_roll
            return attk_monster_health
        else:
            print("The Creature blocks the attack!")
            return attk_monster_health
    elif dungeon_class == "Mage":
        if hit_roll == 20:
            print("It's a critical hit!")
            input("Roll for damage")
            dmg_roll = (dice(1, 10)) * 2
            print("You cast a huge fireball engulfing the creature for", Fore.GREEN, dmg_roll, Style.RESET_ALL, "damage!")
            attk_monster_health -= dmg_roll
            return attk_monster_health
        elif hit_roll == 1:
            print("You wave your wand in the air, nothing happens...")
            attk_monster_health += 0
            return attk_monster_health
        elif (hit_roll + attk_intel_mod + attk_intel) > monster_defence \
                and (hit_roll + attk_intel_mod + intel_mod) != 20 \
                and (hit_roll + attk_intel_mod + intel_mod) != 1:
            print("You cast a fireball directly at the creature!")
            input("Roll for damage")
            dmg_roll = dice(1, 10)
            print("Your fireball scorches the creature for", Fore.GREEN, dmg_roll, Style.RESET_ALL, "damage!")
            attk_monster_health -= dmg_roll
            return attk_monster_health
        else:
            print("The Creature blocks the attack!")
            return attk_monster_health


def monster_attack(player_hp_total, def_player_defence, def_monster_attk, monster_att_value):  # main monster attack loop
    monster_hit_roll = dm_dice(1, 20)  # rolls a hidden to player d20 to see if monster hit
    if monster_hit_roll == 20:
        monster_dmg_roll = (dm_dice(1, 10)) * 2
        print("The monster hits you with a brutal attack dealing", Fore.RED, monster_dmg_roll, Style.RESET_ALL, "damage!")
        player_hp_total -= monster_dmg_roll
        print(f"Your current hp is {player_hp_total}")
        return player_hp_total
    elif monster_hit_roll == 1:
        print("The creature attacks you...and misses")
        return player_hp_total
    elif monster_hit_roll + monster_att_value > def_player_defence \
            and monster_hit_roll + monster_att_value != 20 and monster_hit_roll + monster_att_value != 1:
        print("The monster attacks you!")
        monster_dmg_roll = dm_dice(1, 10)
        print("The monster does", Fore.RED, monster_dmg_roll, Style.RESET_ALL, "damage.")
        player_hp_total -= monster_dmg_roll
        print("Your current hp is", Fore.GREEN, player_hp_total, Style.RESET_ALL)
        return player_hp_total
    else:
        print("You block the monster's attack!")
        return player_hp_total


def check_alive(check_hp_total):  # function to check  if the player is alive
    if check_hp_total <= 0:
        check_player_alive = False
        print("±±±±±±±±±±±±You have died±±±±±±±±±±±±±")
        return check_player_alive
    else:
        check_player_alive = True
        return check_player_alive


def check_monster_alive(mons_hp_total):  # function to check  if the player is alive
    if mons_hp_total <= 0:
        check_mons_alive = False
        print("The Beast is dead!")
        return check_mons_alive
    else:
        check_mons_alive = True
        return check_mons_alive


def which_level():  # gets input for chosen level up skill
    while True:
        skill_up = input("You levelled up, which stat would you like to increase?"
                         "(h = Hit points, d = Defence, s = Strength, c = Charisma, i = Intelligence)")
        if skill_up.lower() == "h":
            return skill_up
        elif skill_up.lower() == "d":
            return skill_up
        elif skill_up.lower() == "s":
            return skill_up
        elif skill_up.lower() == "c":
            return skill_up
        elif skill_up.lower() == "i":
            return skill_up
        else:
            print("Invalid Stat Picked")


def loot_generator(loot_class):
    loot_roll = dm_dice(1, 3)
    if loot_roll == 1:
        if loot_class == "Warrior":
            return 1
        elif loot_class == "Bard":
            return 2
        elif loot_class == "Mage":
            return 3
    elif loot_roll == 2:
        return 4
    elif loot_roll == 3:
        return 5


while play_game:
    action = 'nothing'
    player_escaped = True
    player_alive = True
    monster_alive = True
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('        Welcome To The Dungeon!')  # intro screen
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    race = race_picker()  # asks the player their race and stores result in race
    dungeon_class = class_picker()  # asks the player their class and stores result in class
    print(f"Ah I see now, you're {race} {dungeon_class}.")  # prints players chosen race and class
    strong_mod = strong_mods(race, dungeon_class)  # calculates the player's hidden modifier to strength given
    # chosen race and class
    cha_mod = cha_mods(race, dungeon_class)  # calculates the player's hidden modifier to charisma given chosen
    # race and class
    intel_mod = intel_mods(race, dungeon_class)  # calculates the player's hidden modifier to intelligence
    # given chosen race and class
    hp_total = hp_calc(race, dungeon_class)  # calculates the player's total hp given race and class mods
    mem_hp_total = hp_total
    player_defence = def_calc(race, dungeon_class)  # calculates the player's defence given race and class mods
    strong = strong_calc()  # calculates players strength
    cha = cha_calc()  # calculates players charisma
    intel = intel_calc()  # calculates players intelligence
    display_stats(hp_total, strong, cha, intel, player_defence)  # displays final stats of the player
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    input("      Time to enter the dungeon.")  # intro screen 2
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while player_alive and player_escaped:  # main loop for game
        door = dm_dice(1, 3)  # rolls a die to determine door opened currently only testing first door
        print("You kick open the door!")  # flavour text
        if door == 1 or door == 2:  # checks if this door was rolled
            monster_name = monster_generator()  # generates a monster name
            monster_defence = monster_def_calc(monster_name)  # generates monster defence given the name
            monster_health = monster_health_calc(monster_name)  # generates monster health given the name
            monster_attk = monster_attk_calc(monster_name)  # generates monster attack given the name
            monster_alive = True
            print(f"You encounter a {monster_name}!")
            while monster_alive and player_escaped and player_alive:  # main combat loop
                action = input("What do you do? ([A]ttack, [R]un)")  # asks player for action
                if action.lower() == "a":  # if player chooses to attack
                    monster_health = player_attack(dungeon_class, strong_mod, cha_mod, strong, cha, intel, intel_mod,
                                                   monster_defence, monster_health)
                    monster_alive = check_monster_alive(monster_health)
                    if not monster_alive:
                        hp_total = mem_hp_total
                        if monster_name == "Beholder":
                            level_up = which_level()
                            if level_up.lower() == "h":
                                hp_total += 1
                                mem_hp_total += 1
                            elif level_up.lower() == "d":
                                player_defence += 1
                            elif level_up.lower() == "s":
                                strong += 1
                            elif level_up.lower() == "c":
                                cha += 1
                            elif level_up.lower() == "i":
                                intel += 1
                            display_stats(hp_total, strong, cha, intel, player_defence)
                        level_up = which_level()
                        if level_up.lower() == "h":
                            hp_total += 1
                            mem_hp_total += 1
                        elif level_up.lower() == "d":
                            player_defence += 1
                        elif level_up.lower() == "s":
                            strong += 1
                        elif level_up.lower() == "c":
                            cha += 1
                        elif level_up.lower() == "i":
                            intel += 1
                        display_stats(hp_total, strong, cha, intel, player_defence)
                        continue
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    hp_total = monster_attack(hp_total, player_defence, monster_defence, monster_attk)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    player_alive = check_alive(hp_total)
                elif action.lower() == "r":  # if player runs they will have to roll
                    input("Roll to escape!")
                    escape_roll = dice(1, 20)
                    if escape_roll > 15:
                        player_escaped = True
                        print("You successfully escape the fight!")
                        break
                    else:
                        print("The creature grabs you as you try to escape!")
                        print("You have died.")
                        player_alive = False
        elif door == 3:
            action = input("You find a chest! [O]pen it?")
            if action.lower() == "o":
                chest_roll = dm_dice(1, 20)
                if 1 < chest_roll < 5:
                    chest_dmg_roll = dm_dice(1, 10)
                    print(f"The Chest is trapped and deals {chest_dmg_roll} damage to you!")
                    hp_total = chest_dmg_roll - hp_total
                    player_alive = check_alive(hp_total)
                    print(f"Your current hp is {hp_total}")
                else:
                    print("You open the chest.")
                    loot = loot_generator(dungeon_class)
                    if loot == 1:
                        print("You find a legendary sword, it increases your strength by 1")
                        strong += 1
                    elif loot == 2:
                        print("You find a mystical lute, it increases your charisma by 1")
                        cha += 1
                    elif loot == 3:
                        print("You find a magical wand, it increases your intelligence by 1")
                        intel += 1
                    elif loot == 4:
                        print("You find a potion of experience")
                        level_up = which_level()
                        if level_up.lower() == "h":
                            hp_total += 1
                        elif level_up.lower() == "d":
                            player_defence += 1
                        elif level_up.lower() == "s":
                            strong += 1
                        elif level_up.lower() == "c":
                            cha += 1
                        elif level_up.lower() == "i":
                            intel += 1
                        display_stats(hp_total, strong, cha, intel, player_defence)
                    elif loot == 5:
                        if dungeon_class == "Warrior":
                            print("You find some new armour, it increases your defence by 1")
                            player_defence += 1
                        elif dungeon_class == "Bard":
                            print("You find a new tunic, it increases your defence by 1")
                            player_defence += 1
                        elif dungeon_class == "Mage":
                            print("You find a new robe, it increases your defence by 1")
                            player_defence += 1
            elif action.lower() == "c":  # not done yet
                print("You check the chest for traps.")
        elif door == 3:  # not done yet
            action = input("You encounter a strange man who asks you a riddle?")
            if action in ("Attack", "attack", "ATTACK", "a", "A"):
                print("You Attack.")
            elif action in ("Run", "run", "RUN", "r", "R"):
                print("You Attack.")
    play_again_input = input("Play Again? (y/n)")  # asks if player wants to play again once dead
    if play_again_input.lower() == 'y':
        play_game = True
    elif play_again_input.lower() == "n":
        play_game = False
    else:
        play_game = False
