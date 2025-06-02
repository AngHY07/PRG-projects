# Ang Hao Yi 10273989D

path = "C:\\Text Folders\\minitask02\\"

book_update =[]
days_update = []
stop = False

while not(stop): 

    title = str(input("Enter book title (or type 'stop' to finish): "))

    if title == "stop":
            stop = True
            continue  
            
    days_overdue = int(input("Enter days overdue: "))
    book_update.append (title)
    days_update.append(days_overdue)


with open(path + "overdue_books.txt", "r") as info:

    information = info.readlines()
    booktitle =[]
    overdue_days = []
    total = 0
    price = []
    glare = []

    counter = 0

    while counter < len(information):

        info_split = information[counter].strip().split(";")
        booktitle.append(info_split[0])
        overdue_days.append(int(info_split[1]))
        counter = counter + 1
    
    booktitle.extend(book_update)
    overdue_days.extend(days_update)

    count = 0
    while count < len(overdue_days):
        days = overdue_days[count]

        if  days<= 5: 
            cost = days*0.5
            glare.append("")
        elif days <= 10:
            cost = days*1
            glare.append("")
        else: 
            cost = days*1.5
            glare.append("-.-")

        total += cost 
        price.append(cost)
        count += 1


with open(path + "fines_report.txt","w") as file2: 
    counting = 0 

    while counting < len(booktitle): 
        file2.write(f"{booktitle[counting]} {overdue_days[counting]} - ${price[counting]:.2f} {glare[counting]}\n")
        counting += 1

print("Total books processed: {}".format(len(booktitle)))
print("Overall total fine amount: ${:.2f}".format(total))




    




    
