





from globals_ import *
import time
import cooldown
import shield
from dmgheal import MDmg
from effect import Effect

class Q(ABS_Q):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.SPEED    = 1400
        self.RAD      = 650
        self.cost     = 70 + 5 * self.lvlups
        # make cost a property?
        self.CD       = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                          OWNER  = self, 
                                          length = 900) 
        self.castable = True
    
    def get_effect(self):
        return Effect(
            CHAMP = self.CHAMP,
            OWNER = self,
            mdmg  = self.mdmg,
            slow  = None,
        )
    def cast(self):
        self.CD.trigger()
        # cd     time.Timer('kassadin?.E.cd', 500, )
        self.CHAMP.current_mp -= self.cost
        shield.Shield(self.CHAMP, self.shield, 1500)
        self.CHAMP.tgt.EFFECT_HANDLER.handle_effect(self.get_effect())

    @property
    def dmg(self):
        return 65 + 30 * self.lvlups + 0.7 * self.CHAMP.ap

    @property
    def mdmg(self):
        # doesnt need to return more than one instance ever?
        return MDmg(
            CHAMP  = self.CHAMP, 
            OWNER  = self, 
            amount = self.dmg, 
            tags   = ['ability']
        )

    @property
    def shield(self):
        return 60 + 25 * self.lvlups + 0.3 * self.CHAMP.ap

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


