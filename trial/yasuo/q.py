

















from globals_ import *
import dmgheal
import cooldown
import stack

class Q(ABS_Q):

    RANGE = 475
    RANGE = 900
    RADIUS = 375

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._CD = cooldown.StatiCooldown(CHAMP  = self.CHAMP, 
                                         OWNER  = self,
                                         name   = ['cd-refresh', str(self.CHAMP) + '.Q'], 
                                         length = None)
        self._pdmg = dmgheal.PDmg(CHAMP  = self.CHAMP, 
                                  OWNER  = self, 
                                  target = None,
                                  amount = None, 
                                  tags   = {'auto', 'ability', 'aoe'})
        self.STACK = stack.Yasuo_Q(CHAMP = self.CHAMP, 
                                   OWNER = self, 
                                   MAX = 2, 
                                   length = 6000)
    def cast(self):
        self.CD.trigger()
        self.pdmg.apply()

    @property
    def CD(self):
        self._CD.length = 4 * (1 - (self.CHAMP.bonus_ats / 0.016725))
        return self._CD    
    @property
    def pdmg(self):
        self._pdmg.target = self.CHAMP.target
        self._pdmg.amount = 20 + 25.0 * self.lvlups + self.CHAMP.total_ad
        return self._pdmg




# Q
# tgt range = 475 + 425.0 * (2) 
# rad: 375 
# static CD = 4 - 1.33 (based on ++ ats) 

# 1st cast - Q: after {{[1]0.54 - 0.18 (based on ++ ats)}} s-delay
# do pDmg to all ems in tgt dir
# give stack on do dmg and give oHs to 1st tgt hit
# pDmg: 20 + 25.0 * (self.lvl -1) (+ 100% ad)
# Q can critly strike, do 80% ad ++ pDmg

# 2nd cast - steel wind rising: for next 6 s, self can give 
# another gathering storm STACK by hitting em with Q, empowering it for same dur.

# 3rd cast - gathering storm: self consumes all STACK to unleash whirlwind 
# that travels incrd distance in tgt dir, do same dmg and knocking airborne all ems hit
# Qs knockup wont give incrd range when cast during sweeping blade.

# tgting         dir
# affects        ems
# dmg            phy
# type           aoe
# sShield        blocked
# oH             true
# parries        blocked
# proj           see nootes

# notes
# pending for test interaction with infinity edge.
# Q give oHs to 1st em hit (including duskblade of draktharrs nightstalker).
# Q can be parried or blocked but cant be dodged or negated if self is blinded.
# Q wont give abil effects.
# Qs dmg is calculated individually for every em hit when critly striking.
# Qs CD and castime reduction interacts with selfs ats growth (25.4% reduction at lvl 18)
# Q wont reset selfs auto timer when cast outside sweeping blade 
# (he atk right after animation ends if possible)
# the 1st and 2nd hit wont count as proj.

