#ex
katudon = 0
kaisendon = 0
gyudon = 0

vote =  ""
while vote != 0:
    
    vote = int(input("投票\n海鮮丼(1),カツ丼(2),牛丼(3):"))
       
        
    if vote == 1:
        kaisendon += 1
    elif vote == 2:
        katudon += 1
    elif vote == 3:
        gyudon += 1
    
print("海鮮丼:",kaisendon,"カツ丼",katudon,"牛丼",gyudon)

    



    