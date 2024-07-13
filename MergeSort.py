arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 8]

def merge_Sort(arr):

    if len(arr) > 1:
        left_arr = arr[:len(arr)//2] # from the beginning to the middle of the array
        right_arr = arr[len(arr)//2:] # from the middle to the end of the array

        print(left_arr)
        # recursion
        # divide O(log n)
        merge_Sort(left_arr)
        merge_Sort(right_arr)


        # merge O(n) 
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

merge_Sort(arr)
print(arr)