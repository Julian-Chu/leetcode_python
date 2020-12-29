class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, str):
        if not str or not pattern:
            return False
        return self.dfs(str, 0, pattern, 0, {}, {})

    def dfs(self, str, str_index, pattern, pattern_index, dic, word_to_pattern):
        if pattern_index == len(pattern):
            return True

        if pattern[pattern_index] in dic:
            # remove words from str
            word = dic[pattern[pattern_index]]
            if str[str_index:str_index + len(word)] == word:
                if self.dfs(str, str_index + len(word), pattern, pattern_index + 1, dic, word_to_pattern):
                    return True
            return False

        for i in range(str_index + 1, len(str) + 1):
            word = str[str_index:i]
            if word in word_to_pattern:
                continue
            dic[pattern[pattern_index]] = word
            word_to_pattern[word] = pattern[pattern_index]
            if self.dfs(str, i, pattern, pattern_index + 1, dic, word_to_pattern):
                return True
            del dic[pattern[pattern_index]]
            del word_to_pattern[word]
        return False


class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, str):
        return self.is_match(pattern, str, {}, set())

    def is_match(self, pattern, string, mapping, used):
        if not pattern:
            return not string

        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            return self.is_match(pattern[1:], string[len(word):], mapping, used)

        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:
                continue

            used.add(word)
            mapping[char] = word
            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True

            del mapping[char]
            used.remove(word)

        return False