# Ang Hao Yi 10273989D

path = "C:\\Text Folders\\Minitask 03\\"
ingredients_list = []

def calculate_cookie_score(ingredients):
    score_local = 0
    for x in ingredients: 
        if x == "sugar": 
            score_local += 5
        elif x == "butter": 
            score_local += 4
        elif x == "chocolatechips":
            score_local += 3
        elif x == "flour": 
            score_local -= 2
        else: 
            score_local += 1
    return score_local 

def process_cookie_file(filename):
    with open(path+filename,"r") as file :
        info = file.readlines()
        counter = 0
        for x in info: 
            filtered_info = x.strip().split(",")
            ingredients_list.append(list())
            ingredients_list[counter].append(filtered_info[0])
            ingredients_list[counter].append(list())
            
            for y in range(1,len(filtered_info)): 
                ingredients_list[counter][1].append(filtered_info[y].replace(" ",""))
            counter += 1


def comment(final_score): 

    if final_score <5: 
        print("This cookie is a disaster")
    elif final_score <= 15: 
        print("This cookie is mediacore, but we're not judging.")
    else: 
        print("This cookie deservers a gold medal.")
            

process_cookie_file('ingredients.txt')
stop = False

while not(stop): 
    yes_no = input("Would you like to score some cookies? (Type 'Stop' to quit, 'Yes' to start): ").lower()

    if yes_no == 'stop': 
        stop = True 
        print("Goodbye!")
        continue 
    
    for i in range(len(ingredients_list)):
        ingredients = ingredients_list[i][1]
        score = calculate_cookie_score(ingredients)  
        print("Cookie: {}".format(ingredients_list[i][0]))
        print("Score: {}".format(score))
        comment(score)



        


