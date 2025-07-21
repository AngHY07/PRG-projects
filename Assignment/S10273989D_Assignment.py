from random import randint

path = "C:\\Text Folders\\Assignment 35%\\"

player = {}
resources_map = []
fog = []
NAME = "NA"


MAP_WIDTH = 0
MAP_HEIGHT = 0
PORTAL_POSITION_X = 1
PORTAL_POSITION_Y = 1
TOWN_POSITION_X = 0
TOWN_POSITION_Y = 0 



TURNS_PER_DAY = 20
WIN_GP = 500
CURRENT_BAG_CAPACITY = 10
BACKPACK_SPACE_TAKEN = 0
PICKAXE_LEVEL = 1
PICKAXE_ORE = "copper"
STEP = 0

CURRENT_MAP_LAYOUT = [list("################################"),
                    list("#T?????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("#??????????????????????????????#"),
                    list("################################")]

minerals = ['copper', 'silver', 'gold']
mineral_names = {'C': 'copper', 'S': 'silver', 'G': 'gold'}



prices = {}
prices['copper'] = (1, 3)
prices['silver'] = (5, 8)
prices['gold'] = (10, 18)

# This function loads a map structure (a nested list) from a file
# It also updates MAP_WIDTH and MAP_HEIGHT
def load_map(filename, map_struct,player):
    map_file = open(path + filename, 'r')
    global MAP_WIDTH
    global MAP_HEIGHT
    global CURRENT_MAP_LAYOUT

    CURRENT_MAP_LAYOUT[player['y']].pop(player['x'])
    CURRENT_MAP_LAYOUT[player['y']].insert(player['x'],"M")

    file_info = map_file.readlines()
    for lines in file_info: 
        map_struct.append(list(lines.strip("\n")))

    for x in range(len(map_struct)):
        map_struct[x].insert(0,"#")
        
    for x in range(len(map_struct)):
        map_struct[x].append("#")

    map_struct.insert(0,list("################################"))
    map_struct.append(list("################################"))

    map_struct[player['y']].pop(player['x'])
    map_struct[player['y']].insert(player['x'],"M")

    
    MAP_WIDTH = len(map_struct[0])
    MAP_HEIGHT = len(map_struct)
    map_file.close()

def map_print_fog():
    global CURRENT_MAP_LAYOUT
    global MAP_WIDTH

    print("+",end="")
    for y in range(MAP_WIDTH-2):
        print("-",end="")
    print("+")

    for line in range(1,len(CURRENT_MAP_LAYOUT)-2):
        print("|",end="")
        for column in range(1,len(CURRENT_MAP_LAYOUT[line])-1):
            print(CURRENT_MAP_LAYOUT[line][column],end="")
        print("|")

    print("+",end="")
    for y in range(MAP_WIDTH-2):
        print("-",end="")
    print("+")


# This function clears the fog of war at the 3x3 square around the player




def initialize_game(game_map, fog, player):
    global CURRENT_MAP_LAYOUT

    player['x'] = 1
    player['y'] = 1
    player['copper'] = 0
    player['silver'] = 0
    player['gold'] = 0
    player['GP'] = 0
    player['day'] = 1
    player['steps'] = 0
    player['turns'] = TURNS_PER_DAY
    player['load'] = 0
    player['gp'] = 0
 

    

    load_map("level1.txt",resources_map,player)
    clear_fog(player,resources_map)


def draw_view (player,resources_map):
    global CURRENT_MAP_LAYOUT
    while  True:

        print("+---+")
        print("|",end="")
        print("{}".format(resources_map[(player['y'])-1][(player['x'])-1]),end="")
        print("{}".format(resources_map[(player['y'])-1][player['x']]),end="")
        print("{}".format(resources_map[(player['y'])-1][(player['x'])+1]),end="")
        print("|")

        print("|",end="")
        print("{}".format(resources_map[player['y']][(player['x'])-1]),end="")
        print("{}".format(resources_map[player['y']][player['x']]),end="")
        print("{}".format(resources_map[player['y']][(player['x'])+1]),end="")
        print("|")

        print("|",end="")
        print("{}".format(resources_map[(player['y'])+1][(player['x'])-1]),end="")
        print("{}".format(resources_map[(player['y'])+1][(player['x'])]),end="")
        print("{}".format(resources_map[(player['y'])+1][(player['x'])+1]),end="")
        print("|")
        print("+---+")
        return



# This function saves the game
def save_game(game_map, fog, player):
    # save map
    # save fog
    # save player
    return
        
# This function loads the game
def load_game(game_map, fog, player):
    # load map
    # load fog
    # load player
    return

def show_main_menu():
    print()
    print("--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
#    print("(H)igh scores")
    print("(Q)uit")
    print("------------------")

def show_town_menu(day):
    print()
    print("DAY {}".format(day))
    print("----- Sundrop Town -----")
    print("(B)uy stuff")
    print("See Player (I)nformation")
    print("See Mine (M)ap")
    print("(E)nter mine")
    print("Sa(V)e game")
    print("(Q)uit to main menu")
    print("------------------------")


def player_information(player): 

    print("----- Player Information -----")
    print("Name: {}".format(NAME))
    print("Portal position: ({},{})".format(PORTAL_POSITION_X-1,PORTAL_POSITION_Y-1))
    print("Pickaxe level: {} ({})".format(PICKAXE_LEVEL,PICKAXE_ORE))
    print("------------------------------")
    print("Load: {}/{}".format(player['load'],CURRENT_BAG_CAPACITY))
    print("------------------------------")
    print("GP: {}".format(player["gp"]))
    print("Steps taken: {}".format(STEP))
    print("------------------------------")

def player_in_game_information(player):
    print("----- Player Information -----")
    print("Name: {}".format(NAME))
    print("Current position: ({},{})".format(player['x']-1,player['y']-1))
    print("Pickaxe level: {} ({})".format(PICKAXE_LEVEL,PICKAXE_ORE))
    print("Gold: {}".format(player['gold']))
    print("Silver: {}".format(player['silver']))
    print("Copper: {}".format(player['copper']))
    print("------------------------------")
    print("Load: {} / {}".format(player['load'],CURRENT_BAG_CAPACITY))
    print("------------------------------")
    print("GP: {}".format(player['gp']))
    print("Steps taken: {}".format(player['steps']))
    print("------------------------------")
    

def buy_stuff(player):
    global CURRENT_BAG_CAPACITY
    global PICKAXE_LEVEL
    global PICKAXE_ORE

    if PICKAXE_LEVEL == 1:
        upgrade_ore = "silver"
        upgrade_price = 50
    elif PICKAXE_LEVEL == 2:
        upgrade_ore = "gold"
        upgrade_price = 150
    print("----------------------- Shop Menu -------------------------")
    print("(P) ickaxe upgrade to Level {} to mine {} ore for {} GP".format(PICKAXE_LEVEL,upgrade_ore,upgrade_price))
    print("(B) ackpack upgrade to carry {} items for {} GP".format((CURRENT_BAG_CAPACITY+2),(CURRENT_BAG_CAPACITY*2)))
    print("(L) eave shop")
    print("-----------------------------------------------------------")
    print("GP: {}".format(player['gp']))
    print("-----------------------------------------------------------")
    buy_1st_choice = input("Your choice? ")

    if buy_1st_choice.lower() == "b":
        while True: 
            
            print("----------------------- Shop Menu -------------------------")
            print("(B) ackpack upgrade to carry {} items for {} GP".format(CURRENT_BAG_CAPACITY+2,CURRENT_BAG_CAPACITY*2))
            print("(L) eave shop") 
            print("----------------------------------------------------------")
            print("GP: {}".format(player['gp']))
            print("----------------------------------------------------------")
            buy_2nd_choice = input("Your choice? ")
            if buy_2nd_choice.lower() == "l":
                return None
            elif buy_2nd_choice.lower() == "b":
                if player['gp'] < CURRENT_BAG_CAPACITY*2:
                    print("You do not have enough GP! Come back again later.")
                else:
                    print("Congratulations! You can now carry {} items!".format(CURRENT_BAG_CAPACITY+2))
                    player['gp'] -= (CURRENT_BAG_CAPACITY*2)
                    CURRENT_BAG_CAPACITY += 2

    
    elif buy_1st_choice.lower() == "p":
        while True : 
            print("----------------------- Shop Menu -------------------------")
            print("(P) ickaxe upgrade to Level {} to mine {} ore for {} GP".format(PICKAXE_LEVEL,upgrade_ore,upgrade_price))
            print("(L) eave shop") 
            print("----------------------------------------------------------")
            print("GP: {}".format(player['gp']))
            print("----------------------------------------------------------")
            buy_2nd_choice = input("Your choice? ")
            if buy_2nd_choice.lower() == "l":
                return None
            elif buy_2nd_choice.lower()=="p": 
                if player['gp']<upgrade_price:
                    print("You do not have enough GP! Come back again later.")
                else: 
                    print("Congratulations you have upgraded you pickaxe to level {}.".format(PICKAXE_LEVEL+1))
                    PICKAXE_LEVEL += 1
                    PICKAXE_ORE = upgrade_ore
                    player['gp'] -= upgrade_price

def ore_mining_w_s(player,value):
    copper_random = randint(1,5)
    silver_random = randint(1,3)
    gold_random = randint(1,2)
    global CURRENT_BAG_CAPACITY

    if resources_map[player['y']+value][player['x']] == "C":
            print("---------------------------------------------------")
            print("You mined {} piece(s) of copper.".format(copper_random))

            if (player['load']+copper_random) > CURRENT_BAG_CAPACITY:
                remaining_slots = CURRENT_BAG_CAPACITY-player['load']
                print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                player['load'] = CURRENT_BAG_CAPACITY
                player['copper'] += remaining_slots
            else :
                player['load'] += copper_random
                player['copper'] += copper_random
    elif resources_map[player['y']+value][player['x']] == "S":
            print("---------------------------------------------------")
            print("You mined {} piece(s) of silver.".format(copper_random))

            if (player['load']+silver_random) > CURRENT_BAG_CAPACITY:
                remaining_slots = CURRENT_BAG_CAPACITY-player['load']
                print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                player['load'] = CURRENT_BAG_CAPACITY
                player['silver'] += remaining_slots
            else :
                player['load'] += silver_random
                player['silver'] += silver_random
    elif resources_map[player['y']+value][player['x']] == "G":
            print("---------------------------------------------------")
            print("You mined {} piece(s) of gold.".format(copper_random))

            if (player['load']+gold_random) > CURRENT_BAG_CAPACITY:
                remaining_slots = CURRENT_BAG_CAPACITY-player['load']
                print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                player['load'] = CURRENT_BAG_CAPACITY
                player['gold'] += remaining_slots
            else :
                player['load'] += gold_random
                player['gold'] += gold_random

def ore_mining_a_d(player,value):
    copper_random = randint(1,5)
    silver_random = randint(1,3)
    gold_random = randint(1,2)
    global CURRENT_BAG_CAPACITY

    if resources_map[player['y']][player['x']+value] == "C":
            print("---------------------------------------------------")
            print("You mined {} piece(s) of copper.".format(copper_random))

            if (player['load']+copper_random) > CURRENT_BAG_CAPACITY:
                remaining_slots = CURRENT_BAG_CAPACITY-player['load']
                print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                player['load'] = CURRENT_BAG_CAPACITY
                player['copper'] += remaining_slots

            else :
                player['load'] += copper_random
                player['copper'] += copper_random
    elif resources_map[player['y']][player['x']+value] == "S":
            print("---------------------------------------------------")
            print("You mined {} piece(s) of silver.".format(copper_random))

            if (player['load']+silver_random) > CURRENT_BAG_CAPACITY:
                remaining_slots = CURRENT_BAG_CAPACITY-player['load']
                print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                player['load'] = CURRENT_BAG_CAPACITY
                player['silver'] += remaining_slots
            else :
                player['load'] += silver_random
                player['silver'] += silver_random
    elif resources_map[player['y']][player['x']+value] == "G":
            print("---------------------------------------------------")
            print("You mined {} piece(s) of gold.".format(copper_random))

            if (player['load']+gold_random) > CURRENT_BAG_CAPACITY:
                remaining_slots = CURRENT_BAG_CAPACITY-player['load']
                print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                player['load'] = CURRENT_BAG_CAPACITY
                player['gold'] += remaining_slots
            else :
                player['load'] += gold_random
                player['gold'] += gold_random

def upper_fog_left(player,resources_map):
    global CURRENT_MAP_LAYOUT
    CURRENT_MAP_LAYOUT[player['y']-1][player['x']-1] = resources_map[player['y']-1][player['x']-1]
    CURRENT_MAP_LAYOUT[player['y']-1][player['x']] = resources_map[player['y']-1][player['x']]
    
def upper_fog_right(player,resources_map):

    CURRENT_MAP_LAYOUT[player['y']-1][player['x']] = resources_map[player['y']-1][player['x']]
    CURRENT_MAP_LAYOUT[player['y']-1][player['x']+1] = resources_map[player['y']-1][player['x']+1]

def right_side_fog(player,resources_map):
    global CURRENT_MAP_LAYOUT
    CURRENT_MAP_LAYOUT[player['y']][player['x']+1]= resources_map[player['y']][player['x']+1]
    

def left_side_fog(player,resources_map): 
    global CURRENT_MAP_LAYOUT
    CURRENT_MAP_LAYOUT[player['y']][player['x']-1]= resources_map[player['y']][player['x']-1]
    

def below_fog_right(player,resources_map):
    global CURRENT_MAP_LAYOUT

    CURRENT_MAP_LAYOUT[player['y']+1][player['x']]= resources_map[player['y']+1][player['x']]
    CURRENT_MAP_LAYOUT[player['y']+1][player['x']+1] = resources_map[player['y']+1][player['x']+1]
    

def below_fog_left(player,resources_map):
    global CURRENT_MAP_LAYOUT

    CURRENT_MAP_LAYOUT[player['y']+1][player['x']-1]= resources_map[player['y']+1][player['x']-1]
    CURRENT_MAP_LAYOUT[player['y']+1][player['x']] = resources_map[player['y']+1][player['x']]
    


def clear_fog(player,resources_map):
    global CURRENT_MAP_LAYOUT

    if CURRENT_MAP_LAYOUT[player['y']-1][player['x']] == "#" and CURRENT_MAP_LAYOUT[player['y']][player['x']+1] =="#":
        left_side_fog(player,resources_map) 
        below_fog_left(player,resources_map)
    elif CURRENT_MAP_LAYOUT[player['y']-1][player['x']] == "#" and CURRENT_MAP_LAYOUT[player['y']][player['x']-1] =="#":
        right_side_fog(player,resources_map)
        below_fog_right(player,resources_map)
    elif CURRENT_MAP_LAYOUT[player['y']+1][player['x']] == "#" and CURRENT_MAP_LAYOUT[player['y']][player['x']+1] =="#":
        left_side_fog(player,resources_map)
        upper_fog_left(player,resources_map)
    elif CURRENT_MAP_LAYOUT[player['y']+1][player['x']] == "#" and CURRENT_MAP_LAYOUT[player['y']][player['x']-1] =="#":
        right_side_fog(player,resources_map)
        upper_fog_right(player,resources_map)
    elif CURRENT_MAP_LAYOUT[player['y']-1][player['x']] == "#":
        left_side_fog(player,resources_map)
        right_side_fog(player,resources_map)
        below_fog_left(player,resources_map)
        below_fog_right(player,resources_map)
    elif CURRENT_MAP_LAYOUT[player['y']+1][player['x']] == "#":
        left_side_fog(player,resources_map)
        right_side_fog(player,resources_map)
        upper_fog_left(player,resources_map)
        upper_fog_right(player,resources_map)
    elif CURRENT_MAP_LAYOUT[player['y']][player['x']+1] == "#":
        left_side_fog(player,resources_map)
        upper_fog_left(player,resources_map)
        upper_fog_right(player,resources_map)
        below_fog_left(player,resources_map)
        below_fog_right(player,resources_map)
    elif CURRENT_MAP_LAYOUT[player['y']][player['x']-1] == "#":
        right_side_fog(player,resources_map)
        upper_fog_left(player,resources_map)
        upper_fog_right(player,resources_map)
        below_fog_left(player,resources_map)
        below_fog_right(player,resources_map)
    else: 
        upper_fog_left(player,resources_map)
        upper_fog_right(player,resources_map)
        right_side_fog(player,resources_map)
        left_side_fog(player,resources_map)
        below_fog_left(player,resources_map)
        below_fog_right(player,resources_map)
   


def movement_input(player,resources_map,user_input): 
    global CURRENT_BAG_CAPACITY
    global TURNS_PER_DAY

    # W
    if user_input.lower() == "w":
        if player['y'] == 1:
            print("You are at the barrier, you can't move further up")
            return 
        clear_fog(player,resources_map)
        ore_mining_w_s (player,-1)
        # Remove original postion
        CURRENT_MAP_LAYOUT[player['y']].pop(player['x'])
        resources_map[player['y']].pop(player['x'])

        #Replace original position with blank space
        CURRENT_MAP_LAYOUT[player['y']].insert(player['x']," ")
        resources_map[player['y']].insert(player['x']," ")

        # Remove the position on top
        CURRENT_MAP_LAYOUT[player['y']-1].pop(player['x'])
        resources_map[player['y']-1].pop(player['x'])

        #Replace position on top with M
        CURRENT_MAP_LAYOUT[player['y']-1].insert(player['x'],"M")
        resources_map[player['y']-1].insert(player['x'],"M")

        
        player['y'] -= 1 
        player['turns'] -= 1
        player['steps'] += 1
        clear_fog(player,resources_map)
        return 
    
    #S 
    elif  user_input.lower() == "s":
        if CURRENT_MAP_LAYOUT[player['y']+1][player['x']] == "#":
            print("You are at the barrier, you can't move further down")
            return 
        clear_fog(player,resources_map)
        ore_mining_w_s(player,1)
        
        # Remove original postion
        CURRENT_MAP_LAYOUT[player['y']].pop(player['x'])
        resources_map[player['y']].pop(player['x'])

        #Replace original position with blank space
        if player["y"] == 1 and player["x"]  == 1:
            CURRENT_MAP_LAYOUT[player['y']].insert(player['x'],"T")
            resources_map[player['y']].insert(player['x'],"T")
        else: 
            CURRENT_MAP_LAYOUT[player['y']].insert(player['x']," ")
            resources_map[player['y']].insert(player['x']," ")

        # Remove the position on bottom
        CURRENT_MAP_LAYOUT[player['y']+1].pop(player['x'])
        resources_map[player['y']+1].pop(player['x'])

        #Replace position on bottom with M
        CURRENT_MAP_LAYOUT[player['y']+1].insert(player['x'],"M")
        resources_map[player['y']+1].insert(player['x'],"M")

  
        player['y'] += 1
        player['turns'] -= 1
        player['steps'] += 1
        clear_fog(player,resources_map)
        return 
    
    #A
    elif  user_input.lower() == "a":
        if CURRENT_MAP_LAYOUT[player['y']][player['x']-1] == "#":
            print("You are at the barrier, you can't move to your left")
            return 
        clear_fog(player,resources_map)
        ore_mining_a_d(player,-1)
        
        # Remove original postion
        CURRENT_MAP_LAYOUT[player['y']].pop(player['x'])
        resources_map[player['y']].pop(player['x'])

        #Replace original position with blank space
        CURRENT_MAP_LAYOUT[player['y']].insert(player['x']," ")
        resources_map[player['y']].insert(player['x']," ")

        # Remove the position on right
        CURRENT_MAP_LAYOUT[player['y']].pop(player['x']-1)
        resources_map[player['y']].pop(player['x']-1)

        #Replace position on right with M
        CURRENT_MAP_LAYOUT[player['y']].insert(player['x']-1,"M")
        resources_map[player['y']].insert(player['x']-1,"M")


        player['x'] -= 1
        player['turns'] -= 1
        player['steps'] += 1
        clear_fog(player,resources_map)

        return 

    #D
    elif  user_input.lower() == "d":
        if CURRENT_MAP_LAYOUT[player['y']][player['x']+1] == "#":
            print("You are at the barrier, you can't move to your right")
            return 
        clear_fog(player,resources_map)
        ore_mining_a_d(player,+1)
        
        # Remove original postion
        CURRENT_MAP_LAYOUT[player['y']].pop(player['x'])
        resources_map[player['y']].pop(player['x'])

        #Replace original position with blank space
        if player["y"] == 1 and player["x"]  == 1:
            CURRENT_MAP_LAYOUT[player['y']].insert(player['x'],"T")
            resources_map[player['y']].insert(player['x'],"T")
        else: 
            CURRENT_MAP_LAYOUT[player['y']].insert(player['x']," ")
            resources_map[player['y']].insert(player['x']," ")

        # Remove the position on right
        CURRENT_MAP_LAYOUT[player['y']].pop(player['x']+1)
        resources_map[player['y']].pop(player['x']+1)

        #Replace position on right with M
        CURRENT_MAP_LAYOUT[player['y']].insert(player['x']+1,"M")
        resources_map[player['y']].insert(player['x']+1,"M")
        player['x'] += 1
        player['turns'] -= 1
        player['steps'] += 1
        clear_fog(player,resources_map)
        return 
    
def portal(player): 
    global PORTAL_POSITION_X
    global PORTAL_POSITION_Y
    copper_price_random = randint(1,3)
    silver_price_random = randint(5,8)
    gold_price_random = randint(10,18)

    copper_earning = 0
    silver_earning = 0
    gold_earning = 0

    global CURRENT_MAP_LAYOUT
    CURRENT_MAP_LAYOUT[player['y']].pop(player['x'])
    resources_map[player['y']].pop(player['x'])

    CURRENT_MAP_LAYOUT[player['y']].insert(player['x'],"P")
    resources_map[player['y']].insert(player['x'],"P")

    PORTAL_POSITION_X = player['x']
    PORTAL_POSITION_Y = player['y']
    player['x'] = 1
    player['y'] = 1

    CURRENT_MAP_LAYOUT[1].pop(1)
    resources_map[1].pop(1)

    CURRENT_MAP_LAYOUT[1].insert(1,"M")
    resources_map[1].insert(1,"M")


    print("-----------------------------------------------------")
    print("You place your portal stone here and zap back to town.")

    if player['copper'] > 0:
        copper_earning = player['copper']*copper_price_random
        print("You sell {} copper ore for {} GP".format(player['copper'],copper_earning))
    
    if player["silver"] > 0:
        silver_earning = player['silver']*silver_price_random
        print("You sell {} silver ore for {} GP.".format(player['silver'],silver_earning))

    if player['gold'] >0:
        gold_earning = player['gold']*gold_price_random
        print("You sell {} gold ore for {} GP.".format(player['gold'],gold_earning))
        
    total_earning = copper_earning+silver_earning+gold_earning
    player['gp'] += total_earning
    print("You now have {} GP!".format(player['gp']))
    player['day'] += 1
    player['turns'] = TURNS_PER_DAY
    player['copper'] = 0
    player['silver'] = 0
    player['gold'] = 0
    player['load'] = 0
    return 
    



#--------------------------- MAIN GAME ---------------------------
initialize_game(resources_map, fog , player)
print("---------------- Welcome to Sundrop Caves! ----------------")
print("You spent all your money to get the deed to a mine, a small")
print("  backpack, a simple pickaxe and a magical portal stone.")
print()
print("How quickly can you get the 500 GP you need to retire")
print("  and live happily ever after?")
print("-----------------------------------------------------------")   
show_main_menu()
user_choice = input("Your choice? ")
stop = False


if user_choice.lower() == "n": 
    
    
    NAME = input("Greetings, miner! What is your name? ")
    print("Pleased to meet you, {}. Welcome tp Sundrop Town!".format(NAME))
    while not(stop):
        show_town_menu(player['day'])
        N_choice = input("Your choice? ")

        if N_choice.lower() == "i":
            player_information(player)
        elif N_choice.lower() == "b": 
            buy_stuff(player)
        elif N_choice.lower() == "m":
            
            map_print_fog()
        elif N_choice.lower() =='e':
            if player['day'] > 1:
                player['x'] = PORTAL_POSITION_X
                player['y'] = PORTAL_POSITION_Y

                PORTAL_POSITION_X = 0
                PORTAL_POSITION_Y = 0
                CURRENT_MAP_LAYOUT[1].pop(1)
                resources_map[1].pop(1)

                CURRENT_MAP_LAYOUT[1].insert(1,"T")
                resources_map[1].insert(1,"T")

                CURRENT_MAP_LAYOUT[player['y']].pop(player['x'])
                resources_map[player['y']].pop(player['x'])

                CURRENT_MAP_LAYOUT[player['y']].insert(player['x'],"M")
                resources_map[player['y']].insert(player['x'],"M")


            enter_stop = False
            while not(enter_stop):
                print("---------------------------------------------------")
                print("                     Day{}                         ".format(player['day']))
                print("---------------------------------------------------")
                print("Day {}".format(player['day']))
                draw_view(player,resources_map)
                print(f"Turns left:{player['turns']}    Load:{player['load']} / {CURRENT_BAG_CAPACITY}    Steps:{player['steps']}")
                print("(WASD) to move")
                print("(M)ap, (I)nformation, (P)ortal, (Q)uit to main menu")


                user_action = input("Action?")

                
                if user_action.lower() == 'w' or user_action.lower() =='s' or user_action.lower() == 'a' or user_action.lower() == 'd':
                    if player['turns'] == 0:
                        print("You ran out of turns, try again tommorrow.")
                        continue
                    else: 
                        movement_input(player,resources_map,user_action)
                elif user_action.lower() == "m":
                    map_print_fog()
                elif user_action.lower() == "q":
                    enter_stop = True
                    continue 
                elif user_action.lower() == 'p':
                    portal(player)
                    enter_stop = True
                    continue
                elif user_action.lower() == "i":
                    player_in_game_information(player)




                    
                

            
        
        

        

















