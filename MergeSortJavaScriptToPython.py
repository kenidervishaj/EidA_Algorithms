arr = [4,9,12,100,32,9,6,120,11]

# O(n log n) time complexity
def merge_Sort(arr):

    if len(arr) < 2:
        return arr

    # O(log n) time complexity, because we are dividing the array in half recursively
    mid = len(arr) // 2 # find the middle of the array
    left = merge_Sort(arr[:mid]) # left array
    right = merge_Sort(arr[mid:]) # right array

    return merge(merge_Sort(left), merge_Sort(right)) # merge the left and right arrays

def merge(left, right):
    # O(n) time complexity, because we are iterating through the left and right arrays once to merge them together in sorted order
    result = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

print(merge_Sort(arr))