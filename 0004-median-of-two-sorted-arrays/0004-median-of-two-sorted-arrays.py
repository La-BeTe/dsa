class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_list_size = len(nums1) + len(nums2)
        index_to_end_at = int(math.floor(total_list_size / 2) if total_list_size % 2 != 0 else total_list_size / 2)
        i, j, k = 0, 0, 0
        longer_list = nums1 if len(nums1) >= len(nums2) else nums2
        shorter_list = nums1 if len(nums1) < len(nums2) else nums2
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

            print(index_to_end_at, k, li)
            if total_list_size % 2 != 0 and k == index_to_end_at:
                li.append(num)
            if total_list_size % 2 == 0 and k >= index_to_end_at - 1:
                li.append(num)

            k = k + 1

        print(index_to_end_at, li)
            
        return li[-1] if len(li) == 1 else (li[-1] + li[-2]) / 2
        