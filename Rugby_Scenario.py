import time
import pandas as pd

#Stop it from breaking from too much data
import sys
sys.setrecursionlimit(10000)

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

#Selection Sort
def selection_sort(myList):
    l = len(myList)
    for i in range(l-1):
        min_index = i
        for j in range(i+1, l):
            if myList[j] < myList[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        myList[i], myList[min_index] = myList[min_index], myList[i]
    return myList

#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#Quick Sort
def quick_sort(arr):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i + 1

    def quicksort_helper(array, low, high):
        if low < high:
            pivot_index = partition(array, low, high)
            quicksort_helper(array, low, pivot_index-1)
            quicksort_helper(array, pivot_index+1, high)

    quicksort_helper(arr, 0, len(arr) - 1)
    return arr

#Heap Sort
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


#Load Excel file
df = pd.read_excel("rugby_players_data-1.xlsx")

Name = "Name"
data_list = df[Name].tolist()

print("Name Sorting")

start_time = time.time()
Bubble_Sort(data_list.copy())
stop_time = time.time()
bubble_duration = stop_time - start_time

start_time = time.time()
Insertion_Sort(data_list.copy())
stop_time = time.time()
insertion_duration = stop_time - start_time

start_time = time.time()
selection_sort(data_list.copy())
stop_time = time.time()

selection_duration = stop_time - start_time

start_time = time.time()
merge_sort(data_list.copy())
stop_time = time.time()

merge_duration = stop_time - start_time

start_time = time.time()
quick_sort(data_list.copy())
stop_time = time.time()

quick_duration = stop_time - start_time

start_time = time.time()
heap_sort(data_list.copy())
stop_time = time.time()

heap_duration = stop_time - start_time

print(f"Bubble Sort: {bubble_duration * 1000:.3f} ms")
print(f"Insertion Sort: {insertion_duration * 1000:.3f} ms")
print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")

Age = "Age"
data_list = df[Age].tolist()

print("Age Sorting")

start_time = time.time()
Bubble_Sort(data_list.copy())
stop_time = time.time()
bubble_duration = stop_time - start_time

start_time = time.time()
Insertion_Sort(data_list.copy())
stop_time = time.time()
insertion_duration = stop_time - start_time

start_time = time.time()
selection_sort(data_list.copy())
stop_time = time.time()

selection_duration = stop_time - start_time

start_time = time.time()
merge_sort(data_list.copy())
stop_time = time.time()

merge_duration = stop_time - start_time

start_time = time.time()
quick_sort(data_list.copy())
stop_time = time.time()

quick_duration = stop_time - start_time

start_time = time.time()
heap_sort(data_list.copy())
stop_time = time.time()

heap_duration = stop_time - start_time

print(f"Bubble Sort: {bubble_duration * 1000:.3f} ms")
print(f"Insertion Sort: {insertion_duration * 1000:.3f} ms")
print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")

Height = "Height"
data_list = df[Height].tolist()

print("Height Sorting")

start_time = time.time()
Bubble_Sort(data_list.copy())
stop_time = time.time()
bubble_duration = stop_time - start_time

start_time = time.time()
Insertion_Sort(data_list.copy())
stop_time = time.time()
insertion_duration = stop_time - start_time

start_time = time.time()
selection_sort(data_list.copy())
stop_time = time.time()

selection_duration = stop_time - start_time

start_time = time.time()
merge_sort(data_list.copy())
stop_time = time.time()

merge_duration = stop_time - start_time

start_time = time.time()
quick_sort(data_list.copy())
stop_time = time.time()

quick_duration = stop_time - start_time

start_time = time.time()
heap_sort(data_list.copy())
stop_time = time.time()

heap_duration = stop_time - start_time

print(f"Bubble Sort: {bubble_duration * 1000:.3f} ms")
print(f"Insertion Sort: {insertion_duration * 1000:.3f} ms")
print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")

Gender = "Gender"
data_list = df[Gender].tolist()

print("Gender Sorting")

start_time = time.time()
Bubble_Sort(data_list.copy())
stop_time = time.time()
bubble_duration = stop_time - start_time

start_time = time.time()
Insertion_Sort(data_list.copy())
stop_time = time.time()
insertion_duration = stop_time - start_time

start_time = time.time()
selection_sort(data_list.copy())
stop_time = time.time()

selection_duration = stop_time - start_time

start_time = time.time()
merge_sort(data_list.copy())
stop_time = time.time()

merge_duration = stop_time - start_time

start_time = time.time()
quick_sort(data_list.copy())
stop_time = time.time()

quick_duration = stop_time - start_time

start_time = time.time()
heap_sort(data_list.copy())
stop_time = time.time()

heap_duration = stop_time - start_time

print(f"Bubble Sort: {bubble_duration * 1000:.3f} ms")
print(f"Insertion Sort: {insertion_duration * 1000:.3f} ms")
print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")