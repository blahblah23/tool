





from globals_ import *
import data
import bonustat
import helpers


class Base_DXR:
    '''will only change when champ.lvl changes'''
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, obj, type=None):
        
        # return obj.ad + obj.ad_lvl * helpers.bbm(obj.lvl)
        return (  getattr(obj, self.attr_name)
                + getattr(obj, self.attr_name + '_lvl')
                * helpers.bbm(obj.lvl)  )
class Total_DXR:
    def __init__(self, attr_name):
        self.attr_name = attr_name
    
    def __get__(self, obj, type=None):
        
        return (getattr(obj, 'base_' + self.attr_name) 
                + sum( [bonus.value for bonus 
                in getattr(obj, 'bonus_' + self.attr_name)]))
class TotalAts_DXR:
    def __init__(self, attr_name):
        self.attr_name = attr_name
    
    def __get__(self, obj, type=None):
        
        return (getattr(obj, 'base_' + self.attr_name) 
                * (1 + sum( [bonus.value for bonus 
                in getattr(obj, 'bonus_' + self.attr_name)])))
class CurrentHp_DXR:
    def __get__(self, obj, type=None):
        return obj._current_hp
    def __set__(self, obj, value):
        if value <= 0:
            # stop_simulation()
            # report_final_state()
            print(obj, 'died LUL')
        if value >= obj.total_hp:
            value = obj.total_hp
        obj._current_hp = value
class CurrentMp_DXR:
    def __get__(self, obj, type=None):
        return obj._current_mp
    def __set__(self, obj, value):
        obj._current_mp = value
class ArPenFlat_DXR:
    def __get__(self, obj, type=None):
        return obj.lethality * (0.6 + 0.4 * obj.lvl / 18) 
class ListBonus_DXR:
    def __init__(self, attr_name):
        self.attr_name = attr_name
    def __get__(self, obj, type=None):
        attr = getattr(obj, '_' + self.attr_name)
        return sum([bonus.value for bonus in attr])
    def __set__(self, obj, value):
        setattr(obj, '_' + self.attr_name, value)



class Stats(KnowsCHAMP):

    if True: # class attrs
        base_ad     =   Base_DXR('ad')
        base_ar     =   Base_DXR('ar')
        base_mr     =   Base_DXR('mr')
        base_hp     =   Base_DXR('hp')
        base_mp     =   Base_DXR('mp')
        base_hp5    =   Base_DXR('hp5')
        base_mp5    =   Base_DXR('mp5')

        total_ats   =   TotalAts_DXR('ats')
        total_ad    =   Total_DXR('ad')
        total_ar    =   Total_DXR('ar')
        total_mr    =   Total_DXR('mr')
        total_hp    =   Total_DXR('hp')
        total_mp    =   Total_DXR('mp')
        total_hp5   =   Total_DXR('hp5')
        total_mp5   =   Total_DXR('mp5')

        current_hp  =   CurrentHp_DXR()
        # current_mp  =   CurrentMp_DXR()
        ar_pen_flat =   ArPenFlat_DXR()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.lvl = self.CHAMP.lvl
        self._init_stats()

    def _get_data(self, stat):
        return data.data[self.CHAMP.__class__.__name__][stat]
    def _init_stats(self):

        self.cdr         =  0    # probly property/_DXR
        self.ap          =  0    # probly property/_DXR
        self.ar_reduc_flat       = 0       
        self.ar_reduc_percent    = 0           
        self.ar_pen_percent      = 0       
        # self.ar_pen_flat         = 0       
        self.lethality           = 0   
        self.mr_reduc_flat       = 0       
        self.mr_reduc_percent    = 0           
        self.mr_pen_percent      = 0       
        self.mr_pen_flat         = 0       
        self.crit        =  0    # probly property/_DXR
        self.critdmg     =  2    # probly property/_DXR
        self.lifesteal   =  0    # probly property/_DXR
        self.vamp        =  0    # probly property/_DXR
        self.hspower     =  0    # probly property/_DXR
        self.tenac       =  0    # probly property/_DXR

        self.autoclass  =  self._get_data( 'autoclass')
        self.ms         =  self._get_data( 'ms'       )
        self.range      =  self._get_data( 'range'    )
        self.ats        =  self._get_data( 'ats'      ) / 1000
        self.ats_lvl    =  self._get_data( 'ats_lvl'  )
        # TODO some champs have innate bonus ats at lvl 1???
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

        self.bonus_ats   =   [bonustat.Bonus('lvlbonus', self.ats_lvl * helpers.bbm(self.lvl))]
        self.bonus_ad    =   []
        self.bonus_ar    =   []
        self.bonus_mr    =   []
        self.bonus_hp    =   []
        self.bonus_mp    =   []
        self.bonus_hp5   =   []
        self.bonus_mp5   =   []

        self.current_hp  =   self.total_hp
        self.current_mp  =   self.total_mp








