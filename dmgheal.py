













from globals_ import *



class ABS_Dmg(KnowsCHAMP, KnowsOWNER):
    def __init__(self, amount, tags=[], **kwargs):
        super().__init__(**kwargs)
        self.tags = tags
        self.amount  = amount

class MDmg(ABS_Dmg):
    '''positional args need kywds := amount, tags, CHAMP, OWNER'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        '''http://leagueoflegends.wikia.com/wiki/Armor_penetration'''
        # self.pen_flat = self.CHAMP.mP
        # self.pen_percent = self.CHAMP.mP

class PDmg(ABS_Dmg):
    pass
class TDmg(ABS_Dmg):
    pass




class Heal(KnowsCHAMP, KnowsOWNER):
    def __init__(self, x, tags=[], **kwargs):
        super().__init__(**kwargs)
        self.tags = tags
        self.x = x
    def __call__(self, target):
        target.takeHeal()




if __name__ == '__main__':

    MDmg(
        amount = 100, 
        tags   = ['basic atk dmg'], 
        CHAMP  = None,
        OWNER  = None
    )





    pass













