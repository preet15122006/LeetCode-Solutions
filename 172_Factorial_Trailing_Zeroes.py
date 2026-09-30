import math
class Solution(object):
    def trailingZeroes(self, n):
        factorial = math.factorial(n)
        s = str(factorial)
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != '0':
                break
            count += 1
        return count



         