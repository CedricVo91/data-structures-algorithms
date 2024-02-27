def selectionsort(array):
    n = len(array)  # 4

    for i in range(
        n - 1  # i= 0,1,2
    ):  # the last item in the array will be the biggest one and does not need to be compared to its prior number
        smallest_index = (
            i  ##correction: it must be reinitialized with every new unsorted subarray
        )
        for j in range(i + 1, n):
            if (
                array[j] < array[smallest_index]
            ):  # just compare the smallest value with the rest of the array: start with default of smallest index = 0 and then come back to same index 0 when relooping
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]

    return array


print(selectionsort([4, 3, 2, 1]))
