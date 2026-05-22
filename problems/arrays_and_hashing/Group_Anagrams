class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for i in strs:
            mp[str(sorted(i))].append(i)
        
        return list(mp.values())