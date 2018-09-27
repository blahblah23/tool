







from globals_ import *


class Time:
    def __init__(self):
        self.t = 0
        self.timers = set()
        Timer.time = self
    def nx(self):
        '''return soonest timer in the set'''
        x = {timer.end: timer for timer in self.timers}
        return x[min(x.keys())]
    def go(self):
        while self.timers:
            nx = self.nx()
            self.t = nx.end
            nx.call()
            # nx.stop()
            # removing the timer after the call prevents it from re-adding itself
            if self.t >= 120000:
                break
    
    # def __repr__(self):
    #     return str(self.timers)


class Timer:
    def __init__(self, name, intent, length, method, args=[], persist=False):
        self.name = name
        self.intent = intent
        self.length = length #depends on ats or other things
        self.method = method
        self.args = args
        self.start = None
        self.end = None
        self.persist = persist
    def __repr__(self):
        return '{}-timer'.format(self.name)
    def go(self):
        print('{:9}start {}'.format(str(self.time.t) + ':', self.name))
        self.reset()
        self.time.timers.add(self)
    def stop(self):
        self.time.timers.discard(self)
    def update_length(self, diff):
        self.length += diff
        self.end += diff
    def call(self):
        print('{:9}{}'.format(str(self.time.t) + ':', self.intent))
        self.method(*self.args)
        if not self.persist:
            self.stop()
    def reset(self):
        self.start = self.time.t
        self.end   = self.time.t + self.length











