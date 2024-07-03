arr = [30, 15, 12, 50, 90, -2]

def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from 1 because we assume that the first element is already sorted
        j = i
        while arr[j - 1] > arr[j] and j > 0:  # Compare the current element with the element to the left of it
            arr[j - 1], arr[j] = arr[j], arr[j - 1]  # Swap the elements, arr[j-1] is the element to the left of arr[j]
            j -= 1 # Move to the left


insertion_sort(arr)
print(arr)  # Output: [1, 2, 3, 4, 5, 6]