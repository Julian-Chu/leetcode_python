class Solution:
    """
    @param array: an integer array
    @return: nothing
    """

    def pancakeSort(self, array):

        for i in range(len(array) - 1, -1, -1):
            max_index = 0
            for j in range(0, i + 1):
                if array[j] > array[max_index]:
                    max_index = j
            if max_index == i:
                continue
            FlipTool.flip(array, max_index)
            FlipTool.flip(array, i)
