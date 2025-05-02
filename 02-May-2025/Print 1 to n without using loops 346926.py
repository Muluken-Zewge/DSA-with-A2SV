# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

def printNumber(n):
    If n == 0:
        return 
    printNumber(n-1)
    print(n, end= ' ')