class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        res_index = None
        res_len = len(res)

        for str in strs[1:]:
            i = 0
            str_len = len(str)

            while i < str_len and i < res_len and str[i] == res[i]:
                i += 1
            
            if i == 0:
                return ""
                
            if res_index is None or i < res_index:
                res_index = i

        return res[:res_index]
        