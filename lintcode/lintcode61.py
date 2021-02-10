class Solution:
  """
  @param A: an integer sorted array
  @param target: an integer to be inserted
  @return: a list of length 2, [index1, index2]
  """

  def searchRange(self, A, target):
    if not A:
      return [-1, -1]

    start = self.find_first_target_index(A, target)
    if start == -1:
      return [-1, -1]

    end = self.find_last_target_index(A, start, target)
    return [start, end]

  def find_first_target_index(self, A, target):
    start, end = 0, len(A) - 1

    while start + 1 < end:
      mid = (start + end) // 2
      if A[mid] >= target:
        end = mid
      else:
        start = mid

    if A[start] == target:
      return start
    if A[end] == target:
      return end
    return -1

  def find_last_target_index(self, A, start, target):
    start, end = start, len(A) - 1

    while start + 1 < end:
      mid = (start + end) // 2
      if A[mid] > target:
        end = mid
      else:
        start = mid

    if A[end] == target:
      return end
    if A[start] == target:
      return start
    return -1


class Solution:
  def searchRange(self, A, target):
    start = bisect.bisect_left(A, target)
    return [-1, -1] if start == len(A) or A[start] != target else [start, bisect.bisect_right(A, target) - 1]