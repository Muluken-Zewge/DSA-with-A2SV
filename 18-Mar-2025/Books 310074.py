# Problem: Books - https://codeforces.com/contest/279/problem/B

def main():
    n, t = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    left = 0
    total_time = 0
    max_books = 0
    
    for right in range(n):# right pointer to expand the window
        total_time += sequence[right]

        #shring the window from the left if the total time exceeds t
        while total_time > t:
            total_time -= sequence[left]
            left += 1
    
        max_books = max(max_books, right - left + 1)
        
    print(max_books)

main()
