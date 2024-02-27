"""
Problem: Sum of Digits
Question: Write a recursive function that takes an integer n and returns the sum of its digits. 
For example, if the input is 123, the function should return 6 (which is 1 + 2 + 3).

Please feel free to think out loud as you approach this problem, and I'll provide guidance if you need any assistance. 
Remember, the key here is to understand how to break down the problem recursively. 
Take your time to think about how you can reduce the problem into smaller, more manageable parts.
"""

"""
Ok, let me first not down the key points and any questions.
key points:
- recursive function  with 
- input: integer n 
- output: sum of digits in integer n 
- e.g.: input =  123, output = 1+2+3 = 6 

questions:
- the main value of this function would be to obtain the sum of an integer with minimal code using recursion?
- do we have the space and memory to host this function or is there a limit to integer "n", do we have the time?

"""
"""
Ok, when identifying the digits using mathematical operation I would like to leverage the fact of the based 10th number system. 
Depending on the length of (integer n) - 1,called length, we have 1*10^length, and with the modulus we can get the digits as the remaindes to integer n % 10 ^ length 


"""


def sumdigits(n):
    if n // 10 == 0:
        return n

    return n % 10 + sumdigits(
        n // 10
    )  # 123//10 = 12, 24 //10 => 2.4 => 2 ##it goes from right to left


print(sumdigits(24))

"""
Patterns to memorize (i.e. important not to memorize the solution code but the pattern): 

1. Simplicity in Extracting the Last Digit: 
In base-10, extracting the last digit of a number is straightforward using the modulo operation (n % 10). 
It's a simple and efficient way to isolate the rightmost digit.

2. Ease of Reducing the Problem Size: 
Using integer division by 10 (n // 10) naturally reduces the number by removing its last digit, 
thus effectively shrinking the problem size with each recursive call. This is a direct and efficient method to iterate through the digits.
"""


"""I would need recursion prep so I can implement merge sort via recursion"""


##new question reverse a string


def reverse_str(string):
    if len(string) == 1:
        return string

    return reverse_str(string[1:]) + string[0]


print(reverse_str("string"))
