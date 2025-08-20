# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

def main():
    
    t = int(input())
    for _ in range(t):
        x = int(input())
        if x == 1:
            print(3)
            
        # if x is a power of two
        elif x & (x - 1) == 0:
            print(x + 1)
        else:
            print(x & -x)
    
main()