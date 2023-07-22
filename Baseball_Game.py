def score(myList):

    newList = []
    for item in myList:
        if item != "D" and item !="C" and item != "+":
            newList.append(int(item))
        elif newList==True and item =="C": 
            del newList[-1]
        elif newList==True and item =="D":
            newList.append(int(newList[-1]) * 2)
        elif newList==True and item =="+":
            newList.append(int(newList[-1])+int(newList[-2]))
        print(newList)
        print(sum(newList))


#ops = ["5", "2", "C", "D","+"]
#ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
#ops=["C","D","+","5","3"]
ops=["4","+","5","C","D","3"]
score(ops)


