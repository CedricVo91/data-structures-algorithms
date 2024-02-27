def binary_search(arr: list[int], target: int) -> int:
    """
    key assumption in vanilla binary search is that array is sorted
    """

    while (
        len(arr) > 0
    ):  # when there are no more elements in the array, we exist the loop realizing that the target is not in the array
        middle_i = len(arr) // 2
        if arr[middle_i] == target:
            return middle_i

        elif arr[middle_i] < target:
            arr = arr[middle_i + 1 :]

        else:  # when target is < than arr [middle i]
            arr = arr[:middle_i]

    return "Not in array"


""" 
the problem via slicing the array is that I don't keep track of the indices of the original array!
"""

##correction via help of tutor chat gpt: instead of slicing use left and right to keep track of current range of original array!


def binary_search(arr: list[int], target: int) -> int:
    """
    key assumption in vanilla binary search is that array is sorted
    """

    left_i = 0
    right_i = len(arr) - 1

    while (
        left_i <= right_i
    ):  # it needs to be smaller equals because if the target is foud left_i = right_i and they point to the same element
        middle_i = (left_i + right_i) // 2

        if arr[middle_i] == target:
            return middle_i

        elif target > arr[middle_i]:
            left_i = middle_i + 1

        else:  # target is smaller than arr[middle_i]
            right_i = middle_i - 1


def find_boundary(arr: list[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)
    left_i = 0
    right_i = n - 1
    while left_i <= right_i:
        m_i = (left_i + right_i) // 2

        if arr[m_i] == True:
            if arr[m_i - 1] == False or m_i == 0:
                return m_i

        elif arr[m_i] == True and arr[m_i - 1] == True:
            if m_i - 1 == 0:
                return m_i - 1
            right_i = m_i - 1

        else:  # arr[m_i] is False and True must be on right side as its ordered
            left_i = m_i + 1

    return -1


print(find_boundary([True, True, True, True, True]))
