class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        result = []

        for i in intervals:
            if len(result) == 0:
                result.append(i)

            elif result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])

            else:
                result.append(i)

        return result