"""
@param pages: an array of integers
@param k: An integer
@return: an integer
"""


def copyBooks(self, pages, k):
    # write your code here
    if not pages:
        return 0

    if k > len(pages):
        k = len(pages)
    start, end = 0, sum(pages)
    while start + 1 < end:
        mid = (start + end) // 2
        print(start, end, mid, self.get_copiers(pages, mid))
        if self.get_copiers(pages, mid) > k:
            start = mid
        else:
            end = mid

    if self.get_copiers(pages, start) <= k:
        return start
    return end


def get_copiers(self, pages, time):
    copiers = 0
    last_copied = time
    for page in pages:
        if page > time:
            return float('inf')

        if last_copied + page > time:
            copiers += 1
            last_copied = page
        else:
            last_copied += page

    return copiers