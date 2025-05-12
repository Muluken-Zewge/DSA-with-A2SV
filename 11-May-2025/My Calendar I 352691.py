# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            # Check for overlap
            if start < e and s < end:
                return False
        self.bookings.append((start, end))
        
        return True

#binary search version
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect_right(self.bookings, (start,end))

        #check overlap with the previous interval
        if idx > 0:
            prev_start, prev_end = self.bookings[idx-1]
            if start < prev_end:
                return False

        #check overlap with the next interval
        #if idx == len(self.bookings),it will be added at the end
        if idx < len(self.bookings):
            next_start, next_end = self.bookings[idx]
            if end > next_start:
                return False
        
        self.bookings.insert(idx, (start,end))

        return True
