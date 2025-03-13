class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, result = 0, len(height) - 1, 0
        while i < j:
            breadth_of_container = j - i
            length_of_container = min(height[i], height[j])
            result = max(result, length_of_container * breadth_of_container)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return result

        