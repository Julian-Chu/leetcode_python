class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        result = 1

        for i in range(1, len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])

        return result

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                idx = self.binarySearch(sub, num)
                sub[idx] = num

        return len(sub)

    def binarySearch(self, sub: List[int], num: int) -> int:
        left, right = 0, len(sub)-1

        while left+1<right:
            mid = (right+left)//2
            if sub[mid] == num:
                return mid
            elif sub[mid] > num:
                right = mid
            else:
                left = mid
        if sub[left] >= num:
            return left
        return right

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num

        return len(sub)