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
                    is_num = ord(char) >= 48 and ord(char) <= 57
                    if is_num:
                        num += int(char)
                    else:
                        break
            else:    
                is_num = ord(char) >= 48 and ord(char) <= 57
                if is_num:
                    num = (num * 10) + int(char)
                else:
                    break
        return min(limit, num) * sign