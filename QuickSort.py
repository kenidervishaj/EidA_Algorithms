arr = [22, 11, 88, 66, 55, 77, 33, 44]

# def quick_Sort(arr):
#     pivot_index = len(arr) - 1
#     i = arr[0]
#     j = arr[len(arr) - 2]
#     for i in range(len(arr)):
#         if arr[i] < arr[pivot_index]:
#             for j in range(len(arr)):
#                 if arr[j] > arr[pivot_index]:
#                     arr[i], arr[j] = arr[j], arr[i]
#                     break
#
#
#
#

def quick_Sort(arr, left, right):
    if left < right:
        partition_index = partition(arr, left, right)
        quick_Sort(arr, left, partition_index - 1)
        quick_Sort(arr, partition_index + 1, right)

def partition(arr, left, right):
    i = left # i is the index of the element that is greater than the pivot
    j = right - 1 # j is the index of the element that is less than the pivot
    pivot = arr[right] # pivot is the last element in the array

    while i < j: # while i is less than j
        while i < right and arr[i] < pivot: # i < right is important
            i += 1  # i is the index of the element that is greater than the pivot
        while j > left and arr[j] > pivot: # j > left is important
            j -= 1  # j is the index of the element that is less than the pivot
        if i < j:  # if i is less than j, swap the elements
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot: # if the element at index i is greater than the pivot, swap it with the pivot
        arr[i], arr[right] = arr[right], arr[i]

    return i # return the index of the pivot

quick_Sort(arr, 0, len(arr) - 1) # call the quick_Sort function
print(arr) # print the sorted array