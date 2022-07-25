class Solution:
    def convert(self, s: str, numRows: int) -> str:
        li = []
        ptr = 0
        is_going_backwards = False
        for i in range(numRows):
            li.append([])
        for i, char in enumerate(s):
            li[ptr].append(char)
            if (i == numRows) or (ptr == numRows - 1):
                ptr -= 1
                is_going_backwards = True
            elif is_going_backwards:
                ptr -= 1
            else:
                ptr += 1
            if ptr == -1:
                ptr = 1 if len(li) > 1 else 0
                is_going_backwards = False
        result = ''
        for row in li:
            result += ''.join(row)
        return result
            