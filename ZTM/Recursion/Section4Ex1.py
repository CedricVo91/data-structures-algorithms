# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop


def findFactorialRecursive(number):
    if number <= 1:
        return 1

    # recursive element: at each step we have a discrete, often binary, decision to make (XOR) depending on the if condition = base case
    else:
        number = (
            number - 1
        )  # this does not work once we corrected the error below -> when 5 becomes number
        return 5 * findFactorialRecursive(
            number
        )  # error: we need to put the input "number" instead of 5 to the recursive step to avoid running 5 for all the subfunctions


def findFactorialIterative(number):
    prod = 1
    for num in range(1, number + 1):
        prod = prod * num
    return prod


print(findFactorialRecursive(5))

print(findFactorialIterative(5))


##Solution


def findFactorialIterative(number):
    prod = 1
    for num in range(2, number + 1):
        prod = prod * num
    return prod


# print(findFactorialIterative(2)) correct


def findFactorialRecursive(number):
    if (
        number == 2
    ):  # avoid extra loops if possible i.e. extra function calling by return 2
        return 2

    return number * findFactorialRecursive(
        number - 1
    )  # important: I have to adjust number, otherwise in each instance it multiplies 5 with what ever sub function; e.g. factorial(5)= 5* factorial(4) = 5*factorial(3)


print(findFactorialRecursive(5))

"""The pattern here in the recursive case is to repeat the same action of multiplying the input number by a the same 
function but on a smaller subset of the inital input data until the data set has just its smallest non divisible discrete number 
as the data set e.g. 2 in our example (basecase). Once this basecase is reached I want to multiply it by the next bigger discrete 
data point e.g. 3 that in turn is called by the one data point larger parent function i.e. recursive(4) that again multiplies this 
one larger data point by 3 and recursive(4) is called by the parent function recursive 5 and returns by definition 5*recursive(4) 
i.e. 5*4*3*2*1"""

"""Interesting insight in the factorial recursion: we do not need to define a container to store sub products. It returns the whole calculation at once"""
