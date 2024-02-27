# implement a hash table


class myHashTable:
    def __init__(self, size=10):
        self.array = [[] for _ in range(size)]

    def _hash(self, key):
        # convert key to integer, resulting in hash_sum, then take modulus to return position in hashtable
        hash_sum = 0  # plan: sum up the ascii values for each character in the key to get to an integer
        for char in key:
            hash_sum += ord(char)  ## `ord` converts a character to its ASCII value
        return hash_sum % len(self.array)

    def insert(self, key, value):
        index = self._hash(key)
        found = False
        for i, (existing_key, existing_value) in enumerate(self.array[index]):
            if key == existing_key:
                self.array[index][i] = (
                    key,
                    value,
                )  # replace old (key,value) with new key,value tuple (only the value is different i.e. gets updated)
                found = True
                break

        if not found:  # if not true
            self.array[index].append((key, value))

    def search(self, key):
        index = self._hash(key)

        for i, (k, v) in enumerate(self.array[index]):
            if key == k:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)

        for i, (k, v) in enumerate(self.array[index]):
            if key == k:
                self.array[index].pop(i)
                return "key value pair removed successfully"

        return "No key was found"

    def get_keys(self):  # get all the keys of the hash table
        keys_array = []
        for hashmaplocation in self.array:  # list of lists so we can iterate over it
            for k, v in hashmaplocation:
                keys_array.append(k)
        return keys_array

    def get_values(self):
        values_array = []
        for hashmaplocation in self.array:  # list of lists so we can iterate over it
            for k, v in hashmaplocation:
                values_array.append(v)
        return values_array


"""The primary purpose of a hash function in a hash table is to map keys to indices in an array. 
    This array is where the actual data (key-value pairs) is stored   
    
    Whether you choose linked lists or dynamic arrays, the fundamental principle of separate chaining 
    remains the same: multiple entries can be stored at each index of the array, with each entry corresponding to a unique key and its value.
    """
