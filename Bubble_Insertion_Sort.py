import time

#Bubble Sort
def Bubble_Sort(mylist):
    n = len(mylist)
    for i in range(n-1):
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist


#Insertion Sort
def Insertion_Sort(mylist):
    n = len(mylist)
    for i in range(1,n):
        insert_index = i
        current_value = mylist.pop(i)
        for j in range(i-1, -1, -1):
            if mylist[j] > current_value:
                insert_index = j
    mylist.insert(insert_index, current_value)
    return mylist

#Main

mylist = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]

start_time = time.time()
Bubble_Sort(mylist)
stop_time = time.time()

start_time = time.time()
Insertion_Sort(mylist)
stop_time = time.time()