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

selection_duration = stop_time - start_time
print(f"{selection_duration * 1000:.3f} ms")

start_time = time.time()
print(merge_sort(tMax.copy()))
stop_time = time.time()

merge_duration = stop_time - start_time
print(f"{merge_duration * 1000:.3f} ms")

start_time = time.time()
print(quick_sort(tMax.copy()))
stop_time = time.time()

quick_duration = stop_time - start_time
print(f"{quick_duration * 1000:.3f} ms")

start_time = time.time()
print(heap_sort(tMax.copy()))
stop_time = time.time()

heap_duration = stop_time - start_time
print(f"{heap_duration * 1000:.3f} ms")

print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")


Tmin = [
    7.6, 7.17, 7.47, 9.13, 10.42, 12.25, 14.95, 15.75, 16.57, 15.23,
    14.78, 10.85, 9.16, 7.89, 7.61, 8.96, 11.31, 11.94, 15.75, 16.2,
    17.31, 13.55, 13.87, 9.84, 7.1, 7.92, 8.58, 10.24, 11.4, 12.17,
    14.2, 14.89, 16.36, 15.24, 12.1, 11.48, 7.47, 6.4, 7.18, 9.18,
    11.04, 13.39, 14.52, 15.97, 18.29, 16.76, 13.82, 11.58, 10.1, 10.58,
    8.8, 10.5, 12.7, 13.06, 15.17, 18.04, 16.55, 16.83, 13.46, 11.11,
    7.77, 7.63, 7.25, 9.28, 11.67, 13.77, 14.19, 15.5, 16.4, 14.76,
    13.52, 11.83, 9.17, 10.15, 7.89, 9.43, 11.51, 11.58, 15.67, 15.18,
    17.36, 14.56, 13.03, 12.25, 7.09, 6.13, 8.34, 9.88, 12.96, 13.22,
    16.47, 15.46, 15.48, 15.69, 11.81, 11.88, 11.28, 7.73, 8.27, 9.84,
    9.79, 11.57, 14.72, 14.94, 15.47, 15.64, 12.63, 10.79, 9.93, 6.23,
    8.06, 10.49, 10.12, 12.57, 15.8, 16.65, 16.21, 13.11, 11.47, 11.05,
    9.43, 6.9, 7.19, 8.78, 11.5, 12.34, 12.68, 15.43, 17.58, 15.75,
    12.18, 11.71, 8.93, 9.16, 7.87, 10.34, 11.44, 12.7, 16.18, 16.21,
    16.55, 14.5, 14.14, 11.03, 6.27, 6.46, 8.07, 10.37, 11.36, 13.13,
    12.71, 16.01, 15.52, 15.78, 11.98, 11.75, 8.5, 8.12, 9.05, 9.75,
    10.9, 12.19, 15.3, 17.24, 16.42, 15.72, 13.49, 8.93, 9.19, 7.99,
    8.88, 9.57, 11.41, 12.94, 14.49, 15.85, 17.26, 14.46, 12.67, 8.48,
    6.39, 6.83, 9.82, 9.75, 10.15, 13.16, 14.67, 15.9, 17.77, 15.01,
    12.95, 10.8, 8.87, 7.11, 9.35, 10.36, 10.47, 13.11, 17.12, 16.96,
    17.89, 14.64, 12.79, 12, 10.53, 8, 6.96, 8.44, 11.99, 13.08, 15.14,
    15.67, 16.01, 14.05, 12.75, 9.56, 8.28, 7.49, 8.71, 9.86, 10.9,
    12.37, 16.1, 16.03, 15.72, 15.24, 14.12, 10.65, 9.14, 7.82, 9.25,
    10.3, 11.55, 13.51, 14.93, 15.23, 16.25, 13.95, 14.29, 9.93, 9.53,
    7.36, 8.55, 10.14, 11.29, 12.12, 14.95, 16.56, 16.14, 15.86, 13.19,
    10.33, 9.41, 7.33, 7.91, 9.51, 11.85, 12.47, 15.02, 17.21, 18.06,
    16.44, 13.67, 12.85, 9.35, 8.3, 7.75, 10.81, 11.86, 13.32, 14.14,
    15.63, 16.45, 16.48, 14.19, 10.2, 8.6, 7.8, 9.07, 10.78, 12.49,
    13.09, 16.07, 18.95, 17.97, 15.86, 13.68, 11.49, 8.12, 7.38, 8.47,
    9.65, 10.4, 12.7, 15.83, 17.43
]

start_time = time.time()
print(selection_sort(Tmin.copy()))
stop_time = time.time()

selection_duration = stop_time - start_time
print(f"{selection_duration * 1000:.3f} ms")

