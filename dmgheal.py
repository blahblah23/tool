













from globals_ import *



class ABS_Dmg(KnowsCHAMP, KnowsOWNER):
    def __init__(self, amount, target=None, tags=set(), **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.amount = amount
        self.tags = tags

    def apply(self, target=None):
        if not target: target = self.target
        if not target: raise Exception('NO TARGET')

        # armor/mr mitigation
        dmg = self.mitigate(target)
        
        # apply dmg_reductions
        for reduction in target.dmg_reductions:
            dmg = reduction.apply(self, dmg)
        
        # dmg shields first
        # shield dmging order: type > soonest to expire
        for shield in self.targets_shields(target):
            sh_hp = shield.current_hp
            if dmg >= sh_hp:
                shield.current_hp = 0
                dmg -= sh_hp
                if dmg == 0: return
            else:
                shield.current_hp -= dmg
                return

        print(round(dmg), 'from: {}'.format(self.OWNER))
        target.current_hp -= dmg
    def mitigate(self, target):
        if isinstance(self, TDmg):
            return self.amount
        if isinstance(self, MDmg):
            def_            = target.total_mr
            def_pen_flat    = self.CHAMP.mr_pen_flat
            def_pen_percent = self.CHAMP.mr_pen_percent
        elif isinstance(self, PDmg):
            def_            = target.total_ar
            def_pen_flat    = self.CHAMP.ar_pen_flat
            def_pen_percent = self.CHAMP.ar_pen_percent

        if def_ >= 0:
            post_dmg = self.amount * 100 / (100 + max(0, 
                def_ - def_pen_percent * def_ - def_pen_flat))
        else:
            post_dmg = self.amount * (2 - 100/(100 - def_))

        return post_dmg
    def targets_shields(self, target):

        raise Excepttion('not implemented')

        # common  = ({'magic', 'physical', 'true'} & self.tags).pop()
        # shields = {'magic': target.mshields, 'physical': target.pshields}
        
        if 'magic' in self.tags:
            return target.mshields + target.shields
        elif 'physical' in self.tags:
            return target.pshields + target.shields
        elif 'true' in self.tags:
            return target.shields

class MDmg(ABS_Dmg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tags.add('magic')
    def targets_shields(self, target):
        return target.mshields + target.shields
class PDmg(ABS_Dmg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tags.add('physical')
    def targets_shields(self, target):
        return target.pshields + target.shields
class TDmg(ABS_Dmg):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tags.add('true')
    def targets_shields(self, target):
        return target.shields




class Heal(KnowsCHAMP, KnowsOWNER):
    def __init__(self, amount, target=None, tags=[], **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.amount = amount
        self.tags = tags

    def apply(self, target=None):
        if not target: target = self.target
        if not target: raise Exception('NO TARGET')

        # other heal logic here
        target.current_hp += self.amount

class Managain(KnowsCHAMP, KnowsOWNER):
    def __init__(self, amount, target=None, **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.amount = amount

    def apply(self, target=None):
        if not target: target = self.target
        if not target: raise Exception('NO TARGET')

        # other managain logic here
        target.current_mp += self.amount


class DmgReduction(KnowsCHAMP, KnowsOWNER):
    def __init__(self, amount, tags=set(), **kwargs):
        super().__init__(**kwargs)
        self.amount = amount
        self.tags = tags
    def apply(self, dmgobj, amount):
        if self.tags & dmgobj.tags:
            return amount * self.amount
        return amount


if __name__ == '__main__':

    MDmg(
        amount = 100, 
        tags   = ['basic atk dmg'], 
        CHAMP  = None,
        OWNER  = None
    )





    pass













