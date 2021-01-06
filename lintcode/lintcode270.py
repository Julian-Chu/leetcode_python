class Solution:
    def __init__(self):
        word_dict = {
            "abc": "2",
            "def": "3",
            "ghi": "4",
            "jkl": "5",
            "mno": "6",
            "pqrs": "7",
            "tuv": "8",
            "wxyz": "9",
        }

        self.prefix_dict = {}

        for letters in word_dict:
            num = word_dict[letters]
            for i in range(len(letters)):
                self.prefix_dict[letters[i]] = num

    """
    @param queries: the queries
    @param dict: the words
    @return: return the queries' answer
    """

    def letterCombinationsII(self, queries, dict):
        result_dict = {}
        for num in queries:
            result_dict[num] = 0
        for letters in dict:
            digits = ""
            for i in range(len(letters)):
                digits += self.prefix_dict[letters[i]]
                if digits in result_dict:
                    result_dict[digits] += 1
        result = []

        for num in queries:
            result.append(result_dict[num])
        return result