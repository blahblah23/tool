









from observer import Observer




class Builda_Stacker:
    def __init__(self):
        super().__init__()

class Abstract_Stacker(Observer):
    def __init__(self, CHAMP, OWNER):
        super().__init__()
        self.CHAMP   = CHAMP
        self.OWNER   = OWNER
        self.counter = 0
    def reset(self):
        self.counter = 0
    def add(self, toAdd):
        self.counter += toAdd
    def note(self):
        self.add(1)

class CoX(Abstract_Stacker):
    def __init__(self, CHAMP, OWNER, MAX, ON_MAX):
        super().__init__(CHAMP, OWNER)
        self.MAX   = MAX
        self.ON_MAX = ON_MAX
    def add(self, toAdd):
        # self.counter += toAdd
        # TODO if counter maxxed, unsubscribe????
        self.counter = min(self.MAX, self.counter + toAdd)
        if self.counter >= self.MAX:
            self.ON_MAX[0](*self.ON_MAX[1])

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
# persist at max(akali R)

# C-call method
# X-max stacks
# R-reset stacks
# F-refresh duration
# D1-duration falloff 1 at a time
# D-duration
# DG-global duration (stacks dont matter)
# E-event
# S-stack
# # P-persist on max


# STOCK                   http://leagueoflegends.wikia.com/wiki/Stock
# C+RoX                   (alistar passive)
# CoS, RoD, FoE while X     (ezreal passive)
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

















