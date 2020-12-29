class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """

    def restoreIpAddresses(self, s):
        if not s or len(s) < 4:
            return []

        IPs = []
        self.dfs(s, 0, [], IPs)
        return IPs

    def dfs(self, s, index, IPstr, IPs):
        if len(IPstr) > 4:
            return
        if index >= len(s):
            if len(IPstr) == 4:
                IPs.append('.'.join(IPstr))
            return

        for l in range(1, 4):
            if index + l > len(s):
                break
            numStr = s[index:index + l]
            num = int(numStr)
            if num > 255:
                break
            IPstr.append(numStr)
            self.dfs(s, index + l, IPstr, IPs)
            IPstr.pop()
            if s[index] == '0':
                break


class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """

    def restoreIpAddresses(self, s):
        if not s or len(s) < 4:
            return []

        ips = []
        self.dfs(s, 0, "", ips)
        return ips

    def dfs(self, s, sub, ip, ips):
        if sub > 4:
            return
        if sub == 4:
            if s == "":
                ips.append(ip[1:])
            return

        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], sub + 1, ip + '.' + s[:i], ips)
                if s[0] == '0':  # avoid 00 000 000
                    break