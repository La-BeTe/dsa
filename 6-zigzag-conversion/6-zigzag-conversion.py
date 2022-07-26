class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        li = [''] * numRows
        ptr, is_going_backwards = 0, False
        for i, char in enumerate(s):
            li[ptr] += char
            is_going_backwards = is_going_backwards or (ptr == numRows - 1)
            ptr += -1 if is_going_backwards else 1    
            if ptr == -1:
                ptr = 1
                is_going_backwards = False
        return ''.join(li)