
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


def convertIntsToStrs():
    arr = [i for i in range(3)]

    strs = [str(i) for i in arr]

def reverse():
    s = [1,2,3]
    rev = s[::-1]


def twoDArray():
    matrix = [[0]*5 for i in range(5)]