import random
f1 = open("dictionary.txt","r")
words=[i.replace('\n' ,'') for i in f1.readlines()]
lastchar1 = ""
lastchar2 = ""
userchoice = input("user : ")
if userchoice in words:
    lastchar1 = userchoice[-1]
    for i in range(0,10,1):
        temp = list(filter(lambda x:x.startswith(lastchar1),words))
        randnum = random.randrange(0,len(temp))
        computerchoice = temp[randnum]
        print("Computer :",computerchoice)
        lastchar2 = computerchoice[-1]
        userchoice = input("user : ")
        if userchoice.startswith(lastchar2) and (userchoice in words):              
        break
