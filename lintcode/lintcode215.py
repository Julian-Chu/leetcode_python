class Solution:

    def __init__(self):
        self.events = {}
        self.timeToSecond = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 3600 * 24
        }

    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """

    def isRatelimited(self, timestamp, event, rate, increment):
        if event not in self.events:
            if increment:
                self.events[event] = [timestamp]
            return False

        rateList = rate.split('/')
        times = int(rateList[0])
        seconds = self.timeToSecond[rateList[1]]

        event_queue = self.events[event]
        if len(event_queue) < times:
            if increment:
                event_queue.append(timestamp)
            return False

        ts = event_queue[-times]
        if ts + seconds > timestamp:
            return True

        if increment:
            event_queue.append(timestamp)
            while len(event_queue) > 100:
                event_queue.pop(0)
        return False








