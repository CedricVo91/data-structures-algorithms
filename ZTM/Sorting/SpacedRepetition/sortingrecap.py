###new recap of bubble sort -> the j and the pythonic parallel assignment when swapping! make note of this!


def bubble_sort_list(unsorted_list):
    n = len(unsorted_list)
    for j in range(n):
        # After j passes, the last j elements are already sorted
        for i in range(n - j - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                # Swap the elements
                ###more elegant way of swpping instead of creating a temporary variable!
                unsorted_list[i], unsorted_list[i + 1] = (
                    unsorted_list[i + 1],
                    unsorted_list[i],
                )
    return unsorted_list


# implement insertion sort


def selectionsort(array):
    for j in range(len(array) - 1):  # array = [1,2,3,4], i = 0,1,2,3
        min_index = j
        for i in range(
            j + 1, len(array)
        ):  # dont need an array minus 1 as range function uses all up to n-1 elements in a list
            if array[min_index] > array[i]:
                min_index = i
        # put minimum value of array in front i.e. on the iteration j.
        array[j], array[min_index] = array[min_index], array[j]

    return array


# print([x for x in range(1, 4)])

print(selectionsort([2, 6, 5, 1, 0]))


# implement Insertionsort
"""Working Backwards:

The key part of insertion sort is moving backwards through the sorted portion (from right to left). 
If the current element is smaller than the compared element, you shift the compared element one position to the right. 
Continue this process until you find the correct position for the current element.""" ""


def insertionsort(array):
    for j in range(1, len(array)):  # start at the second element and not the first
        current_element = array[j]  # 5
        indextoleft = j - 1  # 1
        # current element stays the same in each iteration and hence we can use it as a pointer sliding leftwards
        while (
            indextoleft >= 0 and current_element < array[indextoleft]
        ):  # compare the element to the prior number
            array[indextoleft + 1], array[indextoleft] = (
                array[indextoleft],
                array[indextoleft + 1],
            )
            indextoleft -= 1  # needed as we want to compare each of the elements left to the current element, not just one element!

    return array


print(insertionsort([2, 6, 5, 1, 0]))


# reread and redo the recursion one and memorize the pattern with how to index integers in python (modulus and //)
def fibonacci(n):
    # 0,1,1,2,3, 5
    if n < 2:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


# do another recursion simple exercise
# reverse a string


# implement merge sort

# implement quicksort

# bfs and dfs to learn recursion and backtracking
