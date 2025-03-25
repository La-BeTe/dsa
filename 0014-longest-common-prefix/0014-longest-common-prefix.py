class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        res_index = None
        res_len = len(res)

        for str in strs[1:]:
            str_len = len(str)
            i, new_res_index = 0, 0

            while i < str_len and i < res_len and str[i] == res[i]:
                i += 1
                new_res_index = i
                
            if res_index is None or new_res_index < res_index:
                res_index = new_res_index
            
            if res_index == 0:
                return ""

        return res[:res_index]
        