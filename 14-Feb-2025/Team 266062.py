# Problem: Team - https://codeforces.com/contest/231/problem/A

def main():
    
    num_of_problems = int(input())
    implemented_solutions = 0
    for problem in range(num_of_problems):
        solution_set = list(map(int, input().split()))
        occurance_of_1 = solution_set.count(1)
        if occurance_of_1 > 1:
            implemented_solutions += 1
    
    print(implemented_solutions)
        
main()