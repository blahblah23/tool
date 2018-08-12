













from globals_ import *



class ABS_Dmg(KnowsCHAMP, KnowsOWNER):
    def __init__(self, dmg, tags=[], **kwargs):
        super().__init__(**kwargs)

        self.tags = tags
        self.dmg  = dmg
    def __getattr__(self, attr):
        return getattr(self.CHAMP, attr)

class MDmg(ABS_Dmg):
    '''positional args need kywds := dmg, tags, CHAMP, OWNER'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class PDmg(ABS_Dmg):
    pass
class TDmg(ABS_Dmg):
    pass


MDmg(
    dmg   = 100, 
    tags  = ['basic atk dmg'], 
    CHAMP = None,
    OWNER = None
)


class Heal(KnowsCHAMP, KnowsOWNER):
    def __init__(self, x, tags=[], **kwargs):
        super().__init__(**kwargs)
        self.tags = tags
        self.x = x
    def __call__(self, target):
        target.takeHeal()


















