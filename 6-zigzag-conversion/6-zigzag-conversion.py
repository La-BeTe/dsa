class Solution:
    def convert(self, s: str, numRows: int) -> str:
        li = ['' for _ in range(numRows)]
        ptr = 0
        is_going_backwards = False
        for i, char in enumerate(s):
            li[ptr] += char
            if (i == numRows) or (ptr == numRows - 1) or is_going_backwards:
                ptr -= 1
                is_going_backwards = True
            else:
                ptr += 1
            if ptr == -1:
                ptr = 1 if numRows > 1 else 0
                is_going_backwards = False
        return ''.join(li)