# bubble sort implementation


def bubble_sort(sample_array=[4, 3, 2, 1]):
    # imagine a worstcase bubble sort scenario to code it up: array is starting from the end i.e. 1,2,3,4 becomes 4,3,2,1
    for i in range(len(sample_array)):  # 0,1,2,3
        for j in range(
            len(sample_array)
            - 1
            - i  ## The - i part is to skip the comparison of elements that have already been sorted in previous passes
        ):  # -1 so that the arroy os not out of index i.e. sample_array[j+1] = sample_array[4] out of bounds when i = 3
            if sample_array[j] > sample_array[j + 1]:
                temp = sample_array[j]
                sample_array[j] = sample_array[j + 1]
                sample_array[j + 1] = temp
    return sample_array


print(bubble_sort([4, 3, 2, 1]))
"""Understanding the Inner Loop Range
Basic Concept of Bubble Sort:

In bubble sort, we repeatedly go through the array, swapping adjacent elements if they are in the wrong order. After each full pass through the array, the largest element among the unsorted elements bubbles up to its correct position at the end of the array.
The Role of the Outer Loop (i):

The outer loop (for i in range(len(sample_array))) tracks how many elements have been sorted and placed in their correct position at the end of the array. After the first pass, the largest element is in the correct position, after the second pass, the two largest elements are correctly placed, and so on.
Adjusting the Inner Loop (j):

Initially, we need to compare each element with its neighbor, so we need to iterate through the entire array. However, with each pass (i),
one more element is correctly positioned at the end of the array and does not need to be compared again.
Therefore, in the inner loop, for each increment of i, we can reduce the number of comparisons by one. That's why the range of the inner loop is len(sample_array) - 1 - i.
The - 1 part is to avoid the IndexError because we are comparing element j with j + 1.
The - i part is to skip the comparison of elements that have already been sorted in previous passes.
Visual Explanation
Consider an array of 5 elements [5, 4, 3, 2, 1].

First Pass (i = 0): We compare all pairs (5-4, 4-3, 3-2, 2-1). The largest number 5 bubbles to the end. We need 4 comparisons (5 elements - 1).
Second Pass (i = 1): Now, the last element (5) is in its correct position. We only need to compare up to the second last element. We need 3 comparisons (5 elements - 1 - 1).
Third Pass (i = 2): The last two elements (5 and 4) are in the correct positions. We compare the remaining first three elements. We need 2 comparisons (5 elements - 1 - 2).
... and so on
By adjusting the inner loop range with - 1 - i, we efficiently reduce the number of unnecessary comparisons in each pass, enhancing the performance of the bubble sort algorithm."""

##new recap
