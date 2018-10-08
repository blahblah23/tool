










from globals_ import *
import time_

        
class CurrentHp_DXR:
    def __get__(self, obj, type=None):
        return obj._current_hp
    def __set__(self, obj, value):
        # could cycle through shields here potentially
        if value <= 0:
            obj.target.shields.remove(obj)
            print(obj.target, 'shield depleted')
        obj._current_hp = value

class Shield(KnowsCHAMP, KnowsOWNER):

    current_hp = CurrentHp_DXR()

    def __init__(self, amount, length, target, **kwargs):
        super().__init__(**kwargs)
        self.amount = amount
        self.current_hp = amount
        self.target = target
        self.timer = time_.Timer('shield-expire {}'.format(self.target),
                                 length, 
                                 self.expire)

    def apply(self, target=None):
        if not target: target = self.target
        if not target: raise Exception('NO TARGET')

        # put self in right shield list/index
        shields = self._targets_shields()
        for idx, shield in enumerate(shields):
            if self >= shield:
                shields.insert(idx, self)
                break
        else: shields.append(self)

        self.timer.go()
    def _targets_shields(self):
        return self.target.shields
    def expire(self):
        self.target.shields.remove(self)

    def __ge__(self, y):
        if self.timer.end >= y.timer.end:
            return True
        else: 
            return False
class MShield(Shield, KnowsCHAMP, KnowsOWNER):
    def _targets_shields(self):
        return self.target.mshields
    def expire(self):
        self.target.mshields.remove(self)
class PShield(Shield, KnowsCHAMP, KnowsOWNER):
    def _targets_shields(self):
        return self.target.pshields
    def expire(self):
        self.target.pshields.remove(self)








