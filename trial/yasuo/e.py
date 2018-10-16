














from globals_ import *
import dmgheal
import cooldown
import stack

class E(ABS_E):

    RANGE = 475

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._CD = cooldown.StatiCooldown(CHAMP  = self.CHAMP, 
                                          OWNER  = self,
                                          name   = ['CD-refresh', str(self.CHAMP) + '.E'], 
                                          length = None)
        self._targetCD = cooldown.StatiCooldown(CHAMP  = self.CHAMP, 
                                                OWNER  = self,
                                                name   = ['targetCD-refresh', str(self.CHAMP) + '.E'], 
                                                length = None)
        self._mdmg = dmgheal.MDmg(CHAMP  = self.CHAMP, 
                                  OWNER  = self, 
                                  target = None,
                                  amount = None, 
                                  tags   = {'auto', 'ability'})
        self.STACK = stack.DurMax(CHAMP = self.CHAMP, 
                                  OWNER = self, 
                                  MAX = 2, 
                                  length = 5000)
    def cast(self):
        self.targetCD.trigger()
        self.CD.trigger()
        self.mdmg.apply()
        self.STACK.add(1)
        self.STACK.duration.reset()
        #self.CHAMP.P.STACK.add(7.5)

    @property
    def CD(self):
        self._CD.length = 500 - 100 * self.lvlups
        return self._CD    
    @property
    def targetCD(self):
        self._targetCD.length = 10000 - 1000 * self.lvlups
        return self._targetCD    
    @property
    def mdmg(self):
        self._mdmg.target = self.CHAMP.target
        fromstacks = 0.25 * self.STACK.counter * (60 + 10 * self.lvlups)
        self._mdmg.amount = fromstacks + (60 + 10 * self.lvlups + 0.2 
                             * self.CHAMP.bonus_ad + 0.6 * self.CHAMP.ap)
        return self._mdmg








# E
# tgt range = 475 
# static CD = 0.5 / 0.4 / 0.3 / 0.2 / 0.1 
# TODO on-tgt CD = 10 - 1.0 * self.lvlups

# active: self dashes fixed distance toward em TODO over 0.55s 
# (reduced with ++ mvSpd, incrd by slow effects) do mDmg

# mDmg: 60 + 10.0 * self.lvlups (+ 20% ++ ad) (+ 60% ap)
# max : 90 + 15.0 * self.lvlups (+ 20% ++ ad) (+ 60% ap)
# each E cast incrs next dashs base dmg by 25% for 5 s, up to 50%.

# ++ dmg: 15 + 2.5 * self.lvlups
# max ++ dmg: 30 + 5.0 * self.lvlups

# tgting         unit
# affects        tgt
# dmg            mag
# type           sin-tgt
# sShield        blocked
# grounded       disabled
# minion aggro   true
# knockdown      irupted

# notes
# TODO E generate 7.5 flow STACK per cast.
# self can use Es fixed dash distance to go thru walls both before 
# and after hitting his tgt (provided his proximity to wall and/or tgt allows it)
# self stop mid-dash if he is immobilized by cc effects or using flash during E.

