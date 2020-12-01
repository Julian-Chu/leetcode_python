class WebLogger:

    def __init__(self):
        self.queue = []

    """
    @param: timestamp: An integer
    @return: nothing
    """

    def hit(self, timestamp):
        self.queue.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """

    def get_hit_count_in_last_5_minutes(self, timestamp):
        if self.queue == []:
            return 0
        i = 0
        n = len(self.queue)
        while i < n and self.queue[i] + 300 <= timestamp:
            i += 1
        self.queue = self.queue[i:]
        return len(self.queue)
