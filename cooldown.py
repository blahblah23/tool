



from globals_ import *
import time_

class Cooldown(KnowsCHAMP, KnowsOWNER):
    def __init__(self, length, **kwargs):
        super().__init__(**kwargs)
        self.ready = True
        self.timer = time_.Timer('kassadin?.E.cd', 
                                 'cd-refresh kassadin?.E',
                                 length, 
                                 self.refresh)

    def trigger(self):
        self.ready = False
        self.timer.go()
    def refresh(self):
        self.ready = True
        self.timer.stop()



class StatiCooldown(KnowsCHAMP, KnowsOWNER):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    
    





# timer
# activate
# refresh
# resolve
# lower
# notify





























