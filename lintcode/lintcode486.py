class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        import heapq
        if not arrays:
            return []
        if len(arrays) == 1:
            return arrays[0]

        heap = []
        heapq.heapify(heap)

        result = []
        for arr in arrays:
            for element in arr:
                heapq.heappush(heap, element)

        while len(heap) > 0:
            result.append(heapq.heappop(heap))

        return result


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.push(heap, (array[0], index, 0))

        while len(heap):
            val, x, y = heap[0]
            heapq.heappop(heap)
            if y + 1 < len(arrays[x]):
                heapq.push(heap, (arrays[x][y + 1], x, y + 1))


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        return self.merge_range_arrays(arrays, 0, len(arrays) - 1)

    def merge_range_arrays(self, arrays, start, end):
        if start == end:
            return arrays[start]

        mid = (start + end) // 2
        left = self.merge_range_arrays(arrays, start, mid)
        right = self.merge_range_arrays(arrays, mid + 1, end)
        return self.merge_two_arrays(left, right)

    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1

        while i < len(arr1):
            array.append(arr1[i])
            i += 1

        while j < len(arr2):
            array.append(arr2[j])
            j += 1

        return array