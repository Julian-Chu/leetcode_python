class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0

        n = len(s)
        if k == 0:
            return 0
        max_length = 0
        for i in range(n):
            hashset = set([s[i]])
            j = i + 1
            while j < n:
                hashset.add(s[j])
                if len(hashset) > k:
                    break
                j += 1

            max_length = max(max_length, j - i)
            if j >= n:
                break

        return max_length


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or k == 0:
            return 0

        max_length = 0
        char_count = {}

        j = 0

        for i in range(len(s)):
            # if len(char_count) < k , keep searching next char
            # if s[j] in char_count,  keep searching next char, unit l find char not in char_count
            while j < len(s) and (len(char_count) < k or s[j] in char_count):
                if s[j] not in char_count:
                    char_count[s[j]] = 0
                char_count[s[j]] += 1
                j += 1

            max_length = max(max_length, j - i)

            if char_count[s[i]] > 1:
                char_count[s[i]] -= 1
            else:
                del char_count[s[i]]

        return max_length


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or k == 0:
            return 0

        max_length = 0
        counter = {}
        left = 0
        for right in range(len(s)):
            if s[right] not in counter:
                counter[s[right]] = 0
            counter[s[right]] += 1
            while left <= right and len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length


