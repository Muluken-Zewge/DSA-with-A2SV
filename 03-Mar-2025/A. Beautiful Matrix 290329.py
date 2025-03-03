# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

def main():
    rows, colums = 5,5
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    for r in range(rows):
        for c in range(colums):
            if int(matrix[r][c]) == 1:
                position_of_1 = [r,c]
                break
        
    output = abs(2-position_of_1[0]) + abs(2-position_of_1[1])

    print(output)

main()