start_time = time.time()
print(merge_sort(Tmin.copy()))
stop_time = time.time()

merge_duration = stop_time - start_time
print(f"{merge_duration * 1000:.3f} ms")

start_time = time.time()
print(quick_sort(Tmin.copy()))
stop_time = time.time()

quick_duration = stop_time - start_time
print(f"{quick_duration * 1000:.3f} ms")

start_time = time.time()
print(heap_sort(Tmin.copy()))
stop_time = time.time()

heap_duration = stop_time - start_time
print(f"{heap_duration * 1000:.3f} ms")

print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")

Species = [
"Tok","Tok","GS","NIBr","NIBr","NIBr","Tok","Tok","Tok","Tok","Tok",
"NIBr","Tok","GS","NIBr","Tok","Tok","Tok","GS","GS","Tok","Tok",
"NIBr","Tok","GS","Tok","Tok","NIBr","GS","GS","GS","NIBr","NIBr",
"Tok","NIBr","NIBr","Tok","NIBr","GS","Tok","GS","Tok","NIBr","NIBr",
"NIBr","Tok","Tok","Tok","Tok","Tok","Tok","GS","NIBr","NIBr","Tok",
"Tok","GS","Tok","Tok","GS","Tok","NIBr","Tok","NIBr","Tok","NIBr",
"Tok","Tok","NIBr","GS","NIBr","Tok","NIBr","Tok","Tok","NIBr","GS",
"Tok","NIBr","Tok","Tok","NIBr","Tok","Tok","NIBr","NIBr","Tok","GS",
"NIBr","Tok","Tok","Tok","Tok","GS","Tok","Tok","Tok","Tok","NIBr",
"GS","NIBr","Tok","Tok","Tok","Tok","Tok","Tok","GS","NIBr","NIBr",
"NIBr","Tok","GS","NIBr","Tok","NIBr","Tok","NIBr","Tok","NIBr","NIBr",
"NIBr","Tok","GS","Tok","NIBr","GS","Tok","GS","NIBr","Tok","NIBr",
"Tok","NIBr","NIBr","Tok","GS","NIBr","Tok","NIBr","NIBr","GS","NIBr",
"NIBr","GS","Tok","GS","Tok","Tok","NIBr","GS","NIBr","NIBr","Tok",
"NIBr","Tok","NIBr","Tok","Tok","NIBr","NIBr","GS","Tok","GS","GS",
"NIBr","Tok","NIBr","NIBr","Tok","Tok","Tok","NIBr","NIBr","NIBr",
"GS","NIBr","NIBr","GS","Tok","NIBr","NIBr","NIBr","Tok","NIBr","NIBr",
"Tok","GS","NIBr","NIBr","Tok","Tok","NIBr","Tok","Tok","Tok","GS",
"Tok","GS","Tok","NIBr","NIBr","NIBr","Tok","NIBr","GS","NIBr","GS",
"Tok","GS","Tok","NIBr","Tok","Tok","Tok","NIBr","NIBr","Tok","NIBr",
"Tok","GS","Tok","NIBr","GS","NIBr","Tok","GS","NIBr","NIBr","Tok",
"Tok","GS","Tok","NIBr","Tok","Tok","NIBr","GS","NIBr","Tok","Tok",
"Tok","NIBr","Tok","GS","GS","Tok","Tok","NIBr","NIBr","NIBr","Tok",
"NIBr","Tok","NIBr","Tok","Tok","Tok","Tok","Tok","Tok","Tok","Tok",
"Tok","GS","NIBr","NIBr","GS","NIBr","NIBr","GS","NIBr","GS","GS",
"GS","NIBr","Tok","NIBr","GS","NIBr","NIBr","GS","NIBr","NIBr","Tok",
"GS","NIBr","GS","NIBr","Tok","NIBr","Tok","NIBr","Tok","NIBr","NIBr",
"NIBr","NIBr","NIBr","NIBr","NIBr","Tok","GS","NIBr","GS","NIBr",
"NIBr","NIBr","GS","NIBr","NIBr","Tok","GS","NIBr","GS","Tok","NIBr",
"Tok","NIBr","GS","NIBr","GS","Tok","Tok","Tok","GS","Tok","Tok","GS",
"GS","NIBr","Tok","GS","GS","Tok","NIBr","Tok","Tok","NIBr","NIBr",
"Tok","NIBr","NIBr","Tok","NIBr","Tok","Tok","NIBr","Tok","NIBr",
"Tok","NIBr","Tok","NIBr","Tok","Tok","NIBr","NIBr","Tok","NIBr","Tok",
"Tok","GS","Tok","Tok","Tok","NIBr","Tok","Tok","NIBr","Tok","NIBr",
"GS","Tok","NIBr","GS","GS","NIBr","Tok","GS","GS","GS","Tok","NIBr",
"GS","Tok","NIBr","GS","NIBr","GS","Tok","GS","NIBr","GS","GS","Tok",
"Tok","Tok","NIBr","NIBr","Tok","NIBr","NIBr","Tok","GS","NIBr","NIBr",
"Tok","NIBr","NIBr","NIBr","Tok","NIBr","Tok","Tok","GS","NIBr","NIBr",
"Tok","Tok","Tok","NIBr","NIBr","GS","GS","NIBr","GS","GS","NIBr",
"Tok","GS","NIBr","Tok","NIBr","Tok","NIBr","Tok","NIBr","Tok","NIBr",
"GS","GS","Tok","NIBr","Tok","NIBr","NIBr","Tok","NIBr","NIBr","GS",
"NIBr","NIBr","GS","GS","GS","NIBr","NIBr","NIBr","Tok","NIBr","NIBr",
"GS","NIBr","NIBr","NIBr","GS","Tok","GS","NIBr","GS","NIBr","NIBr",
"GS","GS","NIBr","GS","NIBr","NIBr","Tok","GS","NIBr","Tok","Tok",
"NIBr","GS"
]

