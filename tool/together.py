









def foo():
    print('foo')
def handle_time(*args):
    Timer(*args)
class IAuto:
    def auto_start(self):
        self.auto_component.auto_start()

class Time:
    def __init__(self):
        self.t = 0
        self.timer_registry = set()
    def nx(self):
        x = {timer.end: timer for timer in self.timer_registry}
      # x = {obj.var: obj for obj in somelist}
        return x[min(x.keys())]
    def go(self):
        while self.timer_registry:
            nx = self.nx()
            self.t = nx.end
            nx.call()
            nx.kill()
class Timer:
    def __init__(self, name, length, method, args=[]):
        self.start = t.t
        self.name = name
        self.length = length    #depends on attack speed or other things
        self.method = method
        self.args = args
        self.end = t.t + length
        t.timer_registry.add(self)
    def __repr__(self):
        return '{}-timer'.format(self.name)
    def kill(self):
        t.timer_registry.discard(self)
    def get_length(self):
        return self.length
    def update_length(self, diff):
        self.length += diff
        self.end += diff
    def call(self):
        self.method(*self.args)

class Auto:
    def __init__(self, owner):
        self.owner = owner
    def auto_start(self):
        handle_time('windup', 10, foo)
        self.owner.change_state(State_Casting)
        # notify__auto_start()
        pass

class Vayne:
    def __init__(self):
        # self.state_component = StateMachine()
        self.auto_component = Auto(self)
    def __getattr__(self, attr):
        if attr[0:4] == 'auto':
            return getattr(self.auto_component, attr)
        if attr == 'change_state':
            return getattr(self.state_component, attr)












