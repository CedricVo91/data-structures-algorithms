# merge sorted array so that final array is sorted
# questions: can we assume inputs are arrays? result duplicates or not?


def mergeSortedArray(array1, array2):
    merged_array = []  # correct

    # define which array is longer
    if len(array1) <= len(array2):
        first_array = array1
        second_array = array2
    else:
        first_array = array2
        second_array = array1

    i = 0
    for i in range(len(first_array)):
        if first_array[i] > second_array[i]:
            merged_array.append(second_array[i])

        elif first_array[i] < second_array[i]:
            merged_array.append(first_array[i])

        else:  # when they are the same
            merged_array.append(first_array[i])
            merged_array.append(second_array[i])
        i += 1
    for num in second_array[i:]:
        merged_array.append(num)

    return merged_array


print(mergeSortedArray([1, 2, 3, 4], [2, 4, 5, 6, 7]))

# result should be 1,2,2,3,4,4,5,6,7 but I get 1,2,3,,7

# solution: pattern: while loop prefered over two seperate for loops as we gain more control of both the indices of each array and can compare values dynamically


def mergeSortedArray_corr(array1, array2):
    merged_array = []  # correct
    i = 0  # define index for array1
    j = 0  # define index for array2

    # Iterate until one of the arrays is fully traversed
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1

    # in case array1 is longer
    while i < len(array1):
        merged_array.append(array1[i])
        i += 1

    # in case array1 is longer
    while j < len(array2):
        merged_array.append(array2[j])
        j += 1

    return merged_array


print(mergeSortedArray_corr([1, 2, 3, 4], [2, 4, 5, 6, 7]))
