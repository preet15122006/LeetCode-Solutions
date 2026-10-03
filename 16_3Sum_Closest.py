class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()

        cl = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                t = nums[i] + nums[l] + nums[r]

                if abs(t-target) < abs(cl - target):
                    cl = t

                if t < target:
                    l += 1

                elif t > target:
                    r -= 1
                else:
                    return t

        return cl        