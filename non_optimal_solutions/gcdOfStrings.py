class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_str = str1 if len(str1) < len(str2) else str2
        
        max_substr = ""
        for end in range(1,len(min_str)+1):
            substr = min_str[:end]
            if not len(str1) % len(substr) and not len(str2) % len(substr):
                str1_cmp = substr*(len(str1) // len(substr))
                if str1_cmp != str1:
                    continue
                
                str2_cmp = substr*(len(str2) // len(substr))
                if str2_cmp != str2:
                    continue
                    
                max_substr = substr
    
        return max_substr

# O(n^2) time, O(n) space, where n is the longest of str1, str2
