

def swap(lst, i, j):

    lst[i], lst[j] = lst[j], lst[i]


def sift_down(lst, i, upper):
    while (True):

        l, r = i*2+1 , i*2+2  # left and right child

        if max(l,r) < upper:  # if both children exist, upper is the last index

            if lst[i] >= max(lst[l], lst[r]): break
            elif lst[l] > lst[r]:  # if left child is greater than right child
                swap(lst, i, l)  # swap parent with left child
                i = l  # move to left child

            else:
                swap(lst, i, r) # swap parent with right child
                i = r # move to right child

        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, i, l)
                i = l

            else:
                break

        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst, i, r)
                i = r

            else:
                break
        else:
            break

def heapsrot(lst):
    for j in range((len(lst) -2)//2 , -1, -1):
        sift_down(lst, j, len(lst))

    for end in range(len(lst) -1, 0, -1):
        swap(lst, 0, end)
        sift_down(lst, 0, end)

lst = [i for i in range(100, 1, -1)]
heapsrot(lst)
print(lst)

# the heap algorithm works like this:
# 1. create a heap from the list
# 2. swap the first element with the last element
# 3. sift down the first element to the correct position
# 4. repeat step 2 and 3 until the list is sorted
# 5. the list is sorted in ascending order
# 6. the time complexity of the heap sort is O(nlogn)
# 7. the space complexity of the heap sort is O(1)
# 8. the heap sort is not stable
# 9. the heap sort is not adaptive
# 10. the heap sort is not an in-place sorting algorithm
