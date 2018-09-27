













from globals_ import *



class ABS_Dmg(KnowsCHAMP, KnowsOWNER):
    def __init__(self, amount, tags=[], **kwargs):
        super().__init__(**kwargs)
        self.amount  = amount
        self.tags = tags

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
    def __init__(self, amount, target=None, tags=[], **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.amount = amount
        self.tags = tags

    def apply(self, target=None):
        if not target:
            target = self.target
        if not target:
            raise Exception('NO TARGET')

        # other heal logic here
        target.current_hp += self.amount



if __name__ == '__main__':

    MDmg(
        amount = 100, 
        tags   = ['basic atk dmg'], 
        CHAMP  = None,
        OWNER  = None
    )





    pass













