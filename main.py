import random

play_game = True


def dice(low_dice, high_dice):  # dice function you give it the low side and high side of the dice e.g. 1, 6 for a d6
    dice_roll = random.randint(low_dice, high_dice)
    print(f"You rolled a {dice_roll}.")
    return dice_roll


def dm_dice(dm_low_side, dm_high_side):  # same as before but doesn't display the roll
    dm_roll = random.randint(dm_low_side, dm_high_side)
    return dm_roll


def race_picker():  # function to ask player to select their race
    while True:  # race selection while loop will repeat until valid race is picked
        race_picked = input('What is your Race? (Dwarf, Elf, Ogre) ')
        if race_picked in ['Dwarf', 'dwarf', 'DWARF', 'd', 'D']:
            race_picked = 'a Dwarf'
            return race_picked
        elif race_picked in ['Elf', 'elf', 'ELF', 'e', 'E']:
            race_picked = 'an Elf'
            return race_picked
        elif race_picked in ['Ogre', 'ogre', 'OGRE', 'o', 'O']:
            race_picked = 'an Ogre'
            return race_picked
        else:
            print('Invalid Race Picked')


def class_picker():  # functions to ask player to select their class
    while True:  # race selection while loop will repeat until valid race is picked
        class_picked = input('What is your Class? (Warrior, Wizard, Bard) ')
        if class_picked in ['Warrior', 'warrior', 'WARRIOR', 'w', 'W']:
            class_picked = 'Warrior'
            return class_picked
        elif class_picked in ['Wizard', 'wizard', 'WIZARD', 'wi', 'WI', 'Wi']:
            class_picked = 'Wizard'
            return class_picked
        elif class_picked in ['Bard', 'bard', 'BARD', 'b', 'B']:
            class_picked = 'Bard'
            return class_picked
        else:
            print('Invalid Class Picked')


def strong_mods(race_str, class_str):  # takes player's race and class and return's the hidden strength mod not sure
    # if this is working properly and combining both class and race mods
    str_mod = 0
    if race_str in 'a Dwarf':
        str_mod += 2
        return str_mod
    elif race_str in 'an Elf':
        str_mod -= 2
        return str_mod
    else:
        str_mod += 5
    if class_str in 'Warrior':
        str_mod += 2
        return str_mod
    elif class_str in 'Wizard':
        str_mod -= 3
        return str_mod
    else:
        str_mod -= 1
        return str_mod


def cha_mods(race_cha, class_cha):  # takes player's race and class and return's the hidden charisma mod not sure
    # if this is working properly and combining both class and race mods
    char_mod = 0
    if race_cha in 'a Dwarf':
        char_mod += 2
        return char_mod
    elif race_cha in 'an Elf':
        char_mod -= 2
        return char_mod
    else:
        char_mod += 5
    if class_cha in 'Warrior':
        char_mod -= 2
        return char_mod
    elif class_cha in 'Wizard':
        char_mod += 2
        return char_mod
    else:
        char_mod += 5
        return char_mod


def intel_mods(race_intel, class_intel):  # takes player's race and class and return's the hidden strength mod not sure
    # if this is working properly and combining both class and race mods
    int_mod = 0
    if race_intel in 'a Dwarf':
        int_mod += 2
        return int_mod
    elif race_intel in 'an Elf':
        int_mod += 2
        return int_mod
    else:
        int_mod += 5
    if class_intel in 'Warrior':
        int_mod -= 3
        return int_mod
    elif class_intel in 'Wizard':
        int_mod += 5
        return int_mod
    else:
        int_mod += 1
        return int_mod


def hp_calc(race_hp, class_hp):  # calculates the player's hitpoints using race and class mods
    input("Roll for Hit Points.")
    hp_roll = dice(10, 20)
    if race_hp in 'a Dwarf':
        hp_roll += 2
    elif race_hp in 'an Elf':
        hp_roll -= 3
    elif race_hp in 'an Ogre':
        hp_roll += 5
    if class_hp in 'Warrior':
        hp_roll += 2
    elif class_hp in 'Wizard':
        hp_roll -= 3
    elif class_hp in 'Bard':
        hp_roll -= 1
    # print(f"You have {hp_roll} total hit points.")
    return hp_roll