start_time = time.time()
print(selection_sort(Species.copy()))
stop_time = time.time()

selection_duration = stop_time - start_time
print(f"{selection_duration * 1000:.3f} ms")

start_time = time.time()
print(merge_sort(Species.copy()))
stop_time = time.time()

merge_duration = stop_time - start_time
print(f"{merge_duration * 1000:.3f} ms")

start_time = time.time()
print(quick_sort(Species.copy()))
stop_time = time.time()

quick_duration = stop_time - start_time
print(f"{quick_duration * 1000:.3f} ms")

start_time = time.time()
print(heap_sort(Species.copy()))
stop_time = time.time()

heap_duration = stop_time - start_time
print(f"{heap_duration * 1000:.3f} ms")

print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")

Gender = [
"M","F","M","M","F","M","F","F","M","M","M","F","M","F","M","F",
"M","M","M","F","M","F","F","M","M","M","F","M","M","M","M","F",
"M","M","F","M","F","M","F","M","M","F","F","M","F","F","F","F",
"F","M","F","M","F","M","F","F","F","F","F","M","F","F","F","M",
"F","F","M","M","M","M","F","M","F","F","M","F","F","M","F","M",
"F","M","F","F","M","M","F","F","F","M","F","F","F","F","M","M",
"F","M","M","F","M","F","M","F","M","M","M","F","M","F","M","M",
"M","M","F","F","F","F","F","M","M","M","M","M","M","F","F","M",
"M","F","M","F","M","M","M","F","F","M","F","F","F","M","F","F",
"F","F","M","F","F","M","M","F","M","M","F","F","M","F","M","F",
"F","M","F","M","M","M","F","F","M","F","F","F","M","F","M","M",
"F","M","M","M","F","M","F","F","M","F","F","M","F","M","M","F",
"M","M","F","F","F","M","F","M","F","F","F","F","F","F","M","F",
"M","F","F","F","F","M","M","F","F","F","M","M","M","F","F","M",
"M","F","M","F","F","F","F","M","M","M","F","F","M","F","M","M",
"M","M","F","F","F","F","F","M","F","F","M","M","F","F","M","M",
"M","F","F","F","F","F","F","F","M","M","F","F","M","F","M","F",
"F","M","F","M","M","F","M","M","F","M","M","M","M","M","M","M",
"F","F","F","M","M","F","M","F","F","M","M","F","F","F","M","F",
"F","M","F","F","M","M","F","F","M","F","M","M","F","F","M","M",
"F","M","M","F","M","F","F","F","F","F","F","F","F","F","M","M",
"F","M","M","F","M","F","M","F","F","F","F","F","F","F","F","F",
"M","M","M","F","M","F","M","M","F","F","F","M","M","F","M","F",
"F","M","F","F","M","F","M","M","M","M","M","M","F","M","F","M",
"F","F","M","M","F","F","F","M","F","M","M","F","F","F","M","F",
"F","F","F","M","F","M","F","F","F","M","M","M","M","F","F","M",
"F","M","M","F","F","F","F","M","F","F","F","M","M","F","M","F",
"F","F","F","F","F","M","M","M","M","M","F","M","M","M","M","F",
"F","F","F","F","M","F","F","F","F","M","F","F","M","F","F","F",
"M","M","M","F","M","M","F","M","F","F","F","M","F","F","F","M",
"M","F","F","M","F","M","F","F","M","M","F","M","F","M","F","F",
"F","F","M","F","F","M","M","M","F","F","F","F","F","M","M","M",
"F","M","M","M","F","M","F","M","F","M","M","M","M","M","F","F",
"F","F","M","F","F","F","M","F","M","M","F","M","M","M","M","F",
"M","F","M","F","M","F","M","M","M","M","F","F","M","F","F","F",
"F","F","F","M","F","F","F","M","M","M","M","M","M","M","F","F",
"M","F","M","M","M","F","M","F","M","F","M","F","F","F","M","M",
"M","M","M","M","M","F","M","F","F","F","M","M","M","M","F","M",
"F","M","F","F","M","F","F","F","M","F","M","M","M","F","F","M",
"M","F","F","M","F","F","M","M","M","M","M","F","M","M","M","F",
"M","F","M","F","F","F","M","F","M","M","M","M","F","F","F","M",
"F","M","M","F","F","M","M","M","M","F","F","M","F","M","M","F",
"F","M","F","F","M","F","M","F","M","F","M","F","F","M","M","F",
"M","F","M","M","M","F","M","F","F","M","M","F"
]

