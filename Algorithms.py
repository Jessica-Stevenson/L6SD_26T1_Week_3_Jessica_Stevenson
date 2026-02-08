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

print ("Selection Sort: ", myList)

#Merge sort (What the ever loving donut is this)

#The splitening
def mergeSort(arr):
    #This checks if the list actually has things to sort
    if len(arr) <= 1:
        return arr

    #This spilts the list in half
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    #Calls the mergeSort Function for both halfs and outs them into a sorted variable
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    #Returns the data for me to use
    return merge(sortedLeft, sortedRight)

#The actual sorting
def merge(left, right):
    #Result holds the merged list
    result = []
    #I and J tracks the position
    i = j = 0

    #Loops until sorted
    while i < len(left) and j < len(right):
        #Compares two elements and Appends the smaller one
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #Adds leftover (and leaves the mergesort fuction to do it's job)
    result.extend(left[i:])
    result.extend(right[j:])

    return result

myList = [33, 52, 87, 69, 13, 2, 19, 25, 9, 21]
mysortedlist = mergeSort(myList)
print("Merge Sort: ", mysortedlist)