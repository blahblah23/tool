








from globals_ import *
import dmgheal




class EffectHandler(KnowsCHAMP):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def handle_dmg(self, dmg):
        if dmg['mdmg']:
            self.CHAMP.STATS.stats['current_hp'] -= dmg['mdmg'].dmg
        if dmg['pdmg']:
            self.CHAMP.STATS.stats['current_hp'] -= dmg['pdmg'].dmg
        if dmg['tdmg']:
            self.CHAMP.STATS.stats['current_hp'] -= dmg['tdmg'].dmg
        
        if self.CHAMP.STATS.stats['current_hp'] <= 0:
            self.CHAMP.die()
    def handle_effect(self, effect):
        # self.handle_dmg(effect)
        self.handle_dmg(effect.dmg)


    def dmg             (self, typ, amount):
        ''' typ = 'phys' or 'magic'  build a dmg dict----ideally this will be the standard for passing around dmg'''
        return {
            'type':   typ,
            'amount': amount,
            'pen':    self.stat4[TYPESTAT[typ]['pen']],
            'pen%':   self.stat4[TYPESTAT[typ]['pen%']]
        }
    def take_dmg        (self, dmg):
        '''            dmg  = {type: ?, amount: ?, pen: ?, pen%: ?}'''           
        if self.defence(dmg) >= 0: post_dmg = 100/(100 + self.pen_def(dmg)) * dmg['amount']
        else:                      post_dmg = (2 - 100/(100 - self.defence(dmg))) * dmg['amount']
        self.stat4['hp_current'] -= post_dmg
    def pen_def         (self, dmg):
        '''return defence value after penetration from dmg'''
        return max(self.defence(dmg) - dmg['pen%'] * self.defence(dmg) - dmg['pen'], 0)
    def defence         (self, dmg):
        ''' return <self.stat4> defence against <dmg['type']> '''
        if dmg['type'] == 'phys':
            return self.stat4['ar']
        elif dmg['type'] == 'magic':
            return self.stat4['mr']
        else: raise ValueError('not phys or magic dmg type')


if __name__ == '__main__':
    print(dmgheal.MDmg)
    pass


