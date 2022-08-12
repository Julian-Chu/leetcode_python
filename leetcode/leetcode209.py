class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        _sum = 0
        res = 10 ** 5 + 1
        for i in range(len(nums)):
            _sum += nums[i]

            while _sum >= target:
                _len = i - slow + 1
                if _len < res:
                    res = _len

                _sum -= nums[slow]
                slow += 1

        if res > 10 ** 5:
            return 0

        return res