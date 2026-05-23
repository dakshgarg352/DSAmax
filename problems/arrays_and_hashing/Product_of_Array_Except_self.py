class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_no = nums.count(0)
        p = 1
        for i in nums:
            if i != 0:
                p*=i
                
        ans = []
        
        for i in nums:
            if zero_no > 1:
                ans.append(0)
                
            elif zero_no == 1:
                if i == 0:
                    ans.append(p)
                else:
                    ans.append(0)
            
            else:
                ans.append(p//i)
        
        return ans