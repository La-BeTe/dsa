class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, result = 0, len(height) - 1, 0
        while i < j:
            length_of_container, breadth_of_container = 0, j - i
            if height[i] > height[j]:
                length_of_container = height[j]
                j -= 1
            else:
                length_of_container = height[i]
                i += 1
            result = max(result, length_of_container * breadth_of_container)
        return result

        