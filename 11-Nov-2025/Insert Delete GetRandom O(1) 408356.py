# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.values = [] # store the values
        self.val_to_index = {} # map a value to it's index in the values list

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_element = self.values[-1]

        # move last element into the spot of the one to remove
        self.values[index] = last_element
        self.val_to_index[last_element] = index

        # remove last element from list
        self.values.pop()
        # delete the removed value from map
        del self.val_to_index[val]

        return True


    def getRandom(self) -> int:
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()