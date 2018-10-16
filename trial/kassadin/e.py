
















from globals_ import *
from stack import Stacker, CoX
from dmgheal import MDmg
from effect import Effect
from slow import Slow
import cooldown




class E(ABS_E):


    RANGE    = 600
    ANGLE    = 80
#TODO SPEED    = ????

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cost     = 60 + 5 * self.lvlups
        self.castable = False
        #TODO costs mana   and   6 STACKs 
        # make cost a property?


        self.CD = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                    OWNER  = self, 
                                    name   = ['cd-refresh', str(self.CHAMP) + '.E'],
                                    length = 5000) 
        self.STACKER = CoX(CHAMP = self.CHAMP, 
                           OWNER = self, 
                           MAX = 6, 
                           on_max = [self.setCastable, [True]])
        self._mdmg = MDmg(CHAMP  = self.CHAMP, 
                          OWNER  = self, 
                          target = None,
                          amount = None, 
                          tags   = {'ability', 'aoe'})
        
        ###### subscribe STACKER to all ABILITY_USE
        toSubscribe.append([self.STACKER, getAllChampAbilityUseComponents]) 
    
    
    def cast(self):
        self.CD.trigger()
        self.CHAMP.current_mp -= self.cost
        self.mdmg.apply()
        self.STACKER.reset()
        
    def setCastable(self, value):
        self.castable = value


    
    
    
    @property
    def mdmg(self):
        self._mdmg.target = self.CHAMP.target
        self._mdmg.amount = 80 + 25 * self.lvlups + 0.7 * self.CHAMP.ap
        return self._mdmg
    @property
    def slow(self):
        return Slow(
            CHAMP = self.CHAMP,
            OWNER = self,
            slow  = 0.50 + 0.10 * self.lvlups,
        )
    
    


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











