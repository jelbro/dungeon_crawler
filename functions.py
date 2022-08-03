import random


def race_picker():  # function to ask player to select their race
    while True:  # race selection while loop will repeat until valid race is picked
        race = input('What is your Race? (Dwarf, Elf, Ogre) ')
        if race in ['Dwarf', 'dwarf', 'DWARF', 'd', 'D']:
            race = 'a Dwarf'
            return race
        elif race in ['Elf', 'elf', 'ELF', 'e', 'E']:
            race = 'an Elf'
            return race
        elif race in ['Ogre', 'ogre', 'OGRE', 'o', 'O']:
            race = 'an Ogre'
            return race
        else:
            print('Invalid Race Picked')


def class_picker():  # functions to ask player to select their class
    while True:  # race selection while loop will repeat until valid race is picked
        dungeon_class = input('What is your Class? (Warrior, Wizard, Bard) ')
        if dungeon_class in ['Warrior', 'warrior', 'WARRIOR', 'w', 'W']:
            dungeon_class = 'Warrior'
            return dungeon_class
        elif dungeon_class in ['Wizard', 'wizard', 'WIZARD', 'w', 'W']:
            dungeon_class = 'Wizard'
            return dungeon_class
        elif dungeon_class in ['Bard', 'bard', 'BARD', 'b', 'B']:
            dungeon_class = 'Bard'
            return dungeon_class
        else:
            print('Invalid Class Picked')


def strong_mods(race, dungeon_class):  # takes player's race and class and return's the hidden strength mod not sure
    # if this is working properly and combining both class and race mods
    strong_mod = 0
    if race in 'a Dwarf':
        strong_mod += 2
        return strong_mod
    elif race in 'an Elf':
        strong_mod -= 2
        return strong_mod
    else:
        strong_mod += 5
    if dungeon_class in 'Warrior':
        strong_mod += 2
        return strong_mod
    elif dungeon_class in 'Wizard':
        strong_mod -= 3
        return strong_mod
    else:
        strong_mod -= 1
        return strong_mod


def cha_mods(race, dungeon_class):  # takes player's race and class and return's the hidden charisma mod not sure
    # if this is working properly and combining both class and race mods
    cha_mod = 0
    if race in 'a Dwarf':
        cha_mod += 2
        return cha_mod
    elif race in 'an Elf':
        cha_mod -= 2
        return cha_mod
    else:
        cha_mod += 5
    if dungeon_class in 'Warrior':
        cha_mod -= 2
        return cha_mod
    elif dungeon_class in 'Wizard':
        cha_mod += 2
        return cha_mod
    else:
        cha_mod += 5
        return cha_mod


def intel_mods(race, dungeon_class):  # takes player's race and class and return's the hidden strength mod not sure
    # if this is working properly and combining both class and race mods
    intel_mod = 0
    if race in 'a Dwarf':
        intel_mod += 2
        return intel_mod
    elif race in 'an Elf':
        intel_mod += 2
        return intel_mod
    else:
        intel_mod += 5
    if dungeon_class in 'Warrior':
        intel_mod -= 3
        return intel_mod
    elif dungeon_class in 'Wizard':
        intel_mod += 5
        return intel_mod
    else:
        intel_mod += 1
        return intel_mod


def dice(low_side, high_side):  # dice function you give it the low side and high side of the dice e.g. 1, 6 for a d6
    roll = random.randint(low_side, high_side)
    print(f"You rolled {roll}")
    return roll


def dm_dice(low_side, high_side):  # same as before but doesn't display the roll
    roll = random.randint(low_side, high_side)
    return roll


def hp_calc(race, dungeon_class):  # calculates the player's hitpoints using race and class mods
    input("Roll for Hit Points.")
    roll = dice(10, 20)
    if race in 'a Dwarf':
        roll += 2
    elif race in 'an Elf':
        roll -= 3
    elif race in 'an Ogre':
        roll += 5
    if dungeon_class in 'Warrior':
        roll += 2
    elif dungeon_class in 'Wizard':
        roll -= 3
    elif dungeon_class in 'Bard':
        roll -= 1
    print(f"You have {roll} total hit points.")
    return roll


def def_calc(race, dungeon_class):  # calculates the player's defence using race and class mods
    input("Roll for Defence.")
    roll = dice(7, 9)
    if race in 'a Dwarf':
        roll += 2
    elif race in 'an Elf':
        roll -= 2
    elif race in 'an Ogre':
        roll += 3
    if dungeon_class in 'Warrior':
        roll += 3
    elif dungeon_class in 'Wizard':
        roll -= 3
    elif dungeon_class in 'Bard':
        roll -= 1
    print(f"You have {roll} Defence.")
    return roll


def strong_calc():  # calculates players strength
    input("Roll for Strength.")
    roll = dice(1, 10)
    print(f"You have {roll} Strength.")
    return roll


def cha_calc():  # calculates players charisma
    input("Roll for Charisma.")
    roll = dice(1, 10)
    print(f"You have {roll} Charisma.")
    return roll


def intel_calc():  # calculates players intelligence
    input("Roll for Intelligence.")
    roll = dice(1, 10)
    print(f"You have {roll} Intelligence.")
    return roll


