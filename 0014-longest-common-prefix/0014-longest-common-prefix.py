class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for str in strs[1:]:
            i = 0
            new_res = ""
            str_len = len(str)
            res_len = len(res)
            while i < str_len and i < res_len and str[i] == res[i]:
                i += 1
                new_res = str[:i]
            res = new_res
        return res
        