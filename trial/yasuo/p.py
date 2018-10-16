















from globals_ import *
import dmgheal
import stack
import shield

class P(ABS_P):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.STACK = stack.Yasuo_flow(CHAMP = self.CHAMP, 
                                      OWNER = self, 
                                      MAX = '?????????')
        self.flow = {1: 100,
                     2: 105, 
                     3: 110, 
                     4: 115, 
                     5: 120, 
                     6: 130, 
                     7: 140, 
                     8: 150, 
                     9: 165, 
                     10: 180, 
                     11: 200, 
                     12: 225, 
                     13: 255, 
                     14: 290, 
                     15: 330, 
                     16: 380, 
                     17: 440, 
                     18: 510}

        self._shield = shield.MShield(CHAMP  = self.CHAMP, 
                                      OWNER  = self, 
                                      target = self.CHAMP,
                                      amount = None,
                                      length = 1000)

    @property
    def shield(self):
        self._shield.amount = self.flow[self.lvl]
        return self._shield

# P
# self gets double critchance
# autos do 10% reduced dmg on crit

# self gets flow STACK for every {{[1]59 / 52 / 46}} units traveled
# at 100 STACK---{{[2]5900 / 5200 / 4600}}
# and upon taking champ or mon dmg, self consumes all flow 
# to shield self for {{[3]100 - 510 (lvl)}} for 1s

# tgting         passive
# affects        self
# type           shield

# notes
# together with infinity edges, selfs crit strike chance quadruples.
# intents reduction is applied to total dmg
# this makes autos crit strike for 180% ad.
# statikk shivs crit strike is also affected by 10% dmg reduction of intent, 
# do total of {{[4]108 - 252 (lvl)}} mDmg.