start_time = time.time()
print(selection_sort(Gender.copy()))
stop_time = time.time()

selection_duration = stop_time - start_time
print(f"{selection_duration * 1000:.3f} ms")

start_time = time.time()
print(merge_sort(Gender.copy()))
stop_time = time.time()

merge_duration = stop_time - start_time
print(f"{merge_duration * 1000:.3f} ms")

start_time = time.time()
print(quick_sort(Gender.copy()))
stop_time = time.time()

quick_duration = stop_time - start_time
print(f"{quick_duration * 1000:.3f} ms")

start_time = time.time()
print(heap_sort(Gender.copy()))
stop_time = time.time()

heap_duration = stop_time - start_time
print(f"{heap_duration * 1000:.3f} ms")

print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")

Weight_kg = [
2.049,2.398,2.009,1.809,2.894,2.054,2.927,2.848,2.246,1.971,2.432,2.739,2.256,3.167,2.289,2.462,
2.044,1.951,2.455,3.719,2.586,1.644,2.994,2.5,2.331,2.21,3.101,2.204,2.289,2.633,2.675,2.47,2.253,
1.67,3.142,2.799,2.686,2.159,3.101,2.457,2.542,2.758,2.933,2.299,2.563,3.017,2.908,3.116,2.505,
2.125,2.33,2.141,3.138,2.297,2.713,2.662,3.668,3.453,2.48,2.612,3.445,2.302,2.461,2.168,3.397,
2.371,2.835,1.824,2.691,2.506,2.853,2.794,2.572,3.471,2.026,2.896,3.222,2.454,1.905,2.322,2.411,
1.679,2.817,2.549,2.206,2.418,2.914,3.822,3.27,2.258,3.294,2.745,2.643,3.313,2.057,2.393,2.389,
2.377,2.102,3.26,2.135,2.929,2.387,2.787,2.367,1.959,2.414,3.436,2.172,3.033,2.085,2.213,2.834,
1.61,2.89,2.612,2.702,3.128,2.536,2.702,2.239,2.186,2.363,2.922,2.01,3.096,2.923,2.003,2.159,
2.922,1.604,2.548,2.532,2.438,2.187,3.714,3.503,1.878,2.317,2.952,2.884,2.2,2.878,2.567,3.556,
3.484,2.249,2.747,2.424,1.882,2.884,3.176,2.673,1.825,2.341,2.328,2.162,2.74,2.205,2.516,3.02,
2.663,2.623,2.222,2.405,2.402,3.026,2.333,2.147,2.734,3.194,2.512,1.96,2.482,2.004,2.281,3.084,
2.157,2.175,1.862,2.552,2.253,2.991,2.795,1.947,2.695,2.693,1.663,2.573,2.414,1.834,3.128,1.652,
2.5,2.271,3.012,3.674,2.018,2.959,2.44,2.993,2.694,2.099,2.641,3.237,3.387,2.585,3.595,1.826,
3.143,2.717,2.239,3.21,1.591,2.13,3.007,2.418,3.074,2.117,2.274,2.021,3.021,2.773,2.188,1.95,
2.321,2.567,2.029,3.322,2.88,3.218,2.086,2.157,2.369,3.232,3.458,2.087,2.488,2.485,2.338,2.246,
2.045,2.615,2.767,2.722,2.89,2.431,2.396,3.022,2.716,1.886,1.965,2.844,3.06,2.399,2.612,1.831,
2.414,2.721,3.183,2.384,4.143,2.837,3.452,2.203,1.921,2.952,3.504,2.389,2.371,2.193,3.102,3.522,
2.526,2.753,2.198,2.079,3.58,2.364,1.88,3.05,2.429,2.006,2.889,2.274,2.081,2.449,2.573,2.339,3.155,
3.578,2.687,2.816,3.226,2.182,3.111,2.638,1.957,2.403,2.681,2.732,2.899,2.39,3.353,3.239,1.93,
2.748,3.291,2.256,2.044,3.454,3.105,2.204,2.841,2.041,2.276,2.912,3.139,2.475,2.604,2.395,2.313,
2.271,2.749,2.461,2.093,3.249,3.749,2.874,2.687,2.846,3.283,2.749,3.677,2.35,2.009,2.244,2.388,
2.285,3.381,2.429,2.603,2.312,3.002,3.518,3.079,2.301,2.653,2.834,2.723,2.904,2.842,2.033,1.916,
2.259,3.45,1.689,2.621,2.15,2.372,2.958,2.81,2.981,2.508,2.53,2.924,1.675,3.249,3.773,2.133,2.486,
3.063,2.486,4.008,2,2.497,1.921,2.353,1.987,2.339,2.735,2.225,3.127,2.353,2.817,2.384,2.195,1.822,
2.264,3.491,2.705,2.455,2.579,1.796,2.469,2.691,3.522,3.294,2.384,2.465,3.119,3.213,3.591,2.404,
2.857,2.014,3.163,3.573,2.662,2.008,2.22,1.836,2.287,2.841,3.309,2.257,3.156,2.596,2.772,2.647,
2.441,2.59,3.314,2.186,2.898,2.751,2.992,2.905,2.426,3.332,2.548,2.502,2.915,3.134,3.386,2.874,
2.716,2.349,2.251,2.148,2.337,2.796,3.35,2.869,2.229,2.165,1.928,2.535,2.421,2.905,2.517,3.206,
2.246,2.563,2.659,3.115,2.549,2.243,3.94,2.878,2.266,2.471,3.267,3.391,2.232,2.65,2.245,3.306,
2.674,2.059,2.435,2.064,2.124,2.54,2.768,1.959,3.392,3.089,3.497,2.014,2.065,3.854,2.993,2.133,
3.446,2.631,3.274,2.929,2.101,2.368,2.292,2.254,3.481,1.916,2.541,2.994,2.45,3.656,2.294,3.29,
3.142,2.028,2.191,2.173,2.871,2.522,2.221,2.629,2.665,2.017,1.718,2.16,2.708,2.62,2.559,2.312,
3.136,2.103,3.504,2.096,2.757,2.557,2.768,2.095,2.303,2.298,3.374,2.602,2.909,2.936,2.291,2.696,
2.468,3.186,1.758,3.311,2.417,2.004,2.142,2.587,2.073,2.39,2.699,3.335,2.716,2.528,2.19,2.96,
2.201,2.421,1.948,1.979,2.435,1.97,2.797,2.538,2.868,2.849,3.045,2.755,3.317,3.005,3.347,2.511,
2.975,3.187,3.416,2.195,2.159,2.331,2.361,2.195,2.687,2.29,2.66,2.405,2.842,2.982,2.155,1.689,
2.016,3.226,2.312,3.046,2.425,2.863,2.468,2.915,2.702,3.417,2.24,2.469,2.29,2.216,2.806,2.41,
2.122,3.206,2.109,3.234,3.16,3.074,2.363,2.093,2.488,2.857,3.147,2.084,2.992,2.304,3.111,2.604,
2.312,2.486,3.029,2.958,2.093,2.986,1.999,2.34,2.508,3.185,2.596,2.092,2.598,2.176,2.501,1.923,
3.298,2.898,2.485,2.171,2.297,2.159,2.177,2.317,2.076,2.271,1.984,2.25,2.61,3.266,2.152,2.544,
3.448,2.967,2.237,3.272,2.46,2.282,2.103,1.884,2.94,2.654,2.797,2.022,3.02,2.247,1.57,2.573,2.72,
2.151,2.095,2.033,2.494,3.114,2.661,2.05,3.413,2.489,1.824,2.722,2.79,2.335,2.179,3.07,2.297,
2.68,2.638,2.784,2.653,2.625,2.177,2.575,3.937,1.996,2.444,3.519,2.424,2.818,2.011,2.393,2.156,
3.19,2.436,2.309,2.414,2.49,2.953,3.695
]
start_time = time.time()
print(selection_sort(Weight_kg.copy()))
stop_time = time.time()

