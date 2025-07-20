path = "C:\\Text Folders\\"

with open(path+"blankcheck.txt",'r') as file: 

    info = file.read()
    print(info) 