










class Time:
    def __init__(self):
        self.t = 0
        self.timers = set()
    def nx(self):
        x = {timer.end: timer for timer in self.timers}
        return x[min(x.keys())]
    def go(self):
        while self.timers:
            nx = self.nx()
            self.t = nx.end
            nx.call()
            nx.stop()


class Timer:
    def __init__(self, name, length, method, args=[]):
        self.start = t.t
        self.name = name
        self.length = length    #depends on attack speed or other things
        self.method = method
        self.args = args
        self.end = t.t + length
    def __repr__(self):
        return '{}-timer'.format(self.name)
    def go(self):
        t.timers.add(self)
    def stop(self):
        t.timers.discard(self)
    def update_length(self, diff):
        self.length += diff
        self.end += diff
    def call(self):
        self.method(*self.args)


class Store:
    pass













