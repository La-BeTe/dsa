class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1) or (len(s) <= numRows):
            return s
        li = [''] * numRows
        ptr, is_going_backwards = 0, False
        for char in s:
            li[ptr] += char
            is_going_backwards = ptr != 0 and (is_going_backwards or (ptr == numRows - 1)) 
            ptr += -1 if is_going_backwards else 1  
        return ''.join(li)