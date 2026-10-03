class Solution(object):
    def isHappy(self, n):
        visited = set()
        while n!=1:
            if n in visited:
                return False
            visited.add(n)
            s = str(n)
            r = 0
            for i in range(len(s)):
                r += int(s[i])**2

            n = r
        return True
        