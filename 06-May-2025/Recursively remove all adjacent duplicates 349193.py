# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

#function to remove one adjecent duplicates in one go
def removeAdjacent(s: str) -> str:
    result = ''
    i = 0
    n = len(s)

    while i < n:
        # Check for adjacent duplicates
        if i < n - 1 and s[i] == s[i + 1]:
            # Skip all adjacent duplicates
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
            i += 1  # Skip the last one of the duplicate group
        else:
            result += s[i]
            i += 1

    return result

def removeAdjacentDuplicates(s: str) -> str:
    new_s = removeAdjacent(s)
    # Base case: no change after one full pass
    if new_s == s:
        return new_s
    # Recursive step
    return removeAdjacent(new_s)