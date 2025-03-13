class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        if nums1_length < nums2_length:
            [nums1, nums2] = [nums2, nums1]
            [nums1_length, nums2_length] = [nums2_length, nums1_length]

        i, j, k, median_sum = 0, 0, 0, 0
        index_to_end_at = (nums1_length + nums2_length) // 2
        total_list_size_is_odd = (nums1_length + nums2_length) % 2 != 0
        
        while k <= index_to_end_at:
            num = 0
            if i >= nums1_length:
                num = nums2[j]
                j += 1
            elif j >= nums2_length:
                num = nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                num = nums1[i]
                i += 1
            else:
                num = nums2[j]
                j += 1

            if total_list_size_is_odd and k == index_to_end_at:
                return num
            if not total_list_size_is_odd and k >= index_to_end_at - 1:
                median_sum += num

            k += 1
            
        return median_sum / 2
        