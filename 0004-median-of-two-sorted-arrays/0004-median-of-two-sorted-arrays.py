class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        total_list_size_is_odd = (nums1_length + nums2_length) % 2 != 0
        index_to_end_at = int(math.floor((nums1_length + nums2_length) / 2) if total_list_size_is_odd else (nums1_length + nums2_length) / 2)
        
        i, j, k, longer_list, shorter_list, longer_list_length, shorter_list_length, median_sum = 0, 0, 0, [], [], 0, 0, 0
        if nums1_length >= nums2_length:
            longer_list = nums1
            shorter_list = nums2
            longer_list_length = nums1_length
            shorter_list_length = nums2_length
        else:
            longer_list = nums2
            shorter_list = nums1
            longer_list_length = nums2_length
            shorter_list_length = nums1_length

        while k <= index_to_end_at:
            num = 0
            if i >= longer_list_length:
                num = shorter_list[j]
                j = j + 1
            elif j >= shorter_list_length:
                num = longer_list[i]
                i = i + 1
            elif longer_list[i] <= shorter_list[j]:
                num = longer_list[i]
                i = i + 1
            else:
                num = shorter_list[j]
                j = j + 1

            if total_list_size_is_odd and k == index_to_end_at:
                return num
            if not total_list_size_is_odd and k >= index_to_end_at - 1:
                median_sum += num

            k = k + 1
            
        return median_sum / 2
        