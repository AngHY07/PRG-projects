path = "C:\\Text Folders\\Minitask 03\\"

def empty_file_check(filename): 
    with open(path + filename, 'r') as file:
        info = file.read()
        if info == "": 
            return "Empty File"


def read_snacks_file(filename):
    """Read snacks and their prices from the file and return two separate lists:
    one for names and one for prices."""
    snack_names = []
    snack_prices = []

    # Read the file and split into snack names and prices
    with open(path + filename, 'r') as file:       
        for line in file:
            name_price = line.strip().split(',')
            snack_names.append(name_price[0])
            snack_prices.append(float(name_price[1]))
            
        return snack_names,snack_prices
            

def get_valid_budget(list):
    """Prompt the user for a valid snack budget (greater than 0)."""
    while True:
        budget = float(input("Enter your snack budget: "))
        lowest_cost = 10000
        for price in list: 
            if price < lowest_cost:
                lowest_cost = price
        if budget < lowest_cost:
            print("Your budget is too low! Try asking the office for a raise.")
        else:
            return budget

def classify_snack(price):
    """Classify the snack into a category based on its price."""
    if price < 2.0:
        return "Healthy snack"
    elif price <= 5.0:
        return "Snack of the Gods"
    else:
        return "Luxury snack"

def eligible_snacks(budget): 
    eligible_list = []
    counter = 0
    list_count = 0
    for x in snack_prices: 
        if budget >= x:
            eligible_list.append(list())
            eligible_list[list_count].append(snack_names[counter])
            eligible_list[list_count].append(x)
            list_count += 1
        counter += 1
    return eligible_list


stop = False
while not(stop):

    if empty_file_check("snack_price.txt") == "Empty File": 
        stop = True 
        continue

    snack_names,snack_prices = read_snacks_file("snack_price.txt")
    budget = get_valid_budget(snack_prices)
    eligible_list = eligible_snacks(budget)

    print('Here is what you can buy:')
    for x in range(len(eligible_list)): 
        print("- {} (${:.2f}) - {}".format(eligible_list[x][0],eligible_list[x][1],classify_snack(eligible_list[x][1])))
    
    with open(path + "snack-list.txt",'w') as file: 
        for y in range(len(eligible_list)):
            file.write("{},{:.2f}\n".format(eligible_list[y][0],eligible_list[y][1]))
    print('Your snack list has been saved to \'snack_list.txt\'')
    stop = True


    


