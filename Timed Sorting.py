import time

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

tMax = [
    14.18, 13.82, 14.51, 15.3, 16.64, 18.99, 22.31, 23.71, 24.55, 22.65,
    21.88, 17.91, 14.98, 13.83, 14.21, 16.44, 17.22, 19.2, 22.29, 24.79,
    25.06, 22.27, 20.47, 16.98, 14.36, 14.37, 14.68, 17.41, 18.05, 19.61,
    20.88, 22.26, 24.31, 22.28, 19.49, 18.07, 14.6, 13.88, 14.35, 15.6,
    17.15, 18.83, 22.55, 24.06, 26.81, 23.58, 20.87, 18.07, 16.57, 16.08,
    15.53, 16.77, 18.88, 20.58, 22.81, 26.02, 25.56, 24.03, 20.69, 18.25,
    16.48, 15.09, 14.83, 16.71, 18.45, 20.25, 20.9, 23.35, 23.29, 22.7,
    20.29, 18.07, 15.58, 15.88, 15.44, 16.7, 17.99, 18.54, 22.93, 22.89,
    24.56, 23.42, 20.19, 17.98, 15.28, 13.88, 15.52, 16.72, 19.42, 20.06,
    22.28, 23.41, 23.83, 23.13, 19.86, 17.35, 16.36, 14.61, 14.89, 16.62,
    17.1, 18.14, 21.47, 23.11, 23.45, 22.61, 20.37, 18.3, 16.49, 13.97,
    15.21, 16.65, 17.42, 19.26, 22.15, 24.32, 22.68, 20.79, 19.18, 17.94,
    16.08, 13.96, 13.85, 15.76, 17.31, 19.89, 19.3, 23, 25.14, 23.84,
    20.78, 18.77, 15.13, 15.2, 15.91, 17.4, 18.54, 19.93, 22.94, 24.26,
    24.7, 22.8, 21.07, 17.49, 14.1, 14.36, 14.93, 16.99, 17.33, 19.36,
    19.11, 22.85, 24.04, 23.61, 19.9, 18.59, 15.36, 14.9, 15.39, 16.76,
    17.68, 19.26, 22.15, 25.15, 24.43, 23.65, 20.6, 16.62, 15.73, 14.55,
    14.55, 16.62, 17.37, 19.5, 22.19, 23.58, 24.65, 21.86, 20.08, 16.01,
    13.66, 13.96, 15.95, 17.04, 16.75, 18.72, 21.92, 23.69, 25.41, 23.28,
    20.9, 18.01, 15.4, 14.17, 15.4, 16.79, 17.89, 20.28, 23.53, 24.31,
    24.37, 23.03, 20.18, 18.89, 16.46, 14.86, 14.45, 16.12, 18.5, 19.31,
    21.53, 22.29, 23.64, 21.4, 21.06, 17.24, 15.47, 14.77, 16.36, 16.59,
    17.8, 18.89, 22.9, 24.4, 24.64, 24.35, 21.39, 17.83, 15.11, 14.9,
    16.09, 16.84, 18.42, 21.52, 22.46, 22.78, 24.67, 22.93, 21.9, 18.05,
    16.76, 14.34, 15.12, 16.84, 17.92, 18.93, 21.66, 25.36, 24.32, 24.43,
    20.98, 17.36, 15.51, 14.14, 15.04, 15.96, 17.58, 19.71, 21.72, 24.63,
    25.92, 23.78, 21.15, 19.94, 16.35, 15.17, 15.02, 16.76, 18.43, 19.53,
    21.71, 22.88, 24.51, 23.12, 21.26, 17.45, 15.71, 14.75, 16.23, 16.86,
    17.95, 20.8, 24.82, 26.05, 24.42, 23.98, 20.73, 18.37, 15.16, 15.22,
    15.62, 16.52, 18.25, 20.05, 22.25, 24.26
]

start_time = time.time()
print(selection_sort(tMax.copy()))
stop_time = time.time()

duration = stop_time - start_time
print(f"{duration * 1000:.3f} ms")

start_time = time.time()
print(merge_sort(tMax.copy()))
stop_time = time.time()

duration = stop_time - start_time
print(f"{duration * 1000:.3f} ms")

start_time = time.time()
print(quick_sort(tMax.copy()))
stop_time = time.time()

duration = stop_time - start_time
print(f"{duration * 1000:.3f} ms")

start_time = time.time()
print(heap_sort(tMax.copy()))
stop_time = time.time()

duration = stop_time - start_time
print(f"{duration * 1000:.3f} ms")