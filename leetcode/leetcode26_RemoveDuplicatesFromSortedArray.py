class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[fast], nums[slow] = nums[slow], nums[fast]

        return slow + 1
