def find_boundary(arr: list[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)
    left_i = 0
    right_i = n - 1

    # edge case: if first item is true we return it without having to run through the whole binary search algorithm, more efficient
    if arr[left_i] == True:
        return left_i

    while left_i <= right_i:
        m_i = (left_i + right_i) // 2

        if arr[m_i] == True:
            if arr[m_i - 1] == False:
                return m_i

        elif arr[m_i] == True and arr[m_i - 1] == True:
            if m_i - 1 == 0:
                return m_i - 1
            right_i = m_i - 1

        else:  # arr[m_i] is False and True must be on right side as its ordered
            left_i = m_i + 1

    return -1


###solution provided: more concise, more streamlined, less efficient in edge case of T,T,T,T i.e. only true values
### always use this template when you look for the first entry in a sorted array where a condition is true


def find_boundary(arr: list[bool]) -> int:
    left, right = 0, len(arr) - 1
    ###initialize the boundary index to keep track of it and return -1 if no True values in array
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


def first_not_smaller(arr: list[int], target: int) -> int:
    # edge case 1:
    if arr[0] == target:
        return 0

    # edge case 2: target biggger than any number in array
    if arr[-1] < target:
        return -1

    # binary search as its sorted
    left_i = 0
    right_i = len(arr) - 1
    ##initialize boundary index as we are looking for the FIRST True condition
    boundary_index = (
        -1
    )  # default returns the situation where we do not have condition fulfilled

    while left_i <= right_i:
        mid_i = (left_i + right_i) // 2

        if arr[mid_i] >= target:
            boundary_index = mid_i
            # we can't return the index yet, as we have to check for the first true
            right_i = (
                mid_i - 1
            )  # in the last iteration where we have only one check left our right becomes smaller than left i.e. becomes -1 and we exit while loop

        else:
            # arr[mid]
            left = mid_i + 1

    return boundary_index
