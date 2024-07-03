arr = [2,6,5,1,3,4]

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        currentMin = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[currentMin]:
                currentMin = j
        arr[i], arr[currentMin] = arr[currentMin], arr[i] # Swap the elements

selection_sort(arr)
print(arr)  # Output: [1, 2, 3, 4, 5, 6]
