
















from globals_ import *
from stack import Stacker, CoX
from dmgheal import MDmg
from effect import Effect
from slow import Slow
import time
import cooldown




class E(ABS_E):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.RAD      = 600
        self.ANGLE    = 80
        self.cost     = 60 + 5 * (self.lvl - 1)
        #### TODO costs mana   and   6 STACKs 
        self.CD       = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                          OWNER  = self, 
                                          length = 500) 
        self.castable = False
        self.STACKER  = CoX(self.CHAMP, 
                            self, 
                            6, 
                            [self.setCastable, [True]])
        
        
        ###### subscribe STACKER to all ABILITY_USE
        toSubscribe.append([self.STACKER, getAllChampAbilityUseComponents]) 
    def get_inherent_dmg(self):
        return 80 + 25 * self.lvlups + 0.7 * self.CHAMP.ap
    def get_inherent_slow(self):
        return 0.50 + 0.10 * self.lvlups
    def get_mdmg(self):
        # doesnt need to return more than one instance ever?
        return MDmg(
            CHAMP  = self.CHAMP, 
            OWNER  = self, 
            amount = self.get_inherent_dmg(), 
            tags   = ['ability', 'aoe']
        )
    def get_slow(self):
        return Slow(
            CHAMP = self.CHAMP,
            OWNER = self,
            slow  = self.get_inherent_slow(),
        )
    def get_effect(self):
        return Effect(
            CHAMP = self.CHAMP,
            OWNER = self,
            mdmg  = self.get_mdmg(),
            slow  = self.get_slow(),
        )
    def cast(self):
        self.CD.trigger()
        # cd     time.Timer('kassadin?.E.cd', 500, )
        self.CHAMP.current_mp -= self.cost
        self.CHAMP.tgt.EFFECT_HANDLER.handle_effect(self.get_effect())
        self.STACKER.reset()
    def setCastable(self, value):
        self.castable = value




# passive: self get STACK on TODO nearby TODO abil use, max 6
# at 6, E becomes castable
# TODO toggle abils dont give STACK TODO

# TODO projectile speed or instant dmg?
# active: TODO skillshot, do mDmg to TODO all ems, slow 1s
# mDmg: 80 + 25 * (self.lvl -1) (+ 70% ap)
# slow: 50 + 10 * (self.lvl -1)%

# tgting         dir
# affects        ems
# dmg            mag

# type           aoe
# sShield        blocked
# proj           n/a











