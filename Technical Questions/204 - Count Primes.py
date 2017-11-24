# Dividing is slow, try the other way around
class Solution(object):
    def countPrimes(self, n):
        if n < 2: return 0

        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, n // 2 + 1):
            # if its a prime, every multiple of it is not
            if primes[i]:
                primes[i ** 2::i] = [False] * len(primes[i ** 2::i])

        return sum(primes)

# from math import sqrt
# # Dividing is slow, try the other way around
# class Solution(object):
#     def isPrime(self, n):
#         if n < 2: return False
#         if n == 2: return True
        
#         for i in range(2, n // 2 + 1):
#             if n % i == 0: return False
#         return True
        
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         counter = 0
#         for x in range(n):
#             if self.isPrime(x): counter += 1
#         return counter
