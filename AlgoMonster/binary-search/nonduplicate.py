##medium difficulty on leetcode
"""You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space."""
# Input: nums = [1,1,2,3,3,4,4,8,8] Output: 2


# pattern 1: sorted array <-> increasing order ->  its a monotonic function and thus we can apply binary search
# single non duplicate is to the left or equals feasability function:
# [1,1,2,3,3,4,4,8,8] -> [F,F,T,T,T,T,T,T,T]

# patterm 2: odd/even parity: duplicate pairs start at index at even number and after the single
# non duplicate number the pairs start at an odd number. Its important to emphasis on pairs here!
# hence any index given, if its an even index and the number at odd "index + 1" is different, we are on the right side of the singular number


def singleNonDuplicate(nums: list) -> int:
    def to_the_left_or_equals(idx):
        """#if we enter idx and idx points to a number right of non duplicate or
        points to the non duplicate, return True"""

        # edge case: our idx from binary search selects the last index in array to be looked at e.g. in [1,1,3] -> mid_0 = 1 -> left_i = mid_0 + 1 = 2
        if idx == len(nums) - 1:
            return True  # idx is the rightest value of array, the singular value is always on the right or equals it

        # normal cases:
        if idx % 2 == 0:
            if nums[idx] != nums[idx + 1]:
                return True

        else:  # index is odd
            if (
                nums[idx] == nums[idx + 1]
            ):  # we are on the right side with idx and singular is to the left
                return True

        return False

    # implement binary search
    ans = -1  # in case no single duplicate is given, we return -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if to_the_left_or_equals(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


# print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
# print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
# print(singleNonDuplicate([3, 3, 7, 7, 10, 10, 11]))
