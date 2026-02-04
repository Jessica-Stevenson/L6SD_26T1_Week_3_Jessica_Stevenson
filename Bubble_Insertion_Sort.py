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

print("Bubble 1")

start_time = time.time()
sorted_list = Bubble_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("Insertion 1")

start_time = time.time()
sorted_list = Insertion_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("-")

mylist = [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

print("Bubble 2")

start_time = time.time()
sorted_list = Bubble_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("Insertion 2")

start_time = time.time()
sorted_list = Insertion_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("-")

mylist = [456, 234, 765, 321, 908, 567, 876, 345, 654, 432,
789, 123, 890, 567, 876, 345, 654, 321, 908, 765,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

print("Bubble 3")

start_time = time.time()
sorted_list = Bubble_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("Insertion 3")

start_time = time.time()
sorted_list = Insertion_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("-")

mylist = [654, 321, 908, 765, 432, 789, 123, 890, 567, 876,
345, 654, 321, 908, 765, 432, 789, 123, 890, 567,
876, 345, 654, 321, 908, 765, 432, 789, 123, 890,
567, 876, 345, 654, 321, 908, 765, 432, 789, 123,
890, 567, 876, 345, 654, 321, 908, 765, 432, 789]

print("Bubble 4")

start_time = time.time()
sorted_list = Bubble_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("Insertion 4")

start_time = time.time()
sorted_list = Insertion_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("-")

mylist = [432, 765, 123, 908, 234, 567, 876, 345, 654, 321,
789, 876, 345, 654, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654,
321, 908, 765, 432, 789, 123, 890, 567, 876, 345,
654, 321, 908, 765, 432, 789, 123, 890, 567, 876,
345, 654, 321, 908, 765, 432, 789, 123, 890, 567,
876, 345, 654, 321, 908, 765, 432, 789, 123, 890,
567, 876, 345, 654, 321, 908, 765, 432, 789, 123,
890, 567, 876, 345, 654, 321, 908, 765, 432, 789,
123, 890, 567, 876, 345, 654, 321, 908, 765, 432,
789, 123, 890, 567, 876, 345, 654, 321, 908, 765,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654,
321, 908, 765, 432, 789, 123, 890, 567, 876, 345,
654, 321, 908, 765, 432, 789, 123, 890, 567, 876,
345, 654, 321, 908, 765, 432, 789, 123, 890, 567]

print("Bubble 5")

start_time = time.time()
sorted_list = Bubble_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("Insertion 5")

start_time = time.time()
sorted_list = Insertion_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("-")

mylist = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "mango", "peach", "pear", "watermelon",
"strawberry", "blueberry", "raspberry", "blackberry", "lemon", "lime", "cherry", "plum", "apricot", "fig",
"grapefruit", "pomegranate", "avocado", "papaya", "coconut", "passionfruit", "guava", "lychee", "dragonfruit",
"persimmon", "raspberry", "blackberry", "strawberry", "cranberry", "blueberry", "elderberry", "gooseberry",
"boysenberry", "currant", "huckleberry", "blackcurrant", "lingonberry", "mulberry", "raspberry", "sloeberry",
"marionberry", "tayberry", "loganberry"]

print("Bubble 6")

start_time = time.time()
sorted_list = Bubble_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")

print("Insertion 6")

start_time = time.time()
sorted_list = Insertion_Sort(mylist.copy())
stop_time = time.time()

duration = stop_time - start_time

print(sorted_list)
print(f"{duration * 1000:.3f} ms")
