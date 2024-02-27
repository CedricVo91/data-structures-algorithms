# create a reverse string via an array


def reverse(string):
    new_string = ""  # string acts as an array
    for i in range(1, len(string) + 1):  # adjust loop accordingly
        new_string += string[-i]
    return new_string


print(reverse("Cédric"))


##solution
def reverse_corr(string):
    # check input - we cant assume that input is a string by default, plus if string is less than one letter, we just return
    if type(string) != str or len(string) < 2:
        return "hmmm thats not good"

    new_string = ""
    for i in range(1, len(string) + 1):
        new_string += string[-i]
    return new_string


print(reverse("Cédric is the best"))

# alternatively using an array


def reverse_str_alt(string):
    reversed_string = []

    for i in range(1, len(string) + 1):
        reversed_string.append(string[-i])

    # use the join method to join strings of a list without spaces by defining ""
    return "".join(reversed_string)


print(reverse_str_alt("Cédric"))
