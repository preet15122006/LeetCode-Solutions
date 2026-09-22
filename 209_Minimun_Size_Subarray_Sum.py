class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        ans = len(nums) + 1

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                ans = min(ans,i-left+1)
                total -= nums[left]
                left += 1

        if ans == len(nums) + 1:
            return 0
        return ans
        