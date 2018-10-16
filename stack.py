









from globals_ import *
from observer import Observer
import time_






class Abstract_Stacker(Observer, KnowsCHAMP, KnowsOWNER):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._counter = 0
    @property
    def counter(self):
        return self._counter
    def reset(self):
        self.counter = 0
    def add(self, toAdd):
        self.counter += toAdd
    def note(self):
        self.add(1)
        # TODO if counter maxxed, unsubscribe????
        # so that it doesnt keep getting notified once at max 
        # doesnt seem necessary


class Max(Abstract_Stacker):
    def __init__(self, MAX, **kwargs):
        super().__init__(**kwargs)
        self.MAX = MAX

    @Abstract_Stacker.counter.setter
    def counter(self, count):
        self._counter = min(self.MAX, count)

class Dur(Abstract_Stacker):
    def __init__(self, length, **kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.duration = time_.Timer(name   = ['stacks-duration', str(self.CHAMP)], 
                                    length = self.length, 
                                    method = self.drop_stack)
    def drop_stack(self):
        self.OWNER.drop_stack()
        self.reset()
        self.duration.stop()

class DurMax(Dur, Max):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)




class Yasuo_flow(Max, Abstract_Stacker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Yasuo_Q(DurMax, Abstract_Stacker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)





class CoX(Max, Abstract_Stacker):
    def __init__(self, on_max, **kwargs):
        super().__init__(**kwargs)
        self.on_max = on_max
    @Abstract_Stacker.counter.setter
    def counter(self, count):
        self._counter = min(self.MAX, count)
        if self._counter >= self.MAX:
            self.on_max[0](*self.on_max[1])




if __name__ == '__main__':
    a = Abstract_Stacker(None, None)
    b = CoX(None, None, 6, None)
    # print(a.__class__.__dict__)
    # print(dir(Abstract_Stacker.counter))
    print(Abstract_Stacker.counter.fset)
    print(CoX.counter.fset)












class Builda_Stacker:
    def __init__(self):
        super().__init__()
class Stacker(Observer):
    def __init__(self, CHAMP, OWNER, MAX, ON_MAX):
        super().__init__()
        self.CHAMP   = CHAMP
        self.OWNER   = OWNER
        self.MAX     = MAX
        self.ON_MAX  = ON_MAX
        self.counter = 0
    def reset(self):
        self.counter = 0
    def add(self, toAdd):
        self.counter += toAdd
    def callOnMax(self):
        self.ON_MAX[0](*self.ON_MAX[1])
    def note(self):
        self.add(1)
        if self.counter >= self.MAX:
            self.callOnMax()





# FO-fall off
# PTS-persist through all stacks
# D- duration
# CAOM-call arg on max
# ROE-reset on event
# ROM-reset on max

# CAOM ROM,  (alistar passive)
# D, update buff every stack, refresh at max same trigger (ezreal passive)
# call arg on 2nd, ROM (aatrox W)
# FO D, CAOM ROM (ahri passive)
# CAOM, ROE(ahri Q)
# FO PTS D, CAOM, ROE(alistar E)
# CAOM or on FO D PTS(ahri R)

# C-call method
# X-max stacks
# R-reset stacks
# F-refresh duration
# D1-duration falloff 1 at a time
# D-duration
# DG-global duration (stacks dont matter)
# E-event
# S-stack
# P-persist on max

# STOCK                   http://leagueoflegends.wikia.com/wiki/Stock
# C+RoX                   (alistar passive)
# CoS, RoD, FoE while X   (ezreal passive)
# Co2S, RoX               (aatrox W)
# C+RoX, RoD1orALL        (ahri passive)
# CoX, RoE                (ahri Q, annie passive)
# CoX or CoDG             (ahri R)
# CoX, RoDG, RoE          (alistar E)
# CoX, CoD, CoD1 from X, RoE      (ashe Q)
# BARD
# brand
# braum
# caitlyn
# maybe camille

