def def_calc(race_def, class_def):  # calculates the player's defence using race and class mods
    input("Roll for Defence.")
    def_roll = dice(7, 9)
    if race_def in 'a Dwarf':
        def_roll += 2
    elif race_def in 'an Elf':
        def_roll -= 2
    elif race_def in 'an Ogre':
        def_roll += 3
    if class_def in 'Warrior':
        def_roll += 3
    elif class_def in 'Wizard':
        def_roll -= 3
    elif class_def in 'Bard':
        def_roll -= 1
    # print(f"You have {def_roll} Defence.")
    return def_roll


def strong_calc():  # calculates players strength
    input("Roll for Strength.")
    str_calc_roll = dice(1, 10)
    # print(f"You have {str_calc_roll} Strength.")
    return str_calc_roll


def cha_calc():  # calculates players charisma
    input("Roll for Charisma.")
    cha_calc_roll = dice(1, 10)
    # print(f"You have {cha_calc_roll} Charisma.")
    return cha_calc_roll


def intel_calc():  # calculates players intelligence
    input("Roll for Intelligence.")
    intel_calc_roll = dice(1, 10)
    # print(f"You have {intel_calc_roll} Intelligence.")
    return intel_calc_roll


def monster_generator():  # rolls a die to see which monster is generated
    monster_name_roll = dm_dice(1, 2)
    if monster_name_roll == 1:
        gen_monster_name = "Goblin"
        return gen_monster_name
    if monster_name_roll == 2:
        gen_monster_name = "Skeleton"
        return gen_monster_name


def monster_def_calc(monster_def_name):  # calculates monsters defence based on monsters name
    if monster_def_name in "Goblin":
        calc_monster_def = 7
        return calc_monster_def
    elif monster_def_name in "Skeleton":
        calc_monster_def = 10
        return calc_monster_def


def monster_attk_calc(monster_attk_name):  # calculates monsters attack based on monsters name
    if monster_attk_name in "Goblin":
        calc_monster_attk = 8
        return calc_monster_attk
    elif monster_attk_name in "Skeleton":
        calc_monster_attk = 9
        return calc_monster_attk


def monster_health_calc(monster_health_name):  # calculates monsters health based on monsters name
    if monster_health_name in "Goblin":
        calc_monster_health = 13
        return calc_monster_health
    elif monster_health_name in "Skeleton":
        calc_monster_health = 11
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
    hit_roll = dice(1, 20)  # rolls a 20 sided dice and stores input in roll
    if attk_dungeon_class in "Warrior":  # warriors attack loop
        if (hit_roll + attk_strong_mod) > attk_strong:  # calculates if you hit
            print("You swing your sword at the creature, it hits!")
            input("Roll for damage")
            dmg_roll = dice(1, 10)  # rolls a new dice which calculates your damage
            block_roll = dm_dice(1, 20)  # rolls a hidden die which calculates if the monster blocked the attack
            if block_roll >= attk_monster_defence:  # calculate if monster blocked
                print("The Creature blocks the attack!")
                return attk_monster_health
            else:  # monster didn't block you damage it
                print(f"Your sword slices the creature for {dmg_roll} damage!")
                attk_monster_health -= dmg_roll  # remove damage from monsters health
                return attk_monster_health
        else:
            print("You swing your sword high into the air, and completely miss the beast...")
            return attk_monster_health
    elif dungeon_class in "Bard":  # this and wizard below are same as above just different flavour text
        if (hit_roll + attk_cha_mod) > attk_cha:
            print("You strum your lute and send a spell right at the creature!")
            input("Roll for damage")
            dmg_roll = dice(1, 10)
            block_roll = dm_dice(1, 20)
            if block_roll >= attk_monster_defence:
                print("The Creature blocks the attack!")
                return attk_monster_health
            else:
                print(f"Your spell hits the creature for {dmg_roll} damage!")
                attk_monster_health -= dmg_roll
                return attk_monster_health
        else:
            print("You strum your lute, maybe you should have tuned first...")
            return attk_monster_health
    elif dungeon_class in "Wizard":
        if (hit_roll + attk_intel_mod) > attk_intel:
            print("You cast a fireball directly at the creature!")
            input("Roll for damage")
            dmg_roll = dice(1, 10)
            block_roll = dm_dice(1, 20)
            if block_roll >= attk_monster_defence:
                print("The Creature blocks the attack!")
                return attk_monster_health
            else:
                print(f"Your fireball scorches the creature for {dmg_roll} damage!")
                attk_monster_health -= dmg_roll
                return attk_monster_health
        else:
            print("You wave your wand in the air, nothing happens...")
            return attk_monster_health


