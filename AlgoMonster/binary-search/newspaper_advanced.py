##advanced problems usually need to be broken down in multiple functions - often a helper function and a main function that makes use of helper function


##helper function: feasable
##intuition: we have accumulation of time that is not feasable i.e. not enough workers to cover the time.
##but at a certain guessed optimum (maximum) time per worker we choose a new one
##binary search here works as an optimization problem where you first guess an optimal middle time and then iteratively narrow it down
## reasion for binary search: monotonic nature of the problem: once a total time is feasable to read all the newspapers, any time higher than that is also feasible
"""
The reason binary search is applicable in this problem is because of the monotonic nature of the problem.
What do we mean by monotonic here? If a given time t is feasible for num_coworkers 
to finish all the newspapers, then any time greater than t will also be feasible"""

"""
basically we are looking for the first true value after an initial sequence of false values
"""


def feasable(newspapers_read_times: list[int], num_coworkers: int, limit: int) -> bool:
    accumulated_time = 0
    num_workers = 1
    for read_time in newspapers_read_times:
        if accumulated_time + read_time <= limit:
            accumulated_time += read_time
        else:
            num_workers += 1
            # reset accumulated time as now the new worker steps in to overtake the current newspaper
            accumulated_time = 0
            # add time of the current iteration of newspaper pile i.e. the time of current newspaper to new worker
            accumulated_time += read_time
    # print function for illustration purposes
    print(
        f"minimum number of workers needed to complete the task given current time limit {limit} min is: {num_workers} workers"
    )
    if num_workers <= num_coworkers:
        return True
    else:
        return False


# print(feasable([7, 2, 5, 10, 8], 2, 10))  # should print False
# print(feasable([7, 2, 5, 10, 8], 4, 10))  # should print True

"""incorporating the above, 
we know that maximum_time needed to complete the task is if just 1 worker reads all the papers.
And the minimum time we spend in the best case is the time of the longest newspaper i.e. the max of reading time array
the optimum lies in between. Hence, we start with a limit per worker of average between the two extremes 
and iteratively get to the first True case in the feasible sequence e.g. FFFTTTT """


def newspapers_split(newspapers_read_times: list[int], num_coworkers: int) -> int:
    max_time = sum(newspapers_read_times)
    min_time = max(newspapers_read_times)

    left = min_time
    right = max_time
    optimal_time = -1

    while left <= right:
        print(f"current minimum bound: {left}")
        print(f"current max bound: {right}")
        mid = (left + right) // 2
        print(f"current guess of optimal upper reading limit time per worker: {mid}")
        if feasable(newspapers_read_times, num_coworkers, mid):
            optimal_time = mid

            right = mid - 1

        else:
            left = mid + 1
            print(
                f"Optimum time per worker is not feasible, lower bound gets adjusted to {left}"
            )

    return optimal_time


# feasible and we narrow down search space from the right i.e. the TTTT part of the sequence FFFTTTTT
print(newspapers_split([7, 2, 5, 10, 8], 2))
# not feasible and we narrow down search space from the left i.e. the FFF part of the sequence FFFTTTTT
# print(newspapers_split(newspapers_read_times=[2, 3, 5, 7], num_coworkers=1))
