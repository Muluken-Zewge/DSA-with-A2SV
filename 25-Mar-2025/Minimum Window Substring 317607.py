# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_counter = Counter(t) 
        window_counter = Counter()# Count occurrences inside the sliding window

        left = 0  
        right = 0 
        min_length = float("inf") # to Store minimum window length
        min_window = ""  # Store result
        required_chars = len(t_counter)  # Unique chars required
        matched_chars = 0  # How many chars we have in correct count

        while right < len(s):  
            # Add current character to window
            char = s[right]
            window_counter[char] += 1

            # If the char count in the window matches the count in `t`, increase `matched_chars`
            if char in t_counter and window_counter[char] == t_counter[char]:
                matched_chars += 1

            # If we have all required characters, minimize the window
            while matched_chars == required_chars:
                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]

                # shrink from the left
                window_counter[s[left]] -= 1
                #check if we lost a required character
                if s[left] in t_counter and window_counter[s[left]] < t_counter[s[left]]:
                    matched_chars -= 1

                left += 1  # Shrink window from left

            right += 1  # Expand window from right
        
        return min_window
