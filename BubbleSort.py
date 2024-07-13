list1 = [5, 3, 8, 6, 7, 2]

print("Original List: ", list1)

def bubbleSort(list1):
    for i in range(len(list1) - 1):  # this loop is for number of passes
        for j in range (len(list1) - 1):  # this loop is for number of comparisons
            if list1[j] > list1[j+1]:  # if the current element is greater than the next element, then swap
                list1[j], list1[j+1] = list1[j+1], list1[j] # swapping the elements
                print(list1)
    return list1  # return the sorted list

print("Sorted List: ", bubbleSort(list1))  # calling the function and printing the sorted list

# this algorithem has the big O notation of O(n^2)