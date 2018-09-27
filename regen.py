












from globals_ import *
import time_
import dmgheal
from effect import Effect


class Regen(KnowsCHAMP):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timer  = time_.Timer('kassadin?.REGEN', 
                                  'proc-regen {}'.format(self.CHAMP),
                                  500, 
                                  self.proc,
                                  persist=True)
        self.timer.go()
        self._heal = dmgheal.Heal(CHAMP  = self.CHAMP, 
                                  OWNER  = self, 
                                  amount = self.CHAMP.total_hp5 / 10,
                                  target = self.CHAMP,
                                  tags   = ['regen'],)
    def proc(self):
        self.timer.reset()
        self.heal.apply()
        # self.CHAMP.EFFECT_HANDLER.handle_effect(self.get_effect())

    @property
    def heal(self):
        # update true heal amount
        self._heal.amount = self.CHAMP.total_hp5 / 10
        return self._heal

    def get_effect(self):
        return Effect(
            CHAMP = self.CHAMP,
            OWNER = self,
            heal  = self.heal)





if __name__ == '__main__':
    pass 







