import random

class RandomizedSet:
    '''Use O(1) time for insert, remove, and getRandom, so we use array + hashmap.'''

    def __init__(self):
        self.nums = []       # Stores the actual values
        self.dict = {}       # Maps value to its index in nums
        self.rand = random.Random()

    def insert(self, val: int) -> bool:
        # Check if the value already exists
        if val in self.dict:
            return False
        # Add value to the end of the list
        self.nums.append(val)
        # Store its index in the dictionary
        self.dict[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        # Check if the value exists
        if val not in self.dict:
            return False
        # Get index of the value to be removed
        index = self.dict[val]
        # Get the last element
        last_element = self.nums[-1]
        # Move the last element to the place of the one to be removed
        self.nums[index] = last_element
        self.dict[last_element] = index
        # Remove the last element
        self.nums.pop()
        # Delete val from the dictionary
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        # Pick a random index and return the value
        return self.nums[self.rand.randint(0, len(self.nums) - 1)]