selection_duration = stop_time - start_time
print(f"{selection_duration * 1000:.3f} ms")

start_time = time.time()
print(merge_sort(Weight_kg.copy()))
stop_time = time.time()

merge_duration = stop_time - start_time
print(f"{merge_duration * 1000:.3f} ms")

start_time = time.time()
print(quick_sort(Weight_kg.copy()))
stop_time = time.time()

quick_duration = stop_time - start_time
print(f"{quick_duration * 1000:.3f} ms")

start_time = time.time()
print(heap_sort(Weight_kg.copy()))
stop_time = time.time()

heap_duration = stop_time - start_time
print(f"{heap_duration * 1000:.3f} ms")

print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")

Height_cm = [
36.5,40.3,42.9,36.1,41.4,38.1,41.8,41.7,38.4,37.2,37.1,39.1,37.3,47.8,37.5,39.1,35.4,37.5,45.9,46.8,
37.2,39.8,42.5,38.2,46.3,35,40.8,37.8,44.4,46.7,47,39,36.1,38.3,38.2,38.4,38.8,38.3,45,36.5,46.4,
39.6,38.6,35.5,39.3,37.6,40.4,39.1,38.1,37.2,40.5,45.9,41,38.9,41.4,37.5,48.3,41.5,39.4,45.7,38.8,
38.2,37.3,36.7,40.8,42.3,34.9,37.9,36.3,48,42.8,36.3,40.2,40.2,38.4,39.4,47.9,37.2,39.7,38,40.5,
36.6,39.3,41.2,36,36,41.6,48.5,39,36.6,41.6,42.1,38.8,48,36.8,37.5,41.2,36.5,35.9,48.5,36.2,41.2,
36.8,40,37.2,38.5,35.6,46.8,37.4,40.5,35.7,37.2,43.9,37.2,39.5,38.8,40.8,37.5,42.5,36.2,35.7,37.4,
36.6,44.1,37.9,37.3,47.1,36.5,44.8,40.5,35.7,40.1,36.5,38.9,37.2,42,50.4,38.4,39.8,41.1,40.5,45.7,
41.1,38.6,46.3,39.6,45.3,40.7,40.3,37.9,46,41.3,36.9,37.3,41.1,40.7,36.6,39.7,36.8,40.3,42.7,45,
37.6,43.6,42.7,36.4,42.1,39.9,37.6,41.8,40.8,39.1,37.5,41,35.1,45.2,38.7,36.3,44.4,36.6,42.4,37.2,
38.9,37.7,35.8,39.6,41.2,45.4,37.3,36.9,38.8,39.7,35.9,37.4,41.4,38.5,47.5,36.8,46.9,37.7,41.5,40.5,
39.1,40.7,40.8,45.3,37.8,49.9,36.6,51.7,41.5,42,37.6,36.8,46.1,45.9,38,41,45.1,36.1,37.3,41.2,40.3,
36.2,36.2,39.1,36.5,40,46.3,39.9,49.6,37.1,36.7,37.6,46.9,47.6,36.5,40.3,35.9,37.6,45,45.8,41.2,
37.1,37.5,38.9,40.6,37.1,40.5,40.6,38.3,36.6,39.5,39.1,36.9,46.4,45.3,39.6,40.7,49.7,38,47.4,39.7,
47.9,37,35.7,46.6,48.9,35.9,41,38.8,50.5,40.3,44.7,39.3,37.6,38.6,47,36.7,36.2,40.6,35.3,47.6,45.5,
37.8,35.4,37.6,45.7,40.2,38.8,45.5,46.9,45,48.4,35.3,38.2,39.8,38,37.3,38.5,42.2,41.6,37.4,39.4,
44.6,38,39.9,48,45.5,38,42.9,40.3,37.7,40.2,45.9,45.9,47.9,41.2,37.2,35.8,40.3,45.4,36.4,37.2,
36.5,40,49,50.6,38.5,39.3,42.1,45.3,39.6,48.8,46.6,45.2,37.8,35.1,36.9,48.7,37.5,39.5,37.8,39.1,
48.4,37.9,40.1,40.7,40.2,40.6,48.1,41.5,36.9,46.8,44.9,45.9,36.9,39.9,38.5,36.7,41.2,42.1,39.4,
36.4,36.6,39.2,35.3,41.9,48.6,36.9,39.2,39.6,46.6,49.5,38.1,44.9,37,37.6,36.6,37.8,39.3,36.7,39.2,
45.9,38.6,38.7,37.2,37.6,40.6,41.3,40.6,37,41,36.3,35.3,37.7,37.8,40,44.9,38.3,41.3,48.5,46.9,
36.4,39.4,37.6,47.3,47.4,41.2,44.5,45.6,37.1,36.6,40.9,40.9,39,38.7,38.4,46.2,40.5,41.3,41.2,
50,36.3,51.2,38.9,37.8,36.2,35.6,40,36.8,41.1,40.5,38.7,49.2,38.7,40,47.1,37.4,37.1,46.3,38.1,
40,37.7,37.4,44.2,37,38.8,40.8,41.4,42.2,50.6,38.4,37.4,39.5,40,39.9,37.2,49.6,48.8,38.6,41.5,
38.1,41.1,36.5,35.3,37.5,41.9,39.2,36.8,40.3,37.1,40.2,41.4,38.6,38.5,42.1,36.9,46.4,36.3,35.9,
45.8,39.1,36.1,51,35.4,51.2,45.2,45.3,35.8,39.8,36.3,48.3,35.5,38.5,48.6,40.1,41.1,37,45.9,40,
45.6,37,35.8,39.9,41.6,42.8,39.7,38.7,36.5,37.3,36.1,40.2,36,37.1,36.3,51.1,35.2,49.5,39.4,39.3,
35.7,43.5,36.8,37.9,37.7,48.2,39.8,50.3,40,35.8,38.5,39,47.2,36.3,46.9,36.9,37.2,40.1,46.4,38.3,
36.3,44.7,51.5,36.8,41.7,47.4,49.8,36.2,39.3,37.7,37.7,36.9,36.9,39.7,41.5,37.4,41.5,39.6,41.4,
39.3,39,39.4,37.6,38.7,42.2,39.2,36.4,37.5,37.2,39.5,36.3,36.6,36.6,40.4,40.4,45.6,40.8,35.3,
36.4,36.2,38.4,36.8,39.4,36.8,39.5,45.1,41.2,41.9,49.4,43.8,37.5,36.9,44.3,42.5,44.6,37.9,40.8,
45.4,37.6,42.4,49.8,37.5,44.3,36.2,43.7,39.9,45.8,46.4,38.2,40,41.2,36.5,42.2,38.7,40.3,35.1,
40.1,44,37.5,36.7,40.6,40.5,37.6,37.7,38.1,40.1,38.3,41,45.9,37.4,37.5,38.2,38.1,36.6,38,37.8,
45.8,43.7,41.5,46.1,46.4,37.1,40.8,48.5,37.3,36.2,39.8,37.9,37.3,37.4,39.1,42.1,37.9,50.2,44.3,
40.5,38.7,37.8,39.6,39.8,36.2,38.5,37.5,44.6,39.9,40.8,44.1,49.1,45.2,36.9,39.4,39.1,37,41.6,
41.3,44.6,38.1,38.3,43.1,45.6,40.5,46.5,39.2,47.6,37,36.6,45.9,44.5,38.6,45.5,35.3,38.1,39.9,46,
39.5,41.2,36.1,34.9,44.2
]

