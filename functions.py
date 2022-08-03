import random


def race_picker():
    race_picked = False  # boolean to track if the player has chosen a valid race
    while not race_picked:  # race selection while loop will repeat until valid race is picked
        race = input('What is your Race? (Dwarf, Elf, Ogre) ')
        if race in ['Dwarf', 'dwarf', 'DWARF', 'd', 'D']:
            race = 'a Dwarf'
            race_picked = True
            return race
        elif race in ['Elf', 'elf', 'ELF', 'e', 'E']:
            race = 'an Elf'
            race_picked = True
            return race
        elif race in ['Ogre', 'ogre', 'OGRE', 'o', 'O']:
            race = 'an Ogre'
            race_picked = True
            return race
        else:
            print('Invalid Race Picked')


def class_picker():
    class_picked = False  # boolean to track if the player has chose a valid class
    dungeon_class = 'Peasant'
    while not class_picked:  # race selection while loop will repeat until valid race is picked
        dungeon_class = input('What is your Class? (Warrior, Wizard, Bard) ')
        if dungeon_class in ['Warrior', 'warrior', 'WARRIOR', 'w', 'W']:
            dungeon_class = 'Warrior'
            class_picked = True
            return dungeon_class
        elif dungeon_class in ['Wizard', 'wizard', 'WIZARD', 'w', 'W']:
            dungeon_class = 'Wizard'
            class_picked = True
            return dungeon_class
        elif dungeon_class in ['Bard', 'bard', 'BARD', 'b', 'B']:
            dungeon_class = 'Bard'
            class_picked = True
            return dungeon_class
        else:
            print('Invalid Class Picked')


def strong_mods(race, dungeon_class):
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


def cha_mods(race, dungeon_class):
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


def intel_mods(race, dungeon_class):
    intel_mod = 0
    if race in 'a Dwarf':
        intel_mod += 2
        return intel_mod
    elif race in 'an Elf':
        intel_mod += 2
        return intel_mod
    else:
        intel_mod += 5
    if race in 'Warrior':
        intel_mod -= 3
        return intel_mod
    elif race in 'Wizard':
        intel_mod += 5
        return intel_mod
    else:
        intel_mod += 1
        return intel_mod


def dice(low_side, high_side):
    roll = random.randint(low_side, high_side)
    print(f"You rolled {roll}")
    return roll


def dm_dice(low_side, high_side):
    roll = random.randint(low_side, high_side)
    return roll


def hp_calc(race, dungeon_class):
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


def def_calc(race, dungeon_class):
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


def strong_calc(race, dungeon_class):
    input("Roll for Strength.")
    roll = dice(1, 10)
    print(f"You have {roll} Strength.")
    return roll


def cha_calc(race, dungeon_class):
    input("Roll for Charisma.")
    roll = dice(1, 10)
    print(f"You have {roll} Charisma.")
    return roll


def intel_calc(race, dungeon_class):
    input("Roll for Intelligence.")
    roll = dice(1, 10)
    print(f"You have {roll} Intelligence.")
    return roll


def monster_generator():
    roll = dm_dice(1, 2)
    if roll == 1:
        monster_name = "Goblin"
        return monster_name
    if roll == 2:
        monster_name = "Skeleton"
        return monster_name


def monster_def_calc(monster_name):
    if monster_name in "Goblin":
        monster_def = 7
        return monster_def
    elif monster_name in "Skeleton":
        monster_def = 10
        return monster_def


def monster_attk_calc(monster_name):
    if monster_name in "Goblin":
        monster_attk = 8
        return monster_attk
    elif monster_name in "Skeleton":
        monster_attk = 9
        return monster_attk


def monster_health_calc(monster_name):
    if monster_name in "Goblin":
        monster_health = 13
        return monster_health
    elif monster_name in "Skeleton":
        monster_health = 11
        return monster_health


def display_stats(hp_total, strong, cha, intel):
    print("Your Stats are:")
    print(f"{hp_total} Hit points")
    print(f"{strong} Strength")
    print(f"{cha} Charisma")
    print(f"{intel} Intelligence")


def player_attack(dungeon_class, strong_mod, cha_mod, strong, cha, intel, intel_mod, monster_defence, monster_health):
    input("Roll to hit")
    roll = dice(1, 20)
    if dungeon_class in "Warrior":
        if (roll + strong_mod) > strong:
            print("You swing your sword at the creature, it hits!")
            input("Roll for damage")
            roll10 = dice(1, 10)
            block_roll = dm_dice(1, 20)
            if block_roll >= monster_defence:
                print("The Creature blocks the attack!")
            else:
                print(f"You rolled a {roll10}.")
                print(f"Your sword slices the creature for {roll10} damage!")
                monster_health -= roll10
            if monster_health <= 0:
                print("You killed the monster!")
        else:
            print("You swing your sword high into the air, and completely miss the beast...")
    elif dungeon_class in "Bard":
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


def monster_attack(hp_total, player_defence, monster_attk):
    roll = dm_dice(1, 20)
    if roll > monster_attk:
        print("The Monster attacks you!")
        roll10 = dm_dice(1, 10)
        input("Roll to Block")
        block_roll = dice(1, 20)
        if block_roll <= player_defence:
            print("You block the monster's attack!")
        else:
            print(f"The creature hits you for {roll10} damage!")
            hp_total = hp_total - roll10
            print(f"Your current hp is {hp_total}")
        if hp_total <= 0:
            print("The monster's attack kills you.")
    else:
        print("The creature attacks you...and misses.")


def check_alive(hp_total):
    if hp_total <= 0:
        player_alive = False
        print("You have died")
        return player_alive
    else:
        player_alive = True
        return player_alive
