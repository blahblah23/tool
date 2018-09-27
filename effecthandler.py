








from globals_ import *
import dmgheal




class EffectHandler(KnowsCHAMP):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def handle_effect(self, effect):

        self.handle_heal(effect)
        self.handle_dmg(effect)    
    def handle_dmg(self, effect):
        '''http://leagueoflegends.wikia.com/wiki/Armor_penetration'''
        # if effect.mdmg:    self.handle_mdmg(effect.mdmg)
        # if effect.pdmg:    self.handle_pdmg(effect.pdmg)
        # if effect.tdmg:    self.handle_tdmg(effect.tdmg)

        if effect.mdmg:    self.handle_xdmg(effect.mdmg)
        if effect.pdmg:    self.handle_xdmg(effect.pdmg)
        if effect.tdmg:    self.handle_xdmg(effect.tdmg)
    
    def handle_mdmg(self, mdmg):
        mr             = self.CHAMP.total_mr
        mr_pen_flat    = mdmg.CHAMP.mr_pen_flat
        mr_pen_percent = mdmg.CHAMP.mr_pen_percent
        
        if mr >= 0:
            post_dmg = mdmg.amount * 100 / (100 + max(0, 
                mr - mr_pen_percent * mr - mr_pen_flat))
        else:
            post_dmg = mdmg.amount * (2 - 100/(100 - mr))

        self.CHAMP.current_hp -= post_dmg
    def handle_xdmg(self, xdmg):
        if isinstance(xdmg, dmgheal.TDmg):
            self.CHAMP.current_hp -= xdmg.amount
            return
        elif isinstance(xdmg, dmgheal.PDmg):
            def_            = self.CHAMP.total_ar
            def_pen_flat    = xdmg.CHAMP.ar_pen_flat
            def_pen_percent = xdmg.CHAMP.ar_pen_percent
        else:
        # elif isinstance(xdmg, dmgheal.MDmg):
            def_            = self.CHAMP.total_mr
            def_pen_flat    = xdmg.CHAMP.mr_pen_flat
            def_pen_percent = xdmg.CHAMP.mr_pen_percent

        if def_ >= 0:
            post_dmg = xdmg.amount * 100 / (100 + max(0, 
                def_ - def_pen_percent * def_ - def_pen_flat))
        else:
            post_dmg = xdmg.amount * (2 - 100/(100 - def_))

        self.CHAMP.current_hp -= post_dmg

    def handle_heal(self, effect):
        
        if effect.heal:
            # hp = self.CHAMP.current_hp
            # amount = effect.heal.amount
            # self.CHAMP.current_hp = min(hp + amount, self.CHAMP.total_hp)
            self.CHAMP.current_hp += effect.heal.amount










    def defend_dmg(self, xdmg):

        if self.defence(dmg) >= 0: 
            post_dmg = 100/(100 + self.pen_def(dmg)) * dmg['amount']
        else:                      
            post_dmg = (2 - 100/(100 - self.defence(dmg))) * dmg['amount']
        
        return post_dmg
    def pen_def (self, dmg):
        '''return defence value after penetration from dmg'''
        return max(self.defence(dmg) - dmg['pen%'] * self.defence(dmg) - dmg['pen'], 0)
    def defence (self, dmg):
        ''' return <self.stat4> defence against <dmg['type']> '''
        if dmg['type'] == 'phys':
            return self.stat4['ar']
        elif dmg['type'] == 'magic':
            return self.stat4['mr']
        else: raise ValueError('not phys or magic dmg type')


if __name__ == '__main__':
    print(dmgheal.MDmg)
    pass