start_time = time.time()
print(selection_sort(Height_cm.copy()))
stop_time = time.time()

selection_duration = stop_time - start_time
print(f"{selection_duration * 1000:.3f} ms")

start_time = time.time()
print(merge_sort(Height_cm.copy()))
stop_time = time.time()

merge_duration = stop_time - start_time
print(f"{merge_duration * 1000:.3f} ms")

start_time = time.time()
print(quick_sort(Height_cm.copy()))
stop_time = time.time()

quick_duration = stop_time - start_time
print(f"{quick_duration * 1000:.3f} ms")

start_time = time.time()
print(heap_sort(Height_cm.copy()))
stop_time = time.time()

heap_duration = stop_time - start_time
print(f"{heap_duration * 1000:.3f} ms")

print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")

Location = [
"StI","SF","NWN","E","W","E","NF","NF","StI","StI","NF","W","SF","NWN","W","StI","StI","StI","CW",
"NWN","NF","SF","W","StI","EC","StI","NF","W","EC","EC","EC","N","W","StI","E","W","StI","N","NWN",
"NF","EC","NF","N","W","W","StI","StI","StI","StI","StI","SF","NWN","E","N","StI","SF","EC","NF",
"StI","CW","StI","W","StI","N","NF","N","StI","NF","W","CW","N","NF","W","NF","SF","W","EC","StI",
"E","StI","StI","N","StI","NF","N","E","StI","NWN","E","StI","StI","StI","StI","EC","StI","StI","StI",
"StI","W","CW","W","StI","StI","SF","StI","NF","NF","CW","N","W","W","StI","EC","N","NF","N","StI",
"E","NF","E","E","W","StI","EC","StI","N","CW","StI","EC","N","NF","N","StI","N","N","StI","NWN",
"E","SF","N","E","EC","E","E","EC","NF","EC","StI","SF","E","EC","W","W","NF","N","NF","E","StI",
"NF","N","N","EC","NF","EC","NWN","E","StI","E","W","StI","StI","StI","E","E","E","EC","N","W","NWN",
"StI","E","W","E","NF","N","W","StI","EC","E","E","StI","NF","E","SF","NF","NF","NWN","StI","EC",
"SF","N","W","N","StI","E","NWN","N","EC","NF","EC","StI","N","E","SF","NWN","EC","StI","W","NWN",
"E","NF","W","StI","N","NF","StI","N","NF","EC","E","CW","E","StI","NF","NWN","CW","E","E","StI",
"NF","CW","EC","NF","NF","E","StI","E","N","N","NF","SF","StI","E","E","NF","CW","EC","StI","StI",
"EC","StI","NWN","StI","NWN","NF","E","CW","NWN","W","W","N","EC","SF","EC","NF","StI","W","NWN",
"E","StI","N","W","CW","NWN","E","NF","N","CW","NF","NF","NWN","NWN","EC","CW","W","StI","SF","StI",
"W","NF","E","StI","StI","W","EC","W","StI","EC","NWN","N","StI","StI","NF","StI","EC","EC","CW",
"W","N","N","N","EC","E","SF","E","NF","CW","NWN","W","NF","SF","NWN","E","CW","CW","CW","E","W",
"E","CW","W","N","StI","W","CW","E","W","E","E","W","NWN","E","NF","NWN","EC","EC","W","StI","NF",
"StI","N","N","NF","StI","NF","W","NF","N","NWN","E","W","StI","CW","NWN","W","CW","W","StI","SF",
"E","W","E","W","CW","W","SF","E","N","NF","StI","StI","W","W","StI","StI","N","E","StI","EC","E",
"NF","EC","NWN","StI","NF","StI","NWN","CW","N","EC","EC","StI","W","StI","W","N","W","SF","NWN",
"E","SF","W","EC","SF","CW","E","StI","SF","StI","N","N","StI","E","NF","CW","StI","N","EC","W",
"StI","CW","E","W","StI","StI","EC","StI","E","StI","SF","N","NWN","W","NF","StI","StI","N","StI",
"EC","EC","NF","StI","N","W","N","StI","W","SF","N","SF","NF","SF","StI","StI","SF","NF","SF","SF",
"CW","E","E","EC","W","W","CW","N","EC","CW","NWN","N","StI","E","EC","W","E","NWN","W","W","StI",
"EC","E","NWN","W","StI","E","StI","E","StI","N","N","N","E","N","N","W","NF","NWN","E","NWN","N",
"N","E","EC","W","N","StI","CW","E","CW","StI","E","StI","W","EC","E","EC","StI","StI","StI","EC",
"SF","StI","EC","CW","N","NF","CW","CW","StI","E","NF","NF","N","W","SF","E","E","NF","N","StI",
"StI","N","NF","N","StI","N","StI","E","SF","SF","E","W","StI","N","StI","NF","CW","SF","StI","StI",
"W","SF","NF","N","NF","E","CW","NF","E","NWN","NWN","W","StI","CW","CW","EC","StI","N","CW","StI",
"N","CW","N","NWN","NF","EC","W","CW","NWN","StI","StI","NF","E","E","StI","N","N","StI","EC","W",
"E","NF","E","N","W","NF","E","StI","StI","EC","N","W","StI","StI","StI","E","W","CW","NWN","E",
"NWN","CW","E","StI","EC","N","StI","N","StI","N","StI","N","StI","W","CW","EC","StI","W","NF","N",
"N","SF","W","W","NWN","N","W","CW","NWN","CW","W","E","E","StI","W","W","EC","N","N","N","EC","SF",
"NWN","W","EC","W","W","CW","EC","N","NWN","E","W","StI","CW","E","StI","NF","W","CW"
]

start_time = time.time()
print(selection_sort(Location.copy()))
stop_time = time.time()

selection_duration = stop_time - start_time
print(f"{selection_duration * 1000:.3f} ms")

start_time = time.time()
print(merge_sort(Location.copy()))
stop_time = time.time()

merge_duration = stop_time - start_time
print(f"{merge_duration * 1000:.3f} ms")

start_time = time.time()
print(quick_sort(Location.copy()))
stop_time = time.time()

quick_duration = stop_time - start_time
print(f"{quick_duration * 1000:.3f} ms")

start_time = time.time()
print(heap_sort(Location.copy()))
stop_time = time.time()

heap_duration = stop_time - start_time
print(f"{heap_duration * 1000:.3f} ms")

print(f"Selection Sort: {selection_duration * 1000:.3f} ms")
print(f"Merge Sort: {merge_duration * 1000:.3f} ms")
print(f"Qucik Sort: {quick_duration * 1000:.3f} ms")
print(f"Heap Sort: {heap_duration * 1000:.3f} ms")