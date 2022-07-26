class Solution:
    def convert(self, s: str, numRows: int) -> str:
        li = [''] * numRows
        ptr, is_going_backwards = 0, False
        for i, char in enumerate(s):
            li[ptr] += char
            if (i == numRows) or (ptr == numRows - 1):
                is_going_backwards = True
                
            ptr += -1 if is_going_backwards else 1
                
            if ptr == -1:
                ptr = 1 if numRows > 1 else 0
                is_going_backwards = False
        return ''.join(li)