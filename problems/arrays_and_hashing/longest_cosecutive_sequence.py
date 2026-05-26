class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        n = 1
        l = 1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] - 1:
                n += 1
            elif nums[i] == nums[i+1]:
                pass
            else:
                l = max(l,n)
                n = 1
        l = max(l,n)
        return l