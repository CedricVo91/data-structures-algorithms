# create the powerset of a list of n integers i.e. all the subsets without duplicates


def gen_subsets(nums):
    result = []

    def explore_subsets(index, current_subset):
        # Base case: if the end of the list is reached
        if index == len(nums):
            result.append(current_subset)
            return

        # Recursive case 1: Include the current number
        explore_subsets(index + 1, current_subset + [nums[index]])

        # Recursive case 2: Exclude the current number
        explore_subsets(index + 1, current_subset)

    explore_subsets(0, [])
    return result


# Test the function
print(gen_subsets([1, 2, 3]))
