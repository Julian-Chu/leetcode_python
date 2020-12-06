class HeartBeat:

    def __init__(self):
        self.slaves_heartbeat = {}
        self.timeout = 0

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """

    def initialize(self, slaves_ip_list, k):
        for slave_ip in slaves_ip_list:
            self.slaves_heartbeat[slave_ip] = 0

        self.timeout = 2 * k

    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """

    def ping(self, timestamp, slave_ip):
        if slave_ip not in self.slaves_heartbeat:
            return
        self.slaves_heartbeat[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """

    def getDiedSlaves(self, timestamp):
        died = []
        for slave in self.slaves_heartbeat:
            heartbeat = self.slaves_heartbeat[slave]
            if timestamp - heartbeat >= self.timeout:
                died.append(slave)

        return died