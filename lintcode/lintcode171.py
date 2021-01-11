def anagrams(self, strs):
    hashmap = {}

    for string in strs:
        string = ''.join(sorted(string))
        hashmap[string] = hashmap.get(string, 0) + 1

    result = []
    for string in strs:
        sortedString = ''.join(sorted(string))
        if sortedString in hashmap and hashmap[sortedString] > 1:
            result.append(string)
    return result


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        words_dict = {}
        key_to_dict = {}

        for word in strs:
            word_dict = {}
            for c in word:
                word_dict[c] = word_dict.get(c, 0) + 1

            is_found = False
            for key in key_to_dict:
                if key_to_dict[key] == word_dict:
                    is_found = True
                    words_dict[key].append(word)
                    break
            if not is_found:
                key_to_dict[word] = word_dict
                words_dict[word] = [word]

        results = []

        for key in words_dict:
            if len(words_dict[key]) < 2:
                continue
            for word in words_dict[key]:
                results.append(word)
        return results