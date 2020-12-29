"""
class HtmlHelper:
    # @param (string)
    # @return (list)
    @classmethod
    def parseUrls(url):
        # Get all urls from a webpage of given url.
"""
from collections import deque
import re


class Solution:
    def __init__(self):
        pattern = "(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]wikipedia+)\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?"

        self.prog = re.compile(pattern)

    """
    @param url(string): a url of root page
    @return (list): all urls
    """

    def crawler(self, url):

        visited = set()
        queue = deque([url])

        while queue:
            url = queue.popleft()

            if url in visited:
                continue

            if not self.prog.match(url):
                continue

            visited.add(url)
            next_urls = HtmlHelper.parseUrls(url)
            for next_url in next_urls:
                queue.append(next_url)
        return list(visited)