# reverse a string using recursion


def reverse_string(string):
    print(string)  # just for illustration purposes
    if len(string) <= 1:  # in case of odd count of letters and we get the middle one
        return string  # whats the easiest string to reverse: just one number

    return string[-1] + reverse_string(string[0:-1])
    # I knew it that I had to add strings together. adding letters together is still a string


# print(reverse_string("string is cool"))

"""Pattern 1: in python we can sum up letters and the result is the sum of the strings: "s" + "r" = "sr" 
   Pattern 2: like in recursive and fibonacci if im building up on smth, use the return to return sum from incremental step and recursive function call of a smaller instance of the input """


##bonus: add the call stack and then the call off procedure
def visual_reverse_string(string):
    print(
        f"current function stack level: {(6-len(string))}"
    )  # illustrates the inputted string of current function call
    if len(string) <= 1:  # in case of odd count of letters and we get the middle one
        print(f"base case of {string} is reached and gets called off")
        return string  # whats the easiest string to reverse: just one number

    # helper variable
    result = string[-1] + visual_reverse_string(string[:-1])
    print(f"function stack {6-len(string)} gets called off with result: {result}")
    return result


# visual_reverse_string("string")


# problem of the above is that its limited to strings with 6 letters. If we want to include the current level of the stack,
# we cant just initialize a counter variable as in every recusive call it gets set to the default value i.e. does not build up
# pattern: if we want to include a counter that counts the recursive calls and then execution levels, we need to have it as input in recursive function
# pattern: if I want to track the recursive call, I can save the recursive call in a variable
# there is a difference between function that runs and a function that returns!see below with the current function in stack and the return value


def visual_reverse_string_corr(string, counter=0):
    print(f"stack is at current level {counter}")
    if len(string) <= 1:
        print(
            f"base case of {string} is reached and the function in the stack position {counter} gets called off the stack"
        )
        return string

    current_function_in_stack = string[-1] + visual_reverse_string_corr(
        string[:-1], counter=counter + 1
    )
    print(f"the current function that is called and realized is at level {counter}")
    return current_function_in_stack


print(visual_reverse_string_corr("string"))
