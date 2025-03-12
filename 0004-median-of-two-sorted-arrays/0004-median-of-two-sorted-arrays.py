class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        total_list_size = nums1_length + nums2_length
        total_list_size_is_odd = total_list_size % 2 != 0
        index_to_end_at = int(math.floor(total_list_size / 2) if total_list_size_is_odd else total_list_size / 2)
        i, j, k = 0, 0, 0
        longer_list = nums1 if nums1_length >= nums2_length else nums2
        shorter_list = nums1 if nums1_length < nums2_length else nums2
        li = []

        while k <= index_to_end_at:
            num = 0
            if i >= len(longer_list):
                num = shorter_list[j]
                j = j + 1
            elif j >= len(shorter_list):
                num = longer_list[i]
                i = i + 1
            elif longer_list[i] <= shorter_list[j]:
                num = longer_list[i]
                i = i + 1
            else:
                num = shorter_list[j]
                j = j + 1

            if total_list_size_is_odd and k == index_to_end_at:
                li.append(num)
            if not total_list_size_is_odd and k >= index_to_end_at - 1:
                li.append(num)

            k = k + 1
            
        return li[-1] if len(li) == 1 else (li[-1] + li[-2]) / 2
        