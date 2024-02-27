def insertionsort(array):
    n = len(array)
    for i in range(n):
        sub_array = array[:i]
        # sort the subarray
        for j in range(len(sub_array)):
            if sub_array[j] > sub_array[j + 1]:
                sub_array[j + 1], sub_array[j] = sub_array[j], sub_array[j + 1]


def test_subarray_sort(sub_array):
    smallest_index = 0
    for j in range(len(sub_array) - 1):  # 0,1,
        if sub_array[j] < sub_array[smallest_index]:
            smallest_index = j
            sub_array[smallest_index], sub_array[j] = (
                sub_array[j],
                sub_array[smallest_index],
            )

    return sub_array


print(test_subarray_sort([5, 6, 3]))


##guided solution as insertion sort above did not yield results


def insertionsort(array):
    n = len(array)
    for i in range(
        1, n
    ):  # for each entry in the array,but start with the second entry as the subarray at index 0 is considered sorted in this algorithm
        # The current element to be inserted into the sorted portion of the array
        current_element = array[i]
        j = i - 1  # compare the number at index i to the left
        while j >= 0 and array[j] > current_element:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_element
    return array


print(insertionsort([5, 6, 3]))


"""Sorting the Sub-array:

The inner loop should start at the current element (i) and work backwards (to the left) towards the start of the array.
Compare the current element with each element to its left and swap them if the current element is smaller.
Working Backwards:

The key part of insertion sort is moving backwards through the sorted portion (from right to left). If the current element is smaller than the 
compared element, you shift the compared element one position to the right. Continue this process until you find the correct position for the current element."""


"""
Certainly! Let's walk through each step of the insertion_sort function when sorting the array [5, 6, 3]. This will help illustrate how the algorithm processes each number:

Initial Array: [5, 6, 3]
First Iteration (i = 1):
Current Element: current_element = array[1] = 6
While Loop: Since j = 0 (starting from i - 1) and array[j] = 5 is not greater than current_element = 6, the while loop does not execute. No shifts are necessary because 6 is already in the correct position relative to 5.
Resulting Array After First Iteration: [5, 6, 3] (no change)
Second Iteration (i = 2):
Current Element: current_element = array[2] = 3
While Loop:
Start with j = 1. Compare array[j] = 6 with 3. Since 6 > 3, shift 6 to the right: [5, 6, 6].
Decrement j to 0. Compare array[j] = 5 with 3. Since 5 > 3, shift 5 to the right: [5, 5, 6].
j is decremented to -1. We exit the while loop.
Insertion: Insert current_element = 3 at array[j + 1], which is array[0]: [3, 5, 6].
Final Sorted Array: [3, 5, 6]
Summary of the Process:
First Iteration:

6 is already correctly positioned with respect to 5, so no shifting or insertion is necessary.
Second Iteration:

3 needs to be placed into its correct position.
It's compared first with 6 and then with 5, both of which are greater, so they are shifted to the right.
When j reaches -1, it's clear that 3 should be placed at the start of the array.
The array is then [3, 5, 6] after inserting 3 in the correct position.
This step-by-step breakdown shows how the insertion sort algorithm gradually builds up a sorted array from left to right, by inserting each element into its correct position within the sorted portion of the array"""
