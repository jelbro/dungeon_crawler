import functions  # all the projects functions think I've done something wrong by putting them all in a separate file
# but not sure what
dice20 = 0  # D20 Dice OLD DICE new one in functions
dice10 = 0  # D10 Dice OLD DICE
dice3 = 0  # D3 Dice OLD DICE
action = 'nothing'  # initialising the players action
player_escaped = False  # initialising that the player has not escaped the combat
player_alive = True  # initialising that the player is alive

print('Welcome To The Dungeon!')  # intro screen
race = functions.race_picker()  # asks the player their race and stores result in race
dungeon_class = functions.class_picker()  # asks the player their class and stores result in class
print(f"Ah I see now, you're {race} {dungeon_class}.")  # prints players chosen race and class
strong_mod = functions.strong_mods(race, dungeon_class)  # calculates the player's hidden modifier to strength given
# chosen race and class
cha_mod = functions.cha_mods(race, dungeon_class)  # calculates the player's hidden modifier to charisma given chosen
# race and class
intel_mod = functions.intel_mods(race, dungeon_class)  # calculates the player's hidden modifier to intelligence
# given chosen race and class
hp_total = functions.hp_calc(race, dungeon_class)  # calculates the player's total hp given race and class mods
player_defence = functions.def_calc(race, dungeon_class)  # calculates the player's defence given race and class mods
strong = functions.strong_calc(race, dungeon_class)  # calculates players strength
cha = functions.cha_calc(race, dungeon_class)  # calculates players charisma
intel = functions.intel_calc(race, dungeon_class)  # calculates players intelligence
functions.display_stats(hp_total, strong, cha, intel, player_defence)  # displays final stats of the player
input("Time to enter the dungeon.")  # intro screen 2
while player_alive:  # main loop for game should check if the player is alive can't get this to work properly
    player_alive = functions.check_alive(hp_total)  # should calculate weather the player is alive cant get this to work
    door = functions.dm_dice(1, 1)  # rolls a die to determine door opened currently only testing first door
    print("You kick open the door!")  # flavour text
    if door == 1:  # checks if this door was rolled
        monster_name = functions.monster_generator()  # generates a monster name
        monster_defence = functions.monster_def_calc(monster_name)  # generates monster defence given the name
        monster_health = functions.monster_health_calc(monster_name)  # generates monster health given the name
        monster_attk = functions.monster_attk_calc(monster_name)  # generates monster attack given the name
        while monster_health > 0 and not player_escaped:  # main combat loop checking if monster is dead or the
            # player has escaped not sure weather this should also be checking if the player is dead don't think this
            # is working
            player_alive = functions.check_alive(hp_total)  # checking if the player is alive
            action = input(f"You encounter a {monster_name}, What do you do? (Attack, Run)")  # asks player for action
            if action in ("Attack", "attack", "ATTACK", "a", "A"):  # if player chooses to attack
                functions.player_attack(dungeon_class, strong_mod, cha_mod, strong, cha, intel, intel_mod, monster_defence, monster_health)  # runs the player attack loop
                functions.monster_attack(hp_total, player_defence, monster_attk)  # runs the monster attack loop
                player_alive = functions.check_alive(hp_total)  # checking if the player is alive don't know the best
                # place to do this but assume I don't need to do 3 times
            elif action in ("Run", "run", "RUN", "r", "R"):  # if player runs they will have to roll but not done yet
                player_escaped = True
                print("You Run.")
    elif dice3 == 2:  # not done yet
        action = input("You find a chest, What do you do? (Open, Check)")
        if action in ("Open", "open", "OPEN", "o", "O"):
            print("You open the chest.")
        elif action in ("Check", "check", "CHECK", "c", "C"):
            print("You check the chest for traps.")
    elif dice3 == 3:  # not done yet
        action = input("You encounter a strange man who asks you a riddle?")
        if action in ("Attack", "attack", "ATTACK", "a", "A"):
            print("You Attack.")
        elif action in ("Run", "run", "RUN", "r", "R"):
            print("You Attack.")
print("You have died")  # in theory should exit main while loop if player is dead then get to here and end
