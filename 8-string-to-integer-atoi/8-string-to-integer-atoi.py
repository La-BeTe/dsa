class Solution:
    def myAtoi(self, s: str) -> int:
        sign = num = 0
        limit = (2 ** 31) - 1
        
        for char in s:
            if sign == 0:
                if char == ' ':
                    continue
                elif char == '-':
                    sign = -1
                    limit += 1
                elif char == '+':
                    sign = 1
                else:
                    sign = 1
                    if (47 < ord(char) < 58):
                        num += int(char)
                    else:
                        break
            else:
                if (47 < ord(char) < 58):
                    num = (num * 10) + int(char)
                else:
                    break
        return min(num, limit) * sign