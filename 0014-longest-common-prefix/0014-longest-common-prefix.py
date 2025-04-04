class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        res_len = len(res)
        res_index = res_len

        for str in strs[1:]:
            i = 0
            str_len = len(str)

            if str[:res_index] == res[:res_index]:
                continue
            
            if res[:str_len] == str:
                if str_len < res_index:
                    res_index = str_len
                continue

            while i < str_len and i < res_len and str[i] == res[i]:
                i += 1
            
            if i == 0:
                return ""
                
            if i < res_index:
                res_index = i

        return res[:res_index]
        