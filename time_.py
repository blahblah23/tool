







from globals_ import *
import helpers


class Time:

    def __init__(self):
        # self.pr_t = []
        # self.pr_msg = []
        self.prev_num = 0
        self.prev_t = 0
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
    def printall(self):

        temp = self.pr_t[:]
    
        for num in set(self.pr_t):
            if isinstance(num, float):
                if round(num) not in temp:
                    temp = [round(x) if x == num else x for x in temp]
                    pass
                # TODO elif round(num) in temp: do nothing 

        for idx, time in enumerate(temp):
            print('{:9}{}'.format(str(time) + ':', self.pr_msg[idx]))




class Timer:
    def __init__(self, name, length, method, args=[], persist=False):
        self.name = name
        self.length = length
        self.method = method
        self.args = args
        self.persist = persist
        self.start = None
    def __repr__(self):
        return '{}-timer'.format(self.name)
    def go(self):
        self.pr('start ')
        self.start = self.time.t
        self.time.timers.add(self)
    def stop(self):
        self.time.timers.discard(self)
        # discard from set does nothing if the element isnt there
    # def pr(self, x=''):
    #     t = self.time.t
    #     msg = '{:6}{}'.format(x, self.name)

    #     self.time.pr_t.append(t)
    #     self.time.pr_msg.append(msg)
        
    #     pass
    def pr(self, x=''):
        num = self.time.t


        if isinstance(num, float):
            if isinstance(self.time.prev_t, float):
                if num != self.time.prev_t:
                    helpers.round_recurse(num, self.time.prev_num)
                pass
            num = round(num)



        msg = '{:<9}{:9}{:20}{}'.format(num, x, self.name[0], self.name[1])
        # msg = '{:<20}{:6}{}'.format(num, x, self.name)
        print(msg)

        self.time.prev_t = self.time.t
        self.time.prev_num = num


    def call(self):
        self.pr('end ')
        self.method(*self.args)
        if not self.persist:
            self.stop()
    @property
    def end(self):
        end = self.start + self.length
        if end < self.time.t:
            end = self.time.t
            # TODO bug where 2 things get set to the same time 
        return end










