








from globals_ import *
import dmgheal




class EffectHandler(KnowsCHAMP):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def handle_dmg(self, dmg):
        '''http://leagueoflegends.wikia.com/wiki/Armor_penetration'''
        if dmg['mdmg']:
            mdmg = dmg['mdmg']

            defence = self.CHAMP.total_mr
            mP_flat = 000000
            self.CHAMP.current_hp -= mdmg.amount

        if dmg['pdmg']:
            pdmg = dmg['pdmg']
            
            defence = self.CHAMP.total_ar
            self.CHAMP.current_hp -= pdmg.amount

        if dmg['tdmg']:
            tdmg = dmg['tdmg']
            self.CHAMP.current_hp -= tdmg.amount
            
    def handle_effect(self, effect):
        # self.handle_dmg(effect)
        self.handle_dmg(effect.dmg)


    def dmg     (self, typ, amount):
        ''' typ = 'phys' or 'magic'  
            return dmg dict'''
        return {
            'type':   typ,
            'amount': amount,
            'pen':    self.stat4[TYPESTAT[typ]['pen']],
            'pen%':   self.stat4[TYPESTAT[typ]['pen%']]
        }
    def defend_dmg(self, dmg):

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


