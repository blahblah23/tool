

















from globals_ import *
import time_
import dmgheal
import cooldown






class Auto(KnowsCHAMP):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.on_land = []
        
        # self.castimer = time_.Timer(name   = 'auto-cast {}'.format(self.CHAMP),
        self.castimer = time_.Timer(name   = ['auto-cast', str(self.CHAMP) + '.AUTO'],
                                    length = self.cast_length,
                                    method = self.castimer_method)


        self.CD = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                    OWNER  = self,
                                    # name   = '{:15}{}.Auto'.format('cd-refresh', str(self.CHAMP)), 
                                    name   = ['cd-refresh', str(self.CHAMP) + '.AUTO'], 
                                    length = self.cd_length) 
        self._pdmg = dmgheal.PDmg(CHAMP  = self.CHAMP, 
                                  OWNER  = self, 
                                  target = None,
                                  amount = None, 
                                  tags   = ['auto'])
    def cast(self):
        self.castimer.go()
    def reset(self):
        self.CD.refresh()
        # TODO does this actually work?
    
    @property
    def cast_length(self):
        C = self.CHAMP
        return 500 - 250 * (C.total_ats - C.base_ats) / (0.0025 - C.base_ats)
        # TODO make an ats cap reference somewhere
    @property
    def cd_length(self):
        # length should be from send to send minus cast_length for a given speed
        return (1 / self.CHAMP.total_ats) - self.cast_length

    @property
    def pdmg(self):
        self._pdmg.target = self.CHAMP.target
        self._pdmg.amount = self.CHAMP.total_ad
        return self._pdmg

class AutoMelee(Auto):
    def __init__(self, **kwargs):
        self.castimer_method = self.land
        super().__init__(**kwargs)

    def land(self):
        self.CD.trigger()
        self.pdmg.apply()
        for thing in self.on_land:
            thing()


class AutoRanged(Auto):
    def __init__(self, **kwargs):
        self.castimer_method = self.send
        super().__init__(**kwargs)
        # self.sendtimer = time_.Timer(name    = 'auto-send {}'.format(self.CHAMP),
        self.sendtimer = time_.Timer(name    = ['auto-send', str(self.CHAMP) + '.AUTO'],
                                     length  = 250,
                                     method  = self.land)


    def send(self):
        self.sendtimer.go()
        self.CD.trigger()
    def land(self):
        self.pdmg.apply()
        for thing in self.on_land:
            thing()

#seems that if u get an ats buff mid cast
#   before the new cast_length; the new cast_length is used normally
#   after the new cast_length; the auto fires instantly
# 
# if u get the buff mid cooldown
#   before the new cd_length; new cd_length used normally
#   after the new cd_length; the auto/cd resets instantly 
# 
# if an ats buff falls off 
#   during cast; cast finishes still with the ats buff
#       but the cd_length and there-on falls down to normal without the buff  
#   during cooldown; the cooldown gets extended to the normalized cd_length







