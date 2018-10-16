





from globals_ import *
import cooldown
import shield
from dmgheal import MDmg




class Q(ABS_Q):

    SPEED = 1400
    RAD   = 650

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cost     = 70 + 5 * self.lvlups
        # make cost a property?
        
        self.CD = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                    OWNER  = self,
                                    name   = ['cd-refresh', str(self.CHAMP) + '.Q'], 
                                    length = 9000)
        self._mdmg = MDmg(CHAMP  = self.CHAMP, 
                          OWNER  = self, 
                          target = None,
                          amount = None, 
                          tags   = {'ability'})
        self._shield = shield.MShield(CHAMP  = self.CHAMP, 
                                      OWNER  = self, 
                                      target = self.CHAMP,
                                      amount = None,
                                      length = 1500)
    
    def cast(self):
        self.CD.trigger()
        self.CHAMP.current_mp -= self.cost
        self.mdmg.apply()
        self.shield.apply()

    @property
    def mdmg(self):
        self._mdmg.target = self.CHAMP.target
        self._mdmg.amount = 65 + 30 * self.lvlups + 0.7 * self.CHAMP.ap
        return self._mdmg
    @property
    def shield(self):
        self._shield.amount = 60 + 25 * self.lvlups + 0.3 * self.CHAMP.ap
        return self._shield

# Q
# tgt range: 650 
# spd: 1400 
# cost: '70+5.0&5' mana 
# cd: 9 

# active: tgtshot, do mDmg to tgt, shield self, TODO irupting channeled abils
# mDmg: '65+30.0&5' (+ 70% ap)
# mShield self 1.5s '60+25.0&5' (+ 30% ap)

# tgting         unit
# affects        tgt
# dmg            mag
# type           sin-tgt
# sShield        blocked
# proj           blocked


