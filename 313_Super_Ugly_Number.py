class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1] *n
        idx = [0] * len(primes)

        for i in range(1,n):
            smallest = float('inf')
            for j in range(len(primes)):
                val = ugly[idx[j]] * primes[j]
                if val < smallest:
                    smallest = val

            ugly[i] = smallest

            for j in range(len(primes)):
                if ugly[idx[j]] * primes[j] == smallest:
                    idx[j] += 1

        return ugly[n-1]