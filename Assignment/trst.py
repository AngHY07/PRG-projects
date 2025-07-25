

high_score_content = [["john",25,23,540,'23445'],['james',25,24,540,'442343']]

high_score_content.sort(key=lambda x:x[1])
changes_days = True

while changes_days: 
        changes_days = False

        for x in range(len(high_score_content)):
            if high_score_content[x][4] == high_score_content[-1][4]:
                continue
            
            if high_score_content[x][1] == high_score_content[x+1][1]:
                temp = "NA"
                if high_score_content[x][2] < high_score_content[x+1][2]:
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
            
            if high_score_content[y][2] == high_score_content[y+1][2]:
                temp_2 = "NA"
                if high_score_content[y][3]< high_score_content[y+1][3]:
                    temp_2 = high_score_content[y+1]
                    high_score_content.pop(y+1)
                    high_score_content.insert(y,temp_2)
                    changes_steps = True


print(high_score_content)