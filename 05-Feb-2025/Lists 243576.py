# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    num_list = []
    for _ in range(N):
        #take each command and convert it to list of strings
        command = input().strip().split()
        
        if command[0] == 'insert':
            i = int(command[1])
            e = int(command[2])
            num_list.insert(i,e)
        elif command[0] == 'print':
            print(num_list)
        elif command[0] == 'remove':
            e = int(command[1])
            num_list.remove(e)
        elif command[0] == 'append':
            e = int(command[1])
            num_list.append(e)
        elif command[0] == 'sort':
            num_list.sort()
        elif command[0] == 'pop':
            if num_list: #check if the list isnot empty
                num_list.pop()
        else:
            num_list.reverse()
            
        
            
   