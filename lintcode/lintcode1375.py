class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        left = 0
        counter = {}
        answer = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while left <= right and len(counter) >= k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            if len(counter) == k - 1 and left > 0 and s[left - 1] not in counter:
                # abcabc , when r =2, left =1, 以r為結尾的substring有left個
                answer += left

        return answer

    def kDistinctCharacters(self, s, k):
        ans =0
        for i in range(len(s)):
            chars = {}
            for j in range(i, len(s)):
              chars[s[j]] = chars.get(s[j],0) + 1
              if len(chars) >= k:
                  # how many steps slide window can move
                  ans+= len(s) - j
                  break
        return ans

    def kDistinctCharacters(self, s, k):
        left = 0
        counter = {}
        answer = 0

        # import => at least!
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while left <= right and len(counter) >= k:
                # 以l為長度的且滿足至少k個char的substring有len(s)-r個
                # how many steps window can move
                answer += len(s) - right
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1

        return answer