def monster_attack(player_hp_total, def_player_defence, def_monster_attk):  # main monster attack loop
    monster_hit_roll = dm_dice(1, 20)  # rolls a hidden to player d20 to see if monster hit
    if monster_hit_roll > def_monster_attk:  # works out if monster hit you
        print("The Monster attacks you!")
        monster_dmg_roll = dm_dice(1, 10)  # dm rolls for monster damage
        input("Roll to Block")  # player rolls to block
        player_block_roll = dice(1, 20)
        if player_block_roll <= def_player_defence:  # bit janky
            print("You block the monster's attack!")
            return player_hp_total
        else:
            print(f"The creature hits you for {monster_dmg_roll} damage!")  # creature hits you and deals damage
            player_hp_total -= monster_dmg_roll  # takes damage from player total health
            print(f"Your current hp is {player_hp_total}")
            return player_hp_total
    else:
        print("The creature attacks you...and misses.")
        return player_hp_total


def check_alive(check_hp_total):  # function to check  if the player is alive
    if check_hp_total <= 0:
        check_player_alive = False
        print("You have died")
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
        if skill_up in "h":
            return skill_up
        elif skill_up in "d":
            return skill_up
        elif skill_up in "s":
            return skill_up
        elif skill_up in "c":
            return skill_up
        elif skill_up in "i":
            return skill_up
        else:
            print("Invalid Stat Picked")
            skill_up = False
            return skill_up


while play_game:
    action = 'nothing'
    player_escaped = True
    player_alive = True
    monster_alive = True
    print('Welcome To The Dungeon!')  # intro screen
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
    input("Time to enter the dungeon.")  # intro screen 2
    while player_alive and player_escaped:  # main loop for game
        door = dm_dice(1, 1)  # rolls a die to determine door opened currently only testing first door
        print("You kick open the door!")  # flavour text
        if door == 1:  # checks if this door was rolled
            monster_name = monster_generator()  # generates a monster name
            monster_defence = monster_def_calc(monster_name)  # generates monster defence given the name
            monster_health = monster_health_calc(monster_name)  # generates monster health given the name
            monster_attk = monster_attk_calc(monster_name)  # generates monster attack given the name
            monster_alive = True
            print(f"You encounter a {monster_name}!")
            while monster_alive and player_escaped and player_alive:  # main combat loop
                action = input("What do you do? (Attack, Run)")  # asks player for action
                if action in ("Attack", "attack", "ATTACK", "a", "A"):  # if player chooses to attack
                    monster_health = player_attack(dungeon_class, strong_mod, cha_mod, strong, cha, intel, intel_mod,
                                                   monster_defence, monster_health)
                    monster_alive = check_monster_alive(monster_health)
                    if not monster_alive:
                        hp_total = mem_hp_total
                        level_up = which_level()
                        if level_up in "h":
                            hp_total += 1
                        elif level_up in "d":
                            player_defence += 1
                        elif level_up in "s":
                            strong += 1
                        elif level_up in "c":
                            cha += 1
                        elif level_up in "i":
                            intel += 1
                        display_stats(hp_total, strong, cha, intel, player_defence)
                        continue
                    hp_total = monster_attack(hp_total, player_defence, monster_defence)
                    player_alive = check_alive(hp_total)
                elif action in ("Run", "run", "RUN", "r", "R"):  # if player runs they will have to roll
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
        elif door == 2:  # not done yet
            action = input("You find a chest, What do you do? (Open, Check)")
            if action in ("Open", "open", "OPEN", "o", "O"):
                print("You open the chest.")
            elif action in ("Check", "check", "CHECK", "c", "C"):
                print("You check the chest for traps.")
        elif door == 3:  # not done yet
            action = input("You encounter a strange man who asks you a riddle?")
            if action in ("Attack", "attack", "ATTACK", "a", "A"):
                print("You Attack.")
            elif action in ("Run", "run", "RUN", "r", "R"):
                print("You Attack.")
    play_again_input = input("Play Again? (y/n)")  # asks if player wants to play again once dead
    if play_again_input in ('y', 'Y'):
        play_game = True
    elif play_again_input in "n":
        play_game = False
    else:
        play_game = False
