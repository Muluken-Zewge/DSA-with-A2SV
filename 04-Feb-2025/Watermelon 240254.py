# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A

def main():
    # Take input and convert it to an integer
    weight_of_watermelon = int(input())
    
    # Check if the weight is even and greater than two
    if (weight_of_watermelon % 2) == 0 and (weight_of_watermelon > 2):
        output = 'YES'
    else:
        output = 'NO'
        
    print(output)
    
# call the main function to excute the code
main()