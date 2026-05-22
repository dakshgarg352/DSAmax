class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        mp = defaultdict(int)
        for i in nums:
            mp[i]+=1
        for i in range(k):
            mx = max(mp,key=mp.get)
            del mp[mx]
            ans.append(mx)
        return ans