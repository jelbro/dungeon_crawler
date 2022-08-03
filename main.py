import random
import functions
dice20 = 0  # D20 Dice
dice10 = 0  # D10 Dice
dice3 = 0  # D3 Dice
action = 'nothing'
monster_defence = 10
monster_health = 20
player_escaped = False
player_alive = True

print('Welcome To The Dungeon!')  # intro screen
race = functions.race_picker()
dungeon_class = functions.class_picker()
print(f"Ah I see now, you're {race} {dungeon_class}.")
strong_mod = functions.strong_mods(race, dungeon_class)
cha_mod = functions.cha_mods(race, dungeon_class)
intel_mod = functions.intel_mods(race, dungeon_class)
hp_total = functions.hp_calc(race, dungeon_class)
player_defence = functions.def_calc(race, dungeon_class)
strong = functions.strong_calc(race, dungeon_class)
cha = functions.cha_calc(race, dungeon_class)
intel = functions.intel_calc(race, dungeon_class)
functions.display_stats(hp_total, strong, cha, intel)
input("Time to enter the dungeon.")
while player_alive:
    player_alive = functions.check_alive(hp_total)
    door = functions.dm_dice(1, 1)
    print("You kick open the door!")
    if door == 1:
        monster_name = functions.monster_generator()
        monster_defence = functions.monster_def_calc(monster_name)
        monster_health = functions.monster_health_calc(monster_name)
        monster_attk = functions.monster_attk_calc(monster_name)
        while monster_health > 0 and not player_escaped:
            player_alive = functions.check_alive(hp_total)
            action = input(f"You encounter a {monster_name}, What do you do? (Attack, Run)")
            if action in ("Attack", "attack", "ATTACK", "a", "A"):
                functions.player_attack(dungeon_class, strong_mod, cha_mod, strong, cha, intel, intel_mod, monster_defence, monster_health)
                functions.monster_attack(hp_total, player_defence, monster_attk)
                player_alive = functions.check_alive(hp_total)
            elif action in ("Run", "run", "RUN", "r", "R"):
                player_escaped = True
                print("You Run.")
    elif dice3 == 2:
        action = input("You find a chest, What do you do? (Open, Check)")
        if action in ("Open", "open", "OPEN", "o", "O"):
            print("You open the chest.")
        elif action in ("Check", "check", "CHECK", "c", "C"):
            print("You check the chest for traps.")
    elif dice3 == 3:
        action = input("You encounter a strange man who asks you a riddle?")
        if action in ("Attack", "attack", "ATTACK", "a", "A"):
            print("You Attack.")
        elif action in ("Run", "run", "RUN", "r", "R"):
            print("You Attack.")
print("You have died")
