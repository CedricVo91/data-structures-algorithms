##First recurring character

##given array [1,2,3,3,4]  it should return 3


def frc(array):
    container = {}
    for char in array:
        if char in container:
            return char
        container[char] = 1  # placeholder


"""dictionarries in python are implemented via a hashmap. A if char in container 
does not loop over the whole container but uses the hashed index of that char key to access it in O(1)
in other containers it would be a for loop but in python if x in container does not always mean the same 
and depend on the actual data structure used as a container"""

"disadvantage: we increased memory space by O(n) as we creater the container"


print(frc([1, 2, 2, 3, 4, 5, 5]))
