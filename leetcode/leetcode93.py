class Solution:
    def __init__(self):
        self.ips = []
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        self.dfs(s, 0)
        return self.res

    def dfs(self, s: str, start_index: int):
        if start_index == len(s) and len(self.ips) == 4:
            self.res.append('.'.join(self.ips[:]))
            return

        if start_index >= len(s) or len(self.ips) >= 4:
            return

        for end in range(start_index, start_index + 3):
            ip_str = s[start_index:end + 1]
            if not self.isValidIP(ip_str):
                return

            self.ips.append(ip_str)
            self.dfs(s, end + 1)
            self.ips.pop()
        return

    def isValidIP(self, ip: str):
        if not ip:
            return False

        if len(ip) > 1 and ip[0] == '0':
            return False

        if int(ip) > 255:
            return False

        return True