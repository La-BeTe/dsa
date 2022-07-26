class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1) or (len(s) <= numRows):
            return s
        li = [[] for _ in range(numRows)]
        ptr, is_going_backwards = 0, False
        for char in s:
            li[ptr].append(char)
            is_going_backwards = (is_going_backwards or (ptr == numRows - 1)) and ptr != 0
            ptr += -1 if is_going_backwards else 1  
        return ''.join([''.join(_) for _ in li])