class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums2.sort()
        intersect = set()

        for num in nums1:
            if num in intersect:
                continue

            if self.binary_serach(nums2, num) != -1:
                intersect.add(num)

        return list(intersect)

    def binary_serach(self, nums, num):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < num:
                start = mid
            elif nums[mid] > num:
                end = mid
            else:
                return mid

        if nums[start] == num:
            return start
        if nums[end] == num:
            return end
        return -1

    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))

    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        result = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if len(result) == 0 or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1

        return result
