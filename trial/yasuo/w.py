















from globals_ import *
import dmgheal
import cooldown
import time_


class W(ABS_W):

    RANGE = 400

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.width = 300 + 50 * self.lvlups # property

        self._CD = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                    OWNER  = self,
                                    name   = ['cd-refresh', str(self.CHAMP) + '.W'], 
                                    length = None)
        self.duration = time_.Timer(name   = ['windwall-duration', str(self.CHAMP) + '.W'], 
                                    length = 4000, 
                                    method = self.stop)
    def cast(self):
        self.CD.trigger()
        self.duration.go()
        self.buff.apply() # stop all projectiles from hitting
    
    def stop(self):
        pass

    @property
    def CD(self):
        self._CD.length = 26 - 2 * self.lvlups
        return self._CD
    
    





# W
# tgt range = 400 
# CD = 26 + -2.0 * self.lvlups

# active: windwall tgt dir over 0.25s
# wall slowly drifts forward 50 units over 3.75s
# blocking all em projs except turret atks

# wall width: 300 + 50 * self.lvlups

# tgting         dir
# affects        none
# proj           n/a

# notes
# W starts blocking projs on-cast (despite not being fully formed) and give sight over small area.

