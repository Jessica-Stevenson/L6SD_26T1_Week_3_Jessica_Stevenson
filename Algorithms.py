#Selection Sort
myList = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]


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

print ("Selection Sort:", myList)

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

myList = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
mysortedlist = mergeSort(myList)
print("Merge Sort:", mysortedlist)

#Quick Sort
def partition(array, low, high):
    #Last Element is chosen
    pivot = array[high]
    #Figures out which numbers are lower onthe list
    i = low - 1

    #Scans each element on the low part and compares it to the pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            #if the element is smaller than pivot then it does some swaparoo magic
            array[i], array[j] = array[j], array[i]

    #Places our pivot in the correct spot after we are done using it
    array[i+1], array[high] = array[high], array[i+1]

    return i+1

def quicksort(array, low=0, high=None):
    #This just helps it to read the data
    if high is None:
        high = len(array) - 1

    #Calls partition to get a pivot and sort using the pivot
    #Then sorts the lower part of the list and higher part of the list separtly
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)


myList = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
quicksort(myList)
print("Quicksort:", myList) 

#Day 3 heap sort (Just shoving heap sort here instead of making a new file)