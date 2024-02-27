# implement bubble, insertion and selection sort again
def insertionsort(unsorted_list):
    """
    sorts a list of integers in n*(n-1)/2 time complexity
    """
    for i in range(1, len(unsorted_list)):
        while (
            i > 0 and unsorted_list[i] < unsorted_list[i - 1]
        ):  ### learning: i hast to be  bigger than 0, not >=0 as otherwise we would get i-1 =-1 at a certain point
            unsorted_list[i - 1], unsorted_list[i] = (
                unsorted_list[i],
                unsorted_list[i - 1],
            )
            i -= 1

    return unsorted_list


print(insertionsort([5, 3, 1, 2, 4]))


##selection sort
def selectionsort(unsorted_list):
    """
    sorting in
    """

    for i in range(len(unsorted_list)):
        ##learning: in selectionsort we keep track of the index of the min val and not the min val itself!
        min_val_index = i
        # start at i + 1 as we already know that the value at i is smaller than whatever comes later
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_val_index]:
                min_val_index = j
        # we have the index of min val of the list here
        # swap the values
        unsorted_list[i], unsorted_list[min_val_index] = (
            unsorted_list[min_val_index],
            unsorted_list[i],
        )
    return unsorted_list


print(selectionsort([5, 3, 1, 2, 4]))

"""
compared to the algo monster solution my inner loop is less redunandt as it starts at i+1.
Your selectionsort Function: Your inner loop starts with j = i + 1. This means that in each iteration of the outer loop, the inner loop starts comparing from the next element (i + 1) rather than the current element i. Since the element at index i is already being considered as the initial minimum (min_val_index = i), there's no need to compare it with itself. This makes your inner loop slightly more efficient as it does one less comparison in each iteration of the outer loop.

The sort_list Function: In this function, the inner loop starts with j = i. This means it includes an unnecessary comparison of the element at index j with itself in each iteration of the outer loop. While this doesn't affect the correctness of the algorithm, it does add an extra comparison in each iteration, which is not needed.




"""


def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):  ##n = 5, we have 0,1,2,3,4 iterations
        for j in range(n - 1 - j):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = (
                    unsorted_list[j + 1],
                    unsorted_list[j],
                )
