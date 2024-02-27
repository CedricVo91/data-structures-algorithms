"""Given a number N return the index value of the Fibonacci sequence, where the sequence is: n"""

# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610


def fibonacciIterative(n=3):
    # result: index number of 3 in sequence: 4 if we have 0 based indexing, 5 otherwise
    # if we want non zero indexing, just change the < n by <=n, and adjust edge cases

    # we first need to recreate the sequence from scratch in the iterative approach:
    # edge case: n <= 1
    if n < 1:
        return 0  # zero based indexing
    elif n == 1:
        return "index 1 and 2 both store number equals 1"

    # main case:
    # store sequence in a list container
    sequence = [0, 1]  # base case
    index = 1  # current index. next value is number at current index i plus number at index-1
    while (
        sequence[index] < n
    ):  # problem is that we want to solve it via for loop which actually results in repeated add ons -> try while loop
        sequence.append(sequence[index] + sequence[index - 1])
        index += 1

    return index


# my solution is correct but an overkill as it builds up the whole fibonacci sequence from bottom up. That pattern is more common in dynamic programming and backtracking and combinatorics where one EXPLORES all possible correct solutions from the groun up
def fibonacciRecursively(
    n, sequence=[0, 1], index=1
):  # tell the function default values when nothing is added (first call)
    # base case: n=result of recursion
    if index < len(sequence) and sequence[index] == n:
        # first part after and to prevent index errors: accesing an empty list with an index gives me always index error!
        return (
            index  # not index+1 because we want zero indexing as solutions are in that
        )

    # recursive case: add curent number at index i to the to the number at index -1 to get new number at index +1
    # index = 0 # we need to store our current index in each iteration
    # question is if we have to store the current sequence like in backtracking of creating subsets to keep track of the sequence
    if n < 1:
        return 0  # zero based indexing
    elif n == 1:
        return "index 1 and 2 both store number equals 1"

    # n = 2: from then on the recursive case is started
    # recreate the sets

    sequence.append(sequence[index] + sequence[index - 1])
    # print(sequence)
    return fibonacciRecursively(n, sequence, index + 1)


# print(fibonacciRecursively(1))
print(fibonacciRecursively(610))
print(fibonacciIterative(610))

# for i in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]:
#   print(f"index of number {i} is:", fibonacciIterative(i))


# pattern:
# the overall pattern to solve it iteratively would be to focus on how to get to the next number and how the index increases.
# index icreases by 1, value increases by summing up the current number at index i (i=1 in our case) plus the number at index i-1, except for 0


print("-----Scenario A: Correct understood question ------------")

##solution: they want me to print out the fibonacci number for a given index. This should be a clarifying step first!
##maybe thats why my approach above where one enters the fibonacci number and gets its corresponding index took longer
# check if my approach above is correct and the reason why it took longer was because we were building up the structure first before selecting indexes
# check if when building up the structure first my base case and recursive step logic are correct!
# if yes, I could derive interesting insights with regards to patterns in recursion
# important to figure out and explore the build up recursion version the build down recursion. Is my problem above solvable by build down and its easier?


# solving the exercise: for any index n, give me the fibonacci number


# pattern: # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610 with zero indexing
# recursively with zero indexing i.e. counting indexes starting at zero
def new_recursive_fibonacci(n):  # should by default return fibo number 3
    if n <= 2 and n > 0:
        return 1

    elif n == 0:
        return 0

    # recursive step
    return new_recursive_fibonacci(n - 1) + new_recursive_fibonacci(n - 2)


print(
    [new_recursive_fibonacci(i) for i in range(16)]
)  # print all up including index 15 (16th number in our sequence)


# correction of my correct solution via code: base case pattern to use the input number more dynamically!


def new_recursive_fibonacci_corr(n):  # should by default return fibo number 3
    if n < 2:
        return n  # indexes equal the fibonacci numbers for index 0 and 1

    # recursive step: even if n = 2, we can apply the recursive step!
    return new_recursive_fibonacci_corr(n - 1) + new_recursive_fibonacci_corr(n - 2)


def new_iterative_fibonacci(n):
    if (
        n < 2
    ):  # same basecase logic as above. Pattern of returning input number when index equals output is universal
        return n

    # for iterative solution I need to store our
    fibo_sum = [0, 1]
    for index in range(
        2, n + 1
    ):  # n+1 to account for zero indexing and range function properties
        fibo_sum.append(fibo_sum[index - 1] + fibo_sum[index - 2])

    return fibo_sum[n]


print(new_iterative_fibonacci(6))


###solutions:
def fib(num):
    if num < 2:
        return num
    a = 0
    b = 1
    total = 0
    for i in range(num - 1):
        total = a + b
        a = b
        b = total
    return total


def fibonacci(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


print([fib(i) for i in range(10)])
print([fibonacci(i) for i in range(10)])
print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

print(
    fibonacci(15)
)  # should return 610 because they did  use zero indexing i.e. start counting at zero.


"""Differences for original question - scenario (A) - between my iterative solution and the provided iterative solution:Differences:

Your solution uses extra space to store the entire sequence up to n, while the provided solution only keeps track of the last two numbers, making it more space-efficient.
The provided solution is slightly more efficient in terms of space complexity because it does not store the entire sequence. It only keeps the last two numbers at any point 
in time, which is all that's needed to compute the next number in the sequence.
In a data structures and algorithms interview, both solutions demonstrate a clear understanding of the Fibonacci sequence
and the ability to implement an iterative solution. The provided solution might be slightly preferred due to its space efficiency,
but your solution is also a correct approach and would likely be well-received in an interview setting. Interviewers often look for correct, clear, and efficient code, and your solution meets these criteria.
If you explained your reasoning and showed awareness of the space trade-off, that would also reflect well on your problem-solving skills."""
