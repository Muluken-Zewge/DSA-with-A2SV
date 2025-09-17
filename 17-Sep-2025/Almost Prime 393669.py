# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def main():
    
    def is_almost_prime(n: int) -> bool:
        factors = []
        d = 2 
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        
        if n > 1:
            factors.append(n)
            
        return len(set(factors)) == 2
    
    n = int(input())
    almost_primes = 0
    for i in range(1, n+1):
        if is_almost_prime(i):
            almost_primes += 1
    print(almost_primes)

main()