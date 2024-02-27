# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop
# facotrial of any number. NUuber = input. Input = 5 -> 5! = 5*4*3*2*1 = 120


# recursive:
def fac(number):
    # base case
    if number == 2:
        return number
    # recursive element
    return number * fac(number - 1)  # correct! I achieved it faster than two weeks ago


print(fac(5))  # correct


# iterative:
def fac_it(number):
    fac = 1
    for num in range(
        1,
        number
        + 1,  # I could actually already start at 2 instead of 1. multipyling by 1 does not change anything. extra step not needed.
    ):  # here I did not think of generalization, ebst to test with other number!
        fac = fac * num
    return fac


print(fac_it(6))

# Given a number N return the index value of the Fibonacci sequence, where the sequence is: n i.e. they mean enter index and give out fibo number
##problem: they want me to print out the fibonacci number for a given index. This should be a clarifying step first!
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610


def fib(index):
    # return fibonacci number at given index (assuming zero indexing)
    # index = 0, return 0
    # index = 1, return 1
    # index = 2, return 1
    # index = 3, return 2
    # index = 4, return 3
    # index = 5, return 5
    # index = 6, return 8

    # base case: where does recursive step logic end?
    # index == 1, return 1
    if index == 1:
        return 1

    if index <= 0:
        return 0
    ## here I could have directly combine the two: clear pattern of if index = num, return num (same num as index)
    # if index <= 1 (or < 2):
    # return index

    # recursive step
    # for each index smaller than initial index i.e. index -1, we return the sum of same function but index -1 and index -2
    return fib(index - 1) + fib(index - 2)


print(fib(7))


# reverse a string using recursion
def reverse_string(string):
    # remember that strings are like lists and I can index them in python
    if len(string) == 1:
        return string

    # recursive step:
    return reverse_string(string[1:]) + string[0]


print(reverse_string("Cedric is cool"))  # works

# pattern that works for me to understand. When designing the recursive step, first think about generally how to break down input problem,
# then think about basecase
# if there are two base cases that come to my mind, think about how to combine them. A useful pattern is to look at the pattern of if input number equals output number, then code it.
# #then adjust/finetune recursive step by thinking of a concrete example of the function instance of one before the function returns basecase
# think about the structure of the return statement. do we need the recursive step to be in a return statement, if yes, what mathematical operation do we need to combine the basecase and the input of the function instance before to get the right result
# then test it with these inputs where we enter the function, where base case is not reached yet, but for the next recursive function call the base case is reached
# let recursion do its magic without thinking through all the functions that get called -> waste of energy
