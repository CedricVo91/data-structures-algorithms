def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    arr = [integer for integer in range(1, n)]
    left_i = 0
    right_i = len(arr) - 1
    boundary_index = -1

    while left_i <= right_i:
        mid_i = (left_i + right_i) // 2

        if (
            arr[mid_i]
        ) ** 2 >= n:  # first true i.e. where the square is equals or bigger
            boundary_index = mid_i
            right = mid_i - 1

        else:  # arr[mid_i]**2 < n
            left_i = mid_i + 1

    # when we have the situation where arr[boundary_index] != n or
    if (arr[boundary_index]) ** 2 != n and boundary_index != -1:
        boundary_index = boundary_index - 1

    return boundary_index


###correction
##1. I don't need an array and can directly focus on the actual numbers
##2. handle edge case first to directly give them back - more efficient than starting binary search


def square_root_corr(n: int) -> int:
    # edge case:
    if n < 2:
        return n  # n =1 or n=0 has square root of n resp 0 or 1

    left = 2
    right = n
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid

        if mid * mid > n:
            boundary_index = mid
            right = mid - 1

        else:
            left = mid + 1
    return (
        boundary_index - 1
    )  # logic is: if square root of n is not in the array, then it always means we have an n whose squareroot is not a whole number. hence we need to go one back and tak efirst false
    # in other words we will never return -1 as we will always find a number, i,  that satisfies i < squareroot(n)
