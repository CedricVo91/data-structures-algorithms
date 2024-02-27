"""
A mountain array is defined as an array that

has at least 3 elements
has an element with the largest value called "peak", with index k. 
The array elements strictly increase from the first element to A[k], and then strictly decreases from A[k + 1] to the last element of the array. 
Thus creating a "mountain" of numbers.
That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k. 
Note that the peak element is neither the first nor the last element of the array.

Find the index of the peak element. Assume there is only one peak element.
"""

# my solution runs correctly but does not check for potential edge case with out of bounds index and also needs two iterations when only 1 is sufficient


def peak_of_mountain_array(arr: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left_i = 0
    right_i = len(arr) - 1

    while left_i <= right_i:
        mid_i = (left_i + right_i) // 2

        if arr[mid_i] > arr[mid_i - 1] and arr[mid_i] > arr[mid_i + 1]:
            return mid_i

        elif (
            arr[mid_i] > arr[mid_i + 1]
        ):  # we know we are on the decreasing side of th mountain
            right_i = mid_i - 1

        else:  # mid_i is smaller than the next,  we are still on increasing side
            left_i = mid_i + 1


##correction
def peak_of_mountain_array(arr: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left_i = 0
    right_i = len(arr) - 1
    boundary_index = -1

    while left_i <= right_i:
        mid_i = (left_i + right_i) // 2

        if mid_i == len(arr) - 1 or arr[mid_i] > arr[mid_i + 1]:
            boundary_index = mid_i
            right_i = mid_i - 1

        else:  # mid_i is smaller than the next,  we are still on increasing side
            left_i = mid_i + 1

    return boundary_index
