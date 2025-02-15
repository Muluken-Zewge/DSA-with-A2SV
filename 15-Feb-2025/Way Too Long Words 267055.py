# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

def main():
    num_of_words = int(input())
    for _ in range(num_of_words):
        word = input()
        if len(word) <= 10:
            print(word)
        else:
            first_char = word[0]
            last_char = word[-1]
            len_between = len(word[1:-1])
            print(f"{first_char}{len_between}{last_char}")
    
main()