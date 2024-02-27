# merge_sort implementation

# define merge function for two sorted sub arrays


def merge(left_array, right_array):
    merged_array = []
    i = 0
    j = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            j += 1

    # my logic: one of the two arrays has an element left i.e. the biggest element in both arrays
    # Append remaining elements of left_array
    while i < len(left_array):
        merged_array.append(left_array[i])
        i += 1

    # Append remaining elements of right_array
    while j < len(right_array):
        merged_array.append(right_array[j])
        j += 1

    return merged_array


print(merge([2], [3, 8]))

# now lets conquer merge sort


def merge_sort(array):
    # basecase
    if len(array) == 1:
        return array

    # recursive case

    # find the middle index of the array
    middle_index = len(array) // 2  # when len(array) == 5 -> middle index is 5//2 = 2
    # split array in half (left and right sub array)
    left = array[:middle_index]  # [2, 3, 8] , [2,3], [2]
    # print(left)
    right = array[middle_index:]  # [1, 5, 7], [8], [3]
    # print(right)

    # recursive step
    left_sorted = merge_sort(left)  # [2], [2,3], [2,3,8]
    print(left_sorted)
    right_sorted = merge_sort(
        right
    )  # [3], [8], restart recursion with [1,5,7] to finally get [1,5,7] (as it is  preordered it wouldnt' be necessary but we cant rely on this assumption), and then merge [2,3,8] and
    print(right_sorted)
    return merge(
        left_sorted, right_sorted
    )  # we need a return statement otherwise it will be None #[2,3], [2,3,8], [2,3,8]


print(merge_sort([2, 3, 8, 1, 5, 7]))


"""the error lies in the merge step: -> have a look at it tomorrow and recorrect. Merge works for merge([2,3], [8]) but not [[2],[3,8]]"""
