def quicksort(self, strs, start, end):
    if start >= end:
        return

    l, r = start, end

    pivot = strs[(start + end) // 2]
    while l <= r:
        while l <= r and strs[l] < pivot:
            l += 1
        while l <= r and strs[r] > pivot:
            r -= 1

        if l <= r:
            strs[l], strs[r] = strs[r], strs[l]
            l, r = l + 1, r - 1

    self.quicksort(strs, start, r)
    self.quicksort(strs, l, end)
