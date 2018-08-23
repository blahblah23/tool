def champ_decorator(cls):
    bases = ['base_ad', 'base_ar', 'base_mr', 
                'base_hp', 'base_mp', 'base_hp5', 'base_mp5']
    totals = ['total_ats', 'total_ad', 'total_ar', 'total_mr', 
                'total_hp', 'total_mp', 'total_hp5', 'total_mp5']
    for name in bases:
        stat = name.split('_')[1]
        setattr(cls, name, BaseDescriptor(stat))
    for name in totals:
        stat = name.split('_')[1]
        setattr(cls, name, TotalDescriptor(stat))
    return cls












from globals_ import *
import observer
# import stats
import effecthandler
import data
import helpers
import bonustat

class BaseDescriptor:
    '''will only change when champ.lvl changes'''
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, obj, type=None):
        
        # return obj.ad                           + obj.ad_lvl                              * obj.bbm(obj.lvl)
        return getattr(obj, self.attr_name) + getattr(obj, self.attr_name + '_lvl') * helpers.bbm(obj.lvl)
class TotalDescriptor:
    def __init__(self, attr_name):
        self.attr_name = attr_name
        pass
    
    def __get__(self, obj, type=None):
        
        # return self.base_ad                             + sum(    [    bonus[1] for bonus in  self.bonus_ad                            ]    )
        return getattr(obj, 'base_' + self.attr_name)   + sum(    [    bonus.value for bonus in  getattr(obj, 'bonus_' + self.attr_name)  ]    )
class CurrentHpDescriptor:
    # def __init__(self):
    #     pass
    
    def __get__(self, obj, type=None):
        return obj._current_hp
    def __set__(self, obj, value):
        if value <= 0:
            # stop_simulation()
            # report_final_state()
            print(obj, 'died LUL')
        obj._current_hp = value


class Champion:

    if True: # class attrs
        base_ad     =   BaseDescriptor('ad')
        base_ar     =   BaseDescriptor('ar')
        base_mr     =   BaseDescriptor('mr')
        base_hp     =   BaseDescriptor('hp')
        base_mp     =   BaseDescriptor('mp')
        base_hp5    =   BaseDescriptor('hp5')
        base_mp5    =   BaseDescriptor('mp5')

        total_ats   =   TotalDescriptor('ats')
        total_ad    =   TotalDescriptor('ad')
        total_ar    =   TotalDescriptor('ar')
        total_mr    =   TotalDescriptor('mr')
        total_hp    =   TotalDescriptor('hp')
        total_mp    =   TotalDescriptor('mp')
        total_hp5   =   TotalDescriptor('hp5')
        total_mp5   =   TotalDescriptor('mp5')

        current_hp  =   CurrentHpDescriptor()

    def __init__(self, lvl, scheme, tgt=None, **kwargs):
        super().__init__(**kwargs)

        allChamps.append(self)

        self.lvl = lvl
        self.tgt = tgt
        self.scheme = scheme

        self._init_stats()

        self.EFFECT_HANDLER = effecthandler.EffectHandler(CHAMP=self)
        self.ABILITY_USED   =      observer.AbilityUsed() ### this design seems bad

        self.P = self._load_skill('p')
        self.Q = self._load_skill('q')
        self.W = self._load_skill('w')
        self.E = self._load_skill('e')
        self.R = self._load_skill('r')
    def _get_data(self, stat):
        return data.data[self.__class__.__name__][stat]
    def _init_stats(self):

        self.cdr        =  0    # probly property/descriptor
        self.ap         =  0    # probly property/descriptor
        self.arP        =  0    # probly property/descriptor
        self.mP         =  0    # probly property/descriptor
        self.crit       =  0    # probly property/descriptor
        self.critdmg    =  2    # probly property/descriptor
        self.lifesteal  =  0    # probly property/descriptor
        self.vamp       =  0    # probly property/descriptor
        self.hspower    =  0    # probly property/descriptor
        self.tenac      =  0    # probly property/descriptor

        self.autoclass  =  self._get_data( 'autoclass')
        self.ms         =  self._get_data( 'ms'       )
        self.range      =  self._get_data( 'range'    )
        self.ats        =  self._get_data( 'ats'      )
        self.ats_lvl    =  self._get_data( 'ats_lvl'  )
        self.ad         =  self._get_data( 'ad'       )
        self.ad_lvl     =  self._get_data( 'ad_lvl'   )
        self.ar         =  self._get_data( 'ar'       )
        self.ar_lvl     =  self._get_data( 'ar_lvl'   )
        self.mr         =  self._get_data( 'mr'       )
        self.mr_lvl     =  self._get_data( 'mr_lvl'   )
        self.hp         =  self._get_data( 'hp'       )
        self.hp_lvl     =  self._get_data( 'hp_lvl'   )
        self.mp         =  self._get_data( 'mp'       )
        self.mp_lvl     =  self._get_data( 'mp_lvl'   )
        self.hp5        =  self._get_data( 'hp5'      )
        self.hp5_lvl    =  self._get_data( 'hp5_lvl'  )
        self.mp5        =  self._get_data( 'mp5'      )
        self.mp5_lvl    =  self._get_data( 'mp5_lvl'  )

        self.base_ats   =  self.ats

        self.bonus_ats   =   [[bonustat.Bonus('lvlbonus', self.ats_lvl * helpers.bbm(self.lvl))]]
        self.bonus_ad    =   []
        self.bonus_ar    =   []
        self.bonus_mr    =   []
        self.bonus_hp    =   []
        self.bonus_mp    =   []
        self.bonus_hp5   =   []
        self.bonus_mp5   =   []

        self.current_hp  =   self.total_hp
        self.current_mp  =   self.total_mp
    def _load_skill(self, skill):
        '''str-skill := p,q,w,e,r'''
        mod = import_module('trial.{}.{}'.format(self.__class__.__name__.lower(), skill))
        return getattr(mod, skill.upper())(CHAMP=self)
    
    def doDmg(self):
        #calc outgoing dmg
        self.tgt.takeDmg(outgoing_dmg)
    def take_dmg(self, incoming_dmg):
        self.hitpoints -= incoming_dmg
    def q(self):
        # other code
        # other code
        # self.abilityUsed()
        self.ABILITY_USED.notify()

    def __str__(self):
        return '{}{}'.format(self.__class__.__name__, hex(id(self)))




if __name__ == '__main__':
    # ass = Champion(10, 'qweqw')
    # pprint(globals())
    # print(allchamps.zyra.p)
    pass















