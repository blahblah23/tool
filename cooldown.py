



from globals_ import *
import time_



class Cooldown(KnowsCHAMP, KnowsOWNER):
    def __init__(self, name, length, **kwargs):
        super().__init__(**kwargs)
        self.ready = True
        self.timer = time_.Timer(name   = name, 
                                 length = length, 
                                 method = self.refresh)

    def trigger(self):
        self.ready = False
        self.timer.go()
    def refresh(self):
        self.ready = True
        self.timer.stop()
        # this might raise exception when trying to refresh if already ready



class StatiCooldown(Cooldown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    
    





# timer
# activate
# refresh
# resolve
# lower
# notify


























