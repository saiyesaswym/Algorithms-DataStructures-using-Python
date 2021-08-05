"""
Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom.
Array List has indexes and could provide Insert and GetRandom in average constant time, though has problems with Delete.
Time complexity: O(1)
Space complexity: O(n)
"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.hmap = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain
        the specified element.
        """
        if val in self.hmap:
            return False
        self.hmap[val]=len(self.arr)
        self.arr.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hmap:
            return False
        #Move last element to index of val
        last_val, idx = self.arr[-1], self.hmap[val]
        self.arr[idx], self.hmap[last_val] = last_val, idx
        #Delete last element
        self.arr.pop()
        del self.hmap[val]
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
