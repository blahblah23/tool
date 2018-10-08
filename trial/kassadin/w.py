




from globals_ import *
import cooldown
import time_
from dmgheal import MDmg


class W(ABS_W):

    cost = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.CD = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                    OWNER  = self,
                                    # name   = '{:15}{}.W'.format('cd-refresh', str(self.CHAMP)), 
                                    name   = ['cd-refresh', str(self.CHAMP) + '.W'], 
                                    length = 7000) 
        # self.duration = time_.Timer(name   = '{:15}{}.W'.format('buff-duration', str(self.CHAMP)), 
        self.duration = time_.Timer(name   = ['buff-duration', str(self.CHAMP) + '.W'], 
                                    length = 5500, 
                                    method = self.buff_active,
                                    args   = [False])

        self._passive_mdmg = MDmg(CHAMP  = self.CHAMP, 
                                  OWNER  = self, 
                                  target = None,
                                  amount = None, 
                                  tags   = ['ability'])
        self._active_mdmg = MDmg(CHAMP  = self.CHAMP, 
                                 OWNER  = self, 
                                 target = None,
                                 amount = None, 
                                 tags   = ['ability'])
        if self.lvl > 0:
            self.CHAMP.AUTO.on_land.append(self.passive_mdmg.apply)


    def cast(self):
        self.CHAMP.AUTO.reset()
        self.CHAMP.current_mp -= self.cost
        self.duration.go()
        self.buff_active(True)

    def active_apply(self):
        self.active_mdmg.apply()
        self.duration.call()
        self.CD.trigger()

    def buff_active(self, value):
        onlands = self.CHAMP.AUTO.on_land
        passive = self.passive_mdmg.apply
        active  = self.active_apply
        print('before:', onlands)
        if value:
            assert onlands.count(passive) == 1
            onlands.remove(passive)
            assert active not in onlands
            onlands.append(active)
        elif not value:
            try:onlands.remove(active)
            except ValueError: pass
            assert active not in onlands
            onlands.append(passive)
            assert onlands.count(passive) == 1
        print('after:', onlands)

    @property
    def passive_mdmg(self):
        self._passive_mdmg.target = self.CHAMP.target
        self._passive_mdmg.amount = 20 + 0.1 * self.CHAMP.ap
        return self._passive_mdmg
    @property
    def active_mdmg(self):
        self._active_mdmg.target = self.CHAMP.target
        self._active_mdmg.amount = 40 + 25 * self.lvlups + 0.8 * self.CHAMP.ap
        return self._active_mdmg





# W
# cd: 7 
# cost 1 mana??????
# passive: selfs autos do ++ mDmg
    # mDmg: '20' (+ 10% ap)
# active: selfs next auto give 50 ++ range, do incrd ++ mDmg, restores mana
    # mDmg: '40+25.0&5' (+ 80% ap)
    # mana restored: '4+1.0&5'% of missing mana........x5 vs champs
    # auto reset
    # buff duration 5.5s

# tgting         no tgt
# affects        self
# dmg            mag
# type           sin-tgt
# sShield        see notes
# parries        see notes

# notes

# pending for test: Ws relationship with dodge, parry, block, and blind.
# the passive dmg affect structures but active one wont.
# sShield blocks active dmg but not passive one.

