# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.counter = defaultdict(int) # to count the number times each number exist
        self.frequency = defaultdict(int) # to count numbers with a given number of frequency

    def add(self, number: int) -> None:
        self.counter[number] += 1
        self.frequency[self.counter[number]] += 1
        
        # subtract one from the previous frequency
        if self.counter[number] - 1 > 0:
            self.frequency[self.counter[number] - 1] -= 1
            if self.frequency[self.counter[number] - 1] == 0:
                    del self.frequency[self.counter[number] - 1] # remove if it no longer exist
    
    def deleteOne(self, number: int) -> None:
        if self.counter[number] != 0: # check if the number exists
            self.frequency[self.counter[number]] -= 1 # decreament the number's frequency
            if self.frequency[self.counter[number]] == 0:
                del self.frequency[self.counter[number]] # remove if it no longer exist

            self.counter[number] -= 1
            if self.counter[number] == 0:
                del self.counter[number]
            else:
                # add 1 to the decremented frequency
                self.frequency[self.counter[number]] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.frequency:
            return True

        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)