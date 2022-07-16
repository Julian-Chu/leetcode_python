
def arr(n):
    arrInit = [0] * n

def copy1(nums):
    arr = [0] * len(nums)
    for i in range(len(nums)):
        arr[i] = nums[i]
    return arr

def copy2(nums):
    arr = [x for x in nums]
    return arr