# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        s = input()
        n = len(s)
        res = ''
        
        left = 0
        # the only way to guarante the char works is,if it appears consecutively in odd number of times.
        while left < n:
            consecutive_occurance = 0
            right = left
            #to count the number of times the char occurs consecutively
            while right < n and s[left] == s[right]:
                right += 1

            consecutive_occurance = right - left
            #check if it occurs odd number of times consecutively
            if consecutive_occurance % 2 == 1 and s[left] not in res:
                res += s[left]
            left = right

        
        print("".join(sorted(res)))

main()