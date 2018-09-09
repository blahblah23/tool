





from globals_ import *
import data
import bonustat
import helpers


class BaseDescriptor:
    '''will only change when champ.lvl changes'''
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, obj, type=None):
        
        # return obj.ad + obj.ad_lvl * helpers.bbm(obj.lvl)
        return (  getattr(obj, self.attr_name)
                + getattr(obj, self.attr_name + '_lvl')
                * helpers.bbm(obj.lvl)  )
class TotalDescriptor:
    def __init__(self, attr_name):
        self.attr_name = attr_name
    
    def __get__(self, obj, type=None):
        
        return (getattr(obj, 'base_' + self.attr_name) 
                + sum( [bonus.value for bonus 
                in getattr(obj, 'bonus_' + self.attr_name)]))
class CurrentHpDescriptor:
    def __get__(self, obj, type=None):
        return obj._current_hp
    def __set__(self, obj, value):
        if value <= 0:
            # stop_simulation()
            # report_final_state()
            print(obj, 'died LUL')
        obj._current_hp = value
class CurrentMpDescriptor:
    def __get__(self, obj, type=None):
        return obj._current_mp
    def __set__(self, obj, value):
        obj._current_mp = value
class ArPenFlatDescriptor:
    def __get__(self, obj, type=None):
        return obj.lethality * (0.6 + 0.4 * obj.lvl / 18) 
class ListBonusDescriptor:
    def __init__(self, attr_name):
        self.attr_name = attr_name
    def __get__(self, obj, type=None):
        attr = getattr(obj, '_' + self.attr_name)
        return sum([bonus.value for bonus in attr])
    def __set__(self, obj, value):
        setattr(obj, '_' + self.attr_name, value)



class Stats(KnowsCHAMP):

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
        # current_mp  =   CurrentMpDescriptor()
        ar_pen_flat =   ArPenFlatDescriptor()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.lvl = self.CHAMP.lvl

        self._init_stats()

    def _get_data(self, stat):
        return data.data[self.CHAMP.__class__.__name__][stat]
    def _init_stats(self):

        self.cdr         =  0    # probly property/descriptor
        self.ap          =  0    # probly property/descriptor

        self.ar_reduc_flat       = 0       
        self.ar_reduc_percent    = 0           
        self.ar_pen_percent      = 0       
        # self.ar_pen_flat         = 0       
        self.lethality           = 0   

        self.mr_reduc_flat       = 0       
        self.mr_reduc_percent    = 0           
        self.mr_pen_percent      = 0       
        self.mr_pen_flat         = 0       

        self.crit        =  0    # probly property/descriptor
        self.critdmg     =  2    # probly property/descriptor
        self.lifesteal   =  0    # probly property/descriptor
        self.vamp        =  0    # probly property/descriptor
        self.hspower     =  0    # probly property/descriptor
        self.tenac       =  0    # probly property/descriptor

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








