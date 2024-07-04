# declarions of variables
arr = []
start = 0
target = 2

#generate an array of numbers from 1 to 1024
for i in range(1, 1025):
    arr.append(i)
print(arr)

# set the end variable to the length of the array minus 1
end = len(arr) - 1

# define the binary search function
# this algorithm is a greate example of the O(log n) time complexity
def binary_Search(arr, start, end, target):
     mid_Index = (start + end) // 2
     if start > end:
         return 0
     if arr[mid_Index] == target:
         return 1
     if target < arr[mid_Index]:
            return binary_Search(arr, start, mid_Index - 1, target)
     else:
        if target > arr[mid_Index]:
            return binary_Search(arr, mid_Index + 1, end, target)




print(binary_Search(arr, start, end, target))
