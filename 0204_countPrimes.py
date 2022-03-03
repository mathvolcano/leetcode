"""
204. Count Primes
https://leetcode.com/problems/count-primes/
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        # Space complexity O(n) for is_prime array
        # Time complexity is O(nloglogn) because
        # for each integer i spend n/i operations eliminating multiples
        # so T(n) = n * (1/2 + 1/3 + 1/5 + ...+) ~ n log log n
        if n < 3: return 0

        # Store labels of whether a num < n is a prime
        is_prime = [1] * n
        is_prime[:2] = [0, 0]

        # Sieve of Eratosthenes
        for i in range(2, int(n**.5) + 1):
            if is_prime[i]:
                # i+i, i+2*i, ... , i*(i-1) already marked 0
                is_prime[i*i:n:i] = [0] * len(is_prime[i*i:n:i])
        return sum(is_prime)
