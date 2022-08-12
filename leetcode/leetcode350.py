class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        counts = [0] * 1001

        for num in nums1:
            counts[num] += 1

        res = []

        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res
