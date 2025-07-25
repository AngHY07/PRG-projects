from random import randint
import secrets
path = "C:\\Text Folders\\Assignment 35%\\"

high_score_content = []
player = {}


eligible_for_mine = True
MAP_WIDTH = 0
MAP_HEIGHT = 0


TURNS_PER_DAY = 20
WIN_GP = 500

resources_map = []
current_map_layout = [list("################################"),
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

def clear_safe_content():
    global player_safe_information
    global resources_map_safe_file
    global portal_position_x_safe
    global portal_position_y_safe
    global name_safe
    global fog_safe_file

    player['name'] = "NA"
    player_safe_information = {}
    resources_map_safe_file = ["map"]
    portal_position_x_safe = 0
    portal_position_y_safe = 0

def load_map(filename, map_struct,player):
    map_file = open(path + filename, 'r')
    global MAP_WIDTH
    global MAP_HEIGHT
    global current_map_layout

    current_map_layout[player['y']].pop(player['x'])
    current_map_layout[player['y']].insert(player['x'],"M")

    file_info = map_file.readlines()
    for lines in file_info: 
        map_struct.append(list(lines.strip("\n")))

    for x in range(len(map_struct)):
        map_struct[x].insert(0,"#")
        
    for x in range(len(map_struct)):
        map_struct[x].append("#")

    map_struct.insert(0,list("################################"))
    map_struct.append(list("################################"))

    map_struct[1][1] ="M"

    
    MAP_WIDTH  = len(map_struct[0])
    MAP_HEIGHT = len(map_struct)
    map_file.close()

def map_print_fog():
    global current_map_layout
    global MAP_WIDTH

    print("+",end="")
    for y in range(MAP_WIDTH-2):
        print("-",end="")
    print("+")

    for line in range(1,len(current_map_layout)-1):
        print("|",end="")
        for column in range(1,len(current_map_layout[line])-1):
            print(current_map_layout[line][column],end="")
        print("|")

    print("+",end="")
    for y in range(MAP_WIDTH-2):
        print("-",end="")
    print("+")

def initialize_game(resources_map,player):

    player['high score count'] = 0 
    player['portal x'] = 1
    player['portal y'] =1
    player['x'] = 1
    player['y'] = 1
    player['copper'] = 0
    player['silver'] = 0
    player['gold'] = 0
    player['day'] = 1
    player['steps'] = 0
    player['turns'] = TURNS_PER_DAY
    player['load'] = 0
    player['gp'] = 0
    player['pickaxe level'] = 1
    player['current capacity'] = 10
    player['pickaxe ore'] = "copper"
    player['name'] = 'NA'
    player['portal activated'] = "False"


    load_map("level1.txt",resources_map,player)
    clear_fog(player,resources_map)
    
def initialize_game_safe_folder(player):
    global current_map_layout
    global resources_map

    current_map_layout.clear()
    resources_map.clear()

    with open(path + 'fogmap.txt','r') as file:
        info = file.read().split(",")
        info.pop(-1)
        for lines in info:
            current_map_layout.append(list(lines))
    
    with open(path + 'resource.txt', 'r') as file_2:

        info_2 = file_2.read().split(',')
        info_2.pop(-1)
        for lines in info_2:
            resources_map.append(list(lines))
    
    with open(path +'values.txt') as file_3:

        info_3 = file_3.readlines()

        for x in range(15):
            info_split = info_3[x].strip().split(",")
            player[info_split[0]] = int(info_split[1])
        
        for x in range(15,18):
            info_split_2 = info_3[x].strip().split(",")
            player[info_split_2[0]] = str(info_split_2[1])

def draw_view (player):
    global current_map_layout
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

def show_main_menu():
    print()
    print("--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
    print("(H)igh scores")
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
    print("Name: {}".format(player['name']))
    print("Portal position: ({},{})".format(player['portal x']-1,player['portal y']-1))
    print("Pickaxe level: {} ({})".format(player['pickaxe level'],player['pickaxe ore']))
    print("------------------------------")
    print("Load: {}/{}".format(player['load'],player['current capacity']))
    print("------------------------------")
    print("GP: {}".format(player["gp"]))
    print("Steps taken: {}".format(player['steps']))
    print("------------------------------")

def player_in_game_information(player):
    print("----- Player Information -----")
    print("Name: {}".format(player['name']))
    print("Current position: ({},{})".format(player['x']-1,player['y']-1))
    print("Pickaxe level: {} ({})".format(player['pickaxe level'],player['pickaxe ore']))
    print("Gold: {}".format(player['gold']))
    print("Silver: {}".format(player['silver']))
    print("Copper: {}".format(player['copper']))
    print("------------------------------")
    print("Load: {} / {}".format(player['load'],player['current capacity']))
    print("------------------------------")
    print("GP: {}".format(player['gp']))
    print("Steps taken: {}".format(player['steps']))
    print("------------------------------")
    
def buy_stuff(player):

    if player['pickaxe level'] == 1:
                upgrade_ore = "silver"
                upgrade_price = 50
    elif player['pickaxe level'] == 2:
                upgrade_ore = "gold"
                upgrade_price = 150
    print("----------------------- Shop Menu -------------------------")
    print("(P) ickaxe upgrade to Level {} to mine {} ore for {} GP".format(player['pickaxe level']+1,upgrade_ore,upgrade_price))
    print("(B) ackpack upgrade to carry {} items for {} GP".format((player['current capacity']+2),(player['current capacity']*2)))
    print("(L) eave shop")
    print("-----------------------------------------------------------")
    print("GP: {}".format(player['gp']))
    print("-----------------------------------------------------------")
    buy_1st_choice = input("Your choice? ")

    if buy_1st_choice.lower() == "b":
        while True: 
            
            print("----------------------- Shop Menu -------------------------")
            print("(B) ackpack upgrade to carry {} items for {} GP".format((player['current capacity']+2),(player['current capacity']*2)))
            print("(L) eave shop") 
            print("----------------------------------------------------------")
            print("GP: {}".format(player['gp']))
            print("----------------------------------------------------------")
            buy_2nd_choice = input("Your choice? ")
            if buy_2nd_choice.lower() == "l":
                return None
            elif buy_2nd_choice.lower() == "b":
                if player['gp'] < player['current capacity']*2:
                    print("You do not have enough GP! Come back again later.")
                else:
                    print("Congratulations! You can now carry {} items!".format(player['current capacity']+2))
                    player['gp'] -= (player['current capacity']*2)
                    player['current capacity']+= 2

    
    elif buy_1st_choice.lower() == "p":
        while True : 
            if player['pickaxe level'] == 1:
                upgrade_ore = "silver"
                upgrade_price = 50
            elif player['pickaxe level'] == 2:
                upgrade_ore = "gold"
                upgrade_price = 150
            print("----------------------- Shop Menu -------------------------")
            print("(P) ickaxe upgrade to Level {} to mine {} ore for {} GP".format(player['pickaxe level']+1,upgrade_ore,upgrade_price))
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
                    print("Congratulations you have upgraded you pickaxe to level {}.".format(player['pickaxe level']+1))
                    player['pickaxe level'] += 1
                    player['pickaxe ore'] = upgrade_ore
                    player['gp'] -= upgrade_price

def ore_mining_w_s(player,value,copper_random,silver_random,gold_random):
    global eligible_for_mine
    if resources_map[player['y']+value][player['x']] == "C":
            print("---------------------------------------------------")
            print("You mined {} piece(s) of copper.".format(copper_random))

            if (player['load']+copper_random) > player['current capacity']:
                remaining_slots = player['current capacity']-player['load']
                print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                player['load'] = player['current capacity']
                player['copper'] += remaining_slots
            else :
                player['load'] += copper_random
                player['copper'] += copper_random

    elif resources_map[player['y']+value][player['x']] == "S":
            if player['pickaxe level'] == 1:
                print("Your pickaxe level is not high enough to mine this ore!")
                eligible_for_mine = False
            else:
                print("---------------------------------------------------")
                print("You mined {} piece(s) of silver.".format(silver_random))

                if (player['load']+silver_random) > player['current capacity']:
                    remaining_slots = player['current capacity']-player['load']
                    print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                    player['load'] = player['current capacity']
                    player['silver'] += remaining_slots
                else :
                    player['load'] += silver_random
                    player['silver'] += silver_random
            
    elif resources_map[player['y']+value][player['x']] == "G":
            if player['pickaxe level'] < 3:
                print("Your pickaxe level is not high enough to mine this ore!")
                eligible_for_mine = False
            else: 
                print("---------------------------------------------------")
                print("You mined {} piece(s) of gold.".format(gold_random))

                if (player['load']+gold_random) > player['current capacity']:
                    remaining_slots = player['current capacity']-player['load']
                    print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                    player['load'] = player['current capacity']
                    player['gold'] += remaining_slots
                else :
                    player['load'] += gold_random
                    player['gold'] += gold_random

def ore_mining_a_d(player,value,copper_random,silver_random,gold_random):
    global eligible_for_mine

    if resources_map[player['y']][player['x']+value] == "C":
            print("---------------------------------------------------")
            print("You mined {} piece(s) of copper.".format(copper_random))

            if (player['load']+copper_random) > player['current capacity']:
                remaining_slots = player['current capacity']-player['load']
                print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                player['load'] = player['current capacity']
                player['copper'] += remaining_slots

            else :
                player['load'] += copper_random
                player['copper'] += copper_random
    elif resources_map[player['y']][player['x']+value] == "S":
            if player['pickaxe level'] == 1:
                print("Your pickaxe level is not high enough to mine this ore!")
                eligible_for_mine = False
            else:  
                print("---------------------------------------------------")
                print("You mined {} piece(s) of silver.".format(silver_random))

                if (player['load']+silver_random) > player['current capacity']:
                    remaining_slots = player['current capacity']-player['load']
                    print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                    player['load'] = player['current capacity']
                    player['silver'] += remaining_slots
                else :
                    player['load'] += silver_random
                    player['silver'] += silver_random
    elif resources_map[player['y']][player['x']+value] == "G":
            if player['pickaxe level'] < 3:
                print("Your pickaxe level is not high enough to mine this ore!")
                eligible_for_mine = False
            else:
                print("---------------------------------------------------")
                print("You mined {} piece(s) of gold.".format(gold_random))

                if (player['load']+gold_random) > player['current capacity']:
                    remaining_slots = player['current capacity']-player['load']
                    print("... but you can only carry {} more piece(s)!".format(remaining_slots))
                    player['load'] = player['current capacity']
                    player['gold'] += remaining_slots
                else :
                    player['load'] += gold_random
                    player['gold'] += gold_random

def upper_fog_left(player,resources_map):
    global current_map_layout
    current_map_layout[player['y']-1][player['x']-1] = resources_map[player['y']-1][player['x']-1]
    current_map_layout[player['y']-1][player['x']] = resources_map[player['y']-1][player['x']]
    
def upper_fog_right(player,resources_map):

    current_map_layout[player['y']-1][player['x']] = resources_map[player['y']-1][player['x']]
    current_map_layout[player['y']-1][player['x']+1] = resources_map[player['y']-1][player['x']+1]

def right_side_fog(player,resources_map):
    global current_map_layout
    current_map_layout[player['y']][player['x']+1]= resources_map[player['y']][player['x']+1]
    
def left_side_fog(player,resources_map): 
    global current_map_layout
    current_map_layout[player['y']][player['x']-1]= resources_map[player['y']][player['x']-1]
    
def below_fog_right(player,resources_map):
    global current_map_layout

    current_map_layout[player['y']+1][player['x']]= resources_map[player['y']+1][player['x']]
    current_map_layout[player['y']+1][player['x']+1] = resources_map[player['y']+1][player['x']+1]
    
def below_fog_left(player,resources_map):
    global current_map_layout

    current_map_layout[player['y']+1][player['x']-1]= resources_map[player['y']+1][player['x']-1]
    current_map_layout[player['y']+1][player['x']] = resources_map[player['y']+1][player['x']]
    
def clear_fog(player,resources_map):

    if current_map_layout[player['y']-1][player['x']] == "#" and current_map_layout[player['y']][player['x']+1] =="#":
        left_side_fog(player,resources_map) 
        below_fog_left(player,resources_map)
    elif current_map_layout[player['y']-1][player['x']] == "#" and current_map_layout[player['y']][player['x']-1] =="#":
        right_side_fog(player,resources_map)
        below_fog_right(player,resources_map)
    elif current_map_layout[player['y']+1][player['x']] == "#" and current_map_layout[player['y']][player['x']+1] =="#":
        left_side_fog(player,resources_map)
        upper_fog_left(player,resources_map)
    elif current_map_layout[player['y']+1][player['x']] == "#" and current_map_layout[player['y']][player['x']-1] =="#":
        right_side_fog(player,resources_map)
        upper_fog_right(player,resources_map)
    elif current_map_layout[player['y']-1][player['x']] == "#":
        left_side_fog(player,resources_map)
        right_side_fog(player,resources_map)
        below_fog_left(player,resources_map)
        below_fog_right(player,resources_map)
    elif current_map_layout[player['y']+1][player['x']] == "#":
        left_side_fog(player,resources_map)
        right_side_fog(player,resources_map)
        upper_fog_left(player,resources_map)
        upper_fog_right(player,resources_map)
    elif current_map_layout[player['y']][player['x']+1] == "#":
        left_side_fog(player,resources_map)
        upper_fog_left(player,resources_map)
        upper_fog_right(player,resources_map)
        below_fog_left(player,resources_map)
        below_fog_right(player,resources_map)
    elif current_map_layout[player['y']][player['x']-1] == "#":
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
    global TURNS_PER_DAY
    global eligible_for_mine

    copper_price = randint(1,5)
    silver_price= randint(1,3)
    gold_price = randint(1,2)
    # W
    if user_input.lower() == "w":
        if player['y'] == 1:
            print("You are at the barrier, you can't move further up")
            return 

        ore_mining_w_s (player,-1,copper_price,silver_price,gold_price)
        if eligible_for_mine == True:
            # Remove original postion
            current_map_layout[player['y']].pop(player['x'])
            resources_map[player['y']].pop(player['x'])

            #Replace original position with blank space
            current_map_layout[player['y']].insert(player['x']," ")
            resources_map[player['y']].insert(player['x']," ")

            # Remove the position on top
            current_map_layout[player['y']-1].pop(player['x'])
            resources_map[player['y']-1].pop(player['x'])

            #Replace position on top with M
            current_map_layout[player['y']-1].insert(player['x'],"M")
            resources_map[player['y']-1].insert(player['x'],"M")

        
            player['y'] -= 1 
            player['turns'] -= 1
            player['steps'] += 1
            clear_fog(player,resources_map)
        
        return 
    
    #S 
    elif  user_input.lower() == "s":
        if current_map_layout[player['y']+1][player['x']] == "#":
            print("You are at the barrier, you can't move further down")
            return 

        ore_mining_w_s (player,1,copper_price,silver_price,gold_price)
    
        if eligible_for_mine == True:
            # Remove original postion
            current_map_layout[player['y']].pop(player['x'])
            resources_map[player['y']].pop(player['x'])

            #Replace original position with blank space
            if player["y"] == 1 and player["x"]  == 1:
                current_map_layout[player['y']].insert(player['x'],"T")
                resources_map[player['y']].insert(player['x'],"T")
            else: 
                current_map_layout[player['y']].insert(player['x']," ")
                resources_map[player['y']].insert(player['x']," ")

            # Remove the position on bottom
            current_map_layout[player['y']+1].pop(player['x'])
            resources_map[player['y']+1].pop(player['x'])

            #Replace position on bottom with M
            current_map_layout[player['y']+1].insert(player['x'],"M")
            resources_map[player['y']+1].insert(player['x'],"M")

  
            player['y'] += 1
            player['turns'] -= 1
            player['steps'] += 1
            clear_fog(player,resources_map)
        
        return 
    
    #A
    elif  user_input.lower() == "a":
        if current_map_layout[player['y']][player['x']-1] == "#":
            print("You are at the barrier, you can't move to your left")
            return 

        ore_mining_a_d(player,-1,copper_price,silver_price,gold_price)

        if eligible_for_mine == True:
            # Remove original postion
            current_map_layout[player['y']].pop(player['x'])
            resources_map[player['y']].pop(player['x'])

            #Replace original position with blank space
            current_map_layout[player['y']].insert(player['x']," ")
            resources_map[player['y']].insert(player['x']," ")

            # Remove the position on right
            current_map_layout[player['y']].pop(player['x']-1)
            resources_map[player['y']].pop(player['x']-1)

            #Replace position on right with M
            current_map_layout[player['y']].insert(player['x']-1,"M")
            resources_map[player['y']].insert(player['x']-1,"M")


            player['x'] -= 1
            player['turns'] -= 1
            player['steps'] += 1
            clear_fog(player,resources_map)

        return 

    #D
    elif  user_input.lower() == "d":
        if current_map_layout[player['y']][player['x']+1] == "#":
            print("You are at the barrier, you can't move to your right")
            return 

        ore_mining_a_d(player,1,copper_price,silver_price,gold_price)

        if eligible_for_mine == True:
            # Remove original postion
            current_map_layout[player['y']].pop(player['x'])
            resources_map[player['y']].pop(player['x'])

            #Replace original position with blank space
            if player["y"] == 1 and player["x"]  == 1:
                current_map_layout[player['y']].insert(player['x'],"T")
                resources_map[player['y']].insert(player['x'],"T")
            else: 
                current_map_layout[player['y']].insert(player['x']," ")
                resources_map[player['y']].insert(player['x']," ")

            # Remove the position on right
            current_map_layout[player['y']].pop(player['x']+1)
            resources_map[player['y']].pop(player['x']+1)

            #Replace position on right with M
            current_map_layout[player['y']].insert(player['x']+1,"M")
            resources_map[player['y']].insert(player['x']+1,"M")
            player['x'] += 1
            player['turns'] -= 1
            player['steps'] += 1
            clear_fog(player,resources_map)
        return 
    
def portal(player): 


    copper_price_random = randint(1,3)
    silver_price_random = randint(5,8)
    gold_price_random = randint(10,18)

    copper_earning = 0
    silver_earning = 0
    gold_earning = 0

 
    current_map_layout[player['y']].pop(player['x'])
    resources_map[player['y']].pop(player['x'])

    current_map_layout[player['y']].insert(player['x'],"P")
    resources_map[player['y']].insert(player['x'],"P")

    player['portal x'] = player['x']
    player['portal y']= player['y']


    current_map_layout[1].pop(1)
    resources_map[1].pop(1)

    current_map_layout[1].insert(1,"M")
    resources_map[1].insert(1,"M")


    print("-----------------------------------------------------")
    if player['turns'] == 0:
        print("You can't carry any more, so you can't go that way.")
        print("You are exhausted.")
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
    player['portal activated'] = "True"
    return 
    

def end_game(player):
    print("-------------------------------------------------------------")
    print("Woo-hoo! Well done, {}, you have {} GP!".format(player['name'],player['gp']))
    print("You now have enough to retire and play video games every day.")
    print("And it only took you {} days and {} steps! You win!".format(player['day']-1 , player['steps']))
    
def safe_game():
            global player
            with open(path+"values.txt",'w') as file:
                for x in player.keys():
                    values = player[x]
                    file.write("{},{}\n".format(x,str(values)))

            with open(path+"fogmap.txt",'w') as file_2:
                for lines in current_map_layout:
                    for char in lines:
                        file_2.write(char)
                    file_2.write(",")

            with open(path+"resource.txt","w") as file_3:
                for lines in resources_map:
                    for char in lines:
                        file_3.write(char)
                    file_3.write(",")


def rearrange_score():
    global high_score_content

    high_score_content.sort(key=lambda x:x[1])

    changes_days = True
    while changes_days: 
        changes_days = False

        for x in range(len(high_score_content)):
            if high_score_content[x][4] == high_score_content[-1][4]:
                continue
            
            if high_score_content[x][1] == high_score_content[x+1][1]:
                temp = "NA"
                if high_score_content[x][2] > high_score_content[x+1][2]:
                    temp = high_score_content[x+1]
                    high_score_content.pop(x+1)
                    high_score_content.insert(x,temp)
                    changes_days = True
    
    changes_steps = True

    while changes_steps:
        changes_steps = False

        for y in range(len(high_score_content)):
            if high_score_content[y][4] == high_score_content[-1][4]:
                continue
            
            if high_score_content[y][1] == high_score_content[y+1][1] and high_score_content[y][2] == high_score_content[y+1][2]:
                temp_2 = "NA"
                if high_score_content[y][3] < high_score_content[y+1][3]:
                    temp_2 = high_score_content[y+1]
                    high_score_content.pop(y+1)
                    high_score_content.insert(y,temp_2)
                    changes_steps = True




    


#--------------------------- MAIN GAME ---------------------------

print("---------------- Welcome to Sundrop Caves! ----------------")
print("You spent all your money to get the deed to a mine, a small")
print("  backpack, a simple pickaxe and a magical portal stone.")
print()
print("How quickly can you get the 500 GP you need to retire")
print("  and live happily ever after?")
print("-----------------------------------------------------------")   

whole_game_stop = False
while not(whole_game_stop):
    show_main_menu()
    user_choice = input("Your choice? ")
    stop = False

    if user_choice.lower() == "n" or user_choice.lower()=="l" or user_choice.lower() =="q" or user_choice.lower =="h":
        if user_choice.lower() == "n": 
            resources_map =[]
            current_map_layout = [list("################################"),
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
            initialize_game(resources_map,player)
            player['name'] = input("Greetings, miner! What is your name? ")
            print("Pleased to meet you, {}. Welcome to Sundrop Town!".format(player['name']))
        elif user_choice.lower() == "l":
            initialize_game(resources_map,player)
            initialize_game_safe_folder(player)
        elif user_choice.lower() == "q":
            whole_game_stop = True
            continue
        elif user_choice.lower() == "h":
            rearrange_score()
            print("{}    {}    {}    {}".format("Names",'Days','Steps','GP'))
            for i in range(len(high_score_content)):
                print("{}    {}    {}    {}".format(high_score_content[i][0],high_score_content[i][1],high_score_content[i][2],high_score_content[i][3]))
    else: 
        print("Your input is not valid!")
        continue

    while not(stop):
            secret = str(secret.token_hex(4))
            if player['gp'] >= 500:
                end_game(player)
                high_score_content.append(list())
                high_score_content[player['high score count']].append(player['names'])
                high_score_content[player['high score count']].append(player['day'])
                high_score_content[player['high score count']].append(player['steps'])
                high_score_content[player['high score count']].append(player['gp'])
                high_score_content[player['high score count']].append(secret)
                stop = True
                continue
                
            show_town_menu(player['day'])
            choice = input("Your choice? ")

            if choice.lower() == "i" or choice.lower() == "b" or choice.lower() == "m" or choice.lower() == "e" or choice.lower() == "q" or choice.lower()=="v":
                
                if choice.lower() == "i":
                    player_information(player)
                elif choice.lower() == "b": 
                    buy_stuff(player)
                elif choice.lower() == "m":   
                    map_print_fog()
                elif choice.lower() =='e':
                    if player['day'] > 1:
                        current_map_layout[1][1]= "T"
                        resources_map[1][1] ="T"

                    print("---------------------------------------------------")
                    print("                     Day{}                         ".format(player['day']))
                    print("---------------------------------------------------")
                    if player['portal activated'] == "True":

                        current_map_layout[player['portal y']].pop(player['portal x'])
                        resources_map[player['portal y']].pop(player['portal x'])

                        current_map_layout[player['portal y']].insert(player['portal x'],"M")
                        resources_map[player['portal y']].insert(player['portal x'],"M")   
                        player['portal x'] = 1
                        player['portal y'] = 1
                        player['portal activated'] = "False"


                    enter_stop = False
                    while not(enter_stop):

                        print("Day {}".format(player['day']))
                        draw_view(player)
                        print(f"Turns left:{player['turns']}    Load:{player['load']} / {player['current capacity']}    Steps:{player['steps']}")
                        print("(WASD) to move")
                        print("(M)ap, (I)nformation, (P)ortal, (Q)uit to main menu")


                        user_action = input("Action?")
                        if user_action.lower() == 'w' or user_action.lower() =='s' or user_action.lower() == 'a' or user_action.lower() == 'd':
                            if player['turns'] == 0:
                                portal(player)
                                enter_stop = True
                                continue
                            else: 
                                movement_input(player,resources_map,user_action)
                                eligible_for_mine = True
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
                        else: 
                            print("Invalid input!")
                            continue
                elif choice.lower() =="q":
                    stop = True
                    continue
                elif choice.lower() =="v":
                    safe_game()
                    print("Game has been saved successfully")
            else: 
                print("Input is not valid!")
                continue




                    
                

            
        
        

        

















