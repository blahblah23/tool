



from globals_ import *
import cooldown
import dmgheal
import stack

class R(ABS_R):

    RANGE = 500
    RAD   = 150

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.STACKER = stack.DurMax(CHAMP = self.CHAMP, 
                                    OWNER = self, 
                                    MAX = 4, 
                                    length = 15000)
        self._CD = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                     OWNER  = self,
                                     name   = ['cd-refresh', str(self.CHAMP) + '.R'], 
                                     length = None)
        self._mdmg = dmgheal.MDmg(CHAMP  = self.CHAMP, 
                                  OWNER  = self, 
                                  target = None,
                                  amount = None, 
                                  tags   = {'ability', 'aoe'})

        self.cost = 50 * 2 ** self.STACKER.counter

    def cast(self):
        self.CD.trigger()
        self.CHAMP.current_mp -= self.cost
        self.mdmg.apply()
        if self.STACKER.counter == 0:
            self.STACKER.duration.go()
        self.STACKER.add(1)
        self.STACKER.duration.reset()

    @property
    def CD(self):
        self._CD.length = 5000 - 1500 * self.lvlups
        return self._CD
    @property
    def mdmg(self):
        self._mdmg.target = self.CHAMP.target
        base  = 80 + 20 * self.lvlups + 0.3 * self.CHAMP.ap + 0.02 * self.CHAMP.total_mp
        stack = (40 + 10 * self.lvlups + 0.1 * self.CHAMP.ap + 0.01 * self.CHAMP.total_mp) * self.STACKER.counter
        self._mdmg.amount = base + stack  
        return self._mdmg

    def __str__(self):
        return 'R{}'.format('')

# R
# tgt range: 500 
# rad: 150 
# cost: 50 / 100 / 200 / 400 / 800 mana 
# cd: '5+-1.5&3' 

# active: after small delay, self blinks to tgt location, do mDmg all to nearby ems on arrival.

# mDmg: '80+20.0&3' (+ 30% ap) (+ 2% max mana)
# each subsequent R in 15 s doubles its mana cost and incrs its dmg, stacking up to 4 times.

# ++ dmg per stack: '40+10.0&3' (+ 10% ap) (+ 1% max mana)
#        max mDmg: '240+60.0&3' (+ 70% ap) (+ 6% max mana)

# tgting         ground
# affects        ems
# dmg            mag
# type           aoe
# sShield        blocked
# grounded       disabled
# knockdown      unstoppable


