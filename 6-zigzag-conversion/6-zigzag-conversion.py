class Solution:
    def convert(self, s: str, numRows: int) -> str:
        li = [''] * numRows
        ptr, is_going_backwards = 0, False
        for i, char in enumerate(s):
            li[ptr] += char
            is_going_backwards = is_going_backwards or (i == numRows) or (ptr == numRows - 1)
            ptr += -1 if is_going_backwards else 1    
            if ptr == -1:
                ptr = 1 if numRows > 1 else 0
                is_going_backwards = False
        return ''.join(li)