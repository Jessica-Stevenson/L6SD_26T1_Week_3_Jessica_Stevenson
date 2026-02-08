#Selection Sort
myList = [33, 52, 87, 69, 13, 2, 19, 25, 9, 21]


l = len(myList)

#I is the current position we are trying to fill so it starts at the first index and makes it's way through
#range makes it start at 0
for i in range(l-1):
    #Tells the code that hey the first index is the one we need to sort
    min_index = i
    #This is the actual sort. It compares numbers together to find the smallest one
    for j in range (i+1, l):
        if myList[j] < myList[min_index]:
            min_index = j
    #Puts the number in the right place once it's found to be out of place. Does it by taking it out of the list then inserting it back in at the right spot
    min_value = myList.pop(min_index)
    myList.insert(i, min_value)

print (myList)