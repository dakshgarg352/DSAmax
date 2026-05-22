class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in s:
            alpha[ord(i) - 97] -= 1
        for i in t:
            alpha[ord(i) - 97] += 1
            
        for i in alpha:
            if i != 0:
                return False
            
        return True