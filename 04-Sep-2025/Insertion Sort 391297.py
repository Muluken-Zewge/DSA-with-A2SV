# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem


def insertionSort1(n, arr):
    key = arr[n-1]  
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        print(*arr)  
        j -= 1

    arr[j+1] = key

    print(*arr)

            
        