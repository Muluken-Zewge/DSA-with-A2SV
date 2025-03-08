# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

def main():
    n,k = map(int, input().split())
    sequence = list(map(int, input().split()))
    sequence.sort() # sort the sequence of numbers
    
    if k == 0:
        #if k==0, there should be a positive number which is less than the smalles element in the sequence
        x = sequence[0] - 1
        if x >= 1:
            print(x)
        else:
            print(-1)
    elif k == n:
        #if n==k, any number greater or equal to the largest number in the sequence can be an answer
        x = sequence[-1]
        print(x)
    else: #for 0 < k < n
        #if there are duplicates of the sequence[k-1] value, there won't be a number to satisfy the condition
        if sequence[k-1] != sequence[k]:
            x = sequence[k-1]
            print(x)
        else:
            print(-1)

main()