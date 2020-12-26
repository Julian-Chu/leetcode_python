"""
offline
"""
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

"""
online
"""
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

    def mergekSortedArrays(self, arrays):
        if not arrays:
            return []

        heap = []

        for i in range(len(arrays)):
            if len(arrays[i]) == 0:
                continue
            heapq.heappush(heap, (arrays[i][0], i, 0))

        res = []
        while heap:
            (num, arrs_index, arr_index) = heapq.heappop(heap)
            res.append(num)
            if arr_index + 1 < len(arrays[arrs_index]):
                arr_index += 1
                heapq.heappush(heap, (arrays[arrs_index][arr_index], arrs_index, arr_index))

        return res


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




class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        if not arrays:
            return []
        while len(arrays) > 1:
            next_arrays = []
            for i in range(0, len(arrays), 2):
                if i + 1 < len(arrays):
                    arr = self.merge(arrays[i], arrays[i + 1])
                    next_arrays.append(arr)
                else:
                    next_arrays.append(arrays[i])
            arrays = next_arrays

        return arrays[0]

    def merge(self, arr1, arr2):
        arr = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                arr.append(arr2[j])
                j += 1
            else:
                arr.append(arr1[i])
                i += 1
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1
        while j < len(arr2):
            arr.append(arr2[j])
            j += 1
        return arr