def monster_generator():  # rolls a die to see which monster is generated
    roll = dm_dice(1, 2)
    if roll == 1:
        monster_name = "Goblin"
        return monster_name
    if roll == 2:
        monster_name = "Skeleton"
        return monster_name


def monster_def_calc(monster_name):  # calculates monsters defence based on monsters name
    if monster_name in "Goblin":
        monster_def = 7
        return monster_def
    elif monster_name in "Skeleton":
        monster_def = 10
        return monster_def


def monster_attk_calc(monster_name):  # calculates monsters attack based on monsters name
    if monster_name in "Goblin":
        monster_attk = 8
        return monster_attk
    elif monster_name in "Skeleton":
        monster_attk = 9
        return monster_attk


def monster_health_calc(monster_name):  # calculates monsters health based on monsters name
    if monster_name in "Goblin":
        monster_health = 13
        return monster_health
    elif monster_name in "Skeleton":
        monster_health = 11
        return monster_health


def display_stats(hp_total, strong, cha, intel, player_defence):  # prints players stats
    print("Your Stats are:")
    print(f"{hp_total} Hit points")
    print(f"{player_defence} Hit points")
    print(f"{strong} Strength")
    print(f"{cha} Charisma")
    print(f"{intel} Intelligence")


def player_attack(dungeon_class, strong_mod, cha_mod, strong, cha, intel, intel_mod, monster_defence, monster_health):  # main player attack loop
    input("Roll to hit")
    roll = dice(1, 20)  # rolls a 20 sided dice and stores input in roll
    if dungeon_class in "Warrior":  # warriors attack loop
        if (roll + strong_mod) > strong:  # this is a bit janky not properly worked out the combat mechanics calculates if you hit
            print("You swing your sword at the creature, it hits!")
            input("Roll for damage")
            roll10 = dice(1, 10)  # rolls a new dice which calculates your damage
            block_roll = dm_dice(1, 20)  # rolls a dice hidden to player which calculates if the monster blocked the attack
            if block_roll >= monster_defence:  # again a bit janky combat mechanics wise should calculate if monster blocked
                print("The Creature blocks the attack!")
            else:  # monster didn't block you damage it
                print(f"You rolled a {roll10}.")
                print(f"Your sword slices the creature for {roll10} damage!")
                monster_health -= roll10  # should remove damage from monster's health don't think this is working tho
            if monster_health <= 0:  # this sometimes works but i don't think it breaks out of the while properly if it does
                print("You killed the monster!")
        else:
            print("You swing your sword high into the air, and completely miss the beast...")
    elif dungeon_class in "Bard":  # this and wizard below are same as above just different flavour text probs a better way to do this?
        if (roll + cha_mod) > cha:
            print("You strum your lute and send a spell right at the creature!")
            input("Roll for damage")
            roll10 = dice(1, 10)
            block_roll = dm_dice(1, 20)
            if block_roll >= monster_defence:
                print("The Creature blocks the attack!")
            else:
                print(f"You rolled a {roll10}.")
                print(f"Your spell hits the creature for {roll10} damage!")
                monster_health -= roll10
            if monster_health <= 0:
                print("You killed the monster!")
        else:
            print("You strum your lute, maybe you should have tuned first...")
    elif dungeon_class in "Wizard":
        if (roll + intel_mod) > intel:
            print("You cast a fireball directly at the creature!")
            input("Roll for damage")
            roll10 = dice(1, 10)
            block_roll = dm_dice(1, 20)
            if block_roll >= monster_defence:
                print("The Creature blocks the attack!")
            else:
                print(f"You rolled a {roll10}.")
                print(f"Your fireball scorches the creature for {roll10} damage!")
                monster_health -= roll10
            if monster_health <= 0:
                print("You killed the monster!")
        else:
            print("You wave your wand in the air, nothing happens...")


def monster_attack(hp_total, player_defence, monster_attk):  # main monster attack loop
    roll = dm_dice(1, 20)  # rolls a hidden to player d20 to see if monster hit
    if roll > monster_attk:  # janky but works out if monster hit you
        print("The Monster attacks you!")
        roll10 = dm_dice(1, 10)  # dm rolls for monster damage
        input("Roll to Block")  # player rolls to block
        block_roll = dice(1, 20)
        if block_roll <= player_defence:  # bit janky
            print("You block the monster's attack!")
        else:
            print(f"The creature hits you for {roll10} damage!")  # creature hits you and deals damage
            hp_total = hp_total - roll10  # this was the main issue i needed help with if you play the game and watch the current hp printed below it does some weird shit number just seems to go up and down randomly
            print(f"Your current hp is {hp_total}")
        if hp_total <= 0:  # dont think this works either especially with the check_alive function or breaking out of the while when dead
            print("The monster's attack kills you.")
    else:
        print("The creature attacks you...and misses.")


def check_alive(hp_total):  # function to check  if the player is alive doesn't seem to work
    if hp_total <= 0:
        player_alive = False
        print("You have died")
        return player_alive
    else:
        player_alive = True
        return player_alive
