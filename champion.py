







#commited from vscode on testbranch



from globals_ import *
import observer
import stats
import effecthandler
import data


class BaseDescriptor:
    '''will only change when champ.lvl changes'''
    def __init__(self, attr_name):
        self.attr_name = attr_name


        
        pass
    
    def __get__(self, obj, type=None):
        
        # return obj.ad                           + obj.ad_lvl                              * obj.base_building_multiplier(obj.lvl)
        return getattr(obj, self.attr_name)   +   getattr(obj, self.attr_name + '_lvl')   *   obj.base_building_multiplier(obj.lvl)


class TotalDescriptor:
    def __init__(self, attr_name):
        self.attr_name = attr_name
        pass
    
    def __get__(self, obj, type=None):
        
        # return self.base_ad                             + sum(    [    bonus[1] for bonus in  self.bonus_ad                            ]    )
        return getattr(obj, 'base_' + self.attr_name)   + sum(    [    bonus[1] for bonus in  getattr(obj, 'bonus_' + self.attr_name)  ]    )


class Champion:
    
    
    base_ad     =   BaseDescriptor('ad')
    total_ad    =   TotalDescriptor('ad')


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
        self.cdr         =   0
        self.ap          =   0
        self.crit        =   0
        self.critdmg     =   2
        self.lifesteal   =   0
        self.vamp        =   0
        self.arP         =   0
        self.mP          =   0
        self.hspower     =   0
        self.tenac       =   0

        # **data.data[self.CHAMP.__class__.__name__]


        attr_names = ['autoclass', 'ms', 'range', 'ats', 'ats_lvl', 'ad', 'ad_lvl', 'ar', 'ar_lvl', 
                        'mr', 'mr_lvl', 'hp', 'hp_lvl', 'mp', 'mp_lvl', 'hp5', 'hp5_lvl', 'mp5', 'mp5_lvl']

        for name in attr_names:
            setattr(self, name, self._get_data(name))

        self.autoclass  =  self._get_data('autoclass')
        self.ms         =  self._get_data('ms')
        self.range      =  self._get_data('range')
        self.ats        =  self._get_data('ats')
        self.ats_lvl    =  self._get_data('ats_lvl')
        self.ad         =  self._get_data('ad')
        self.ad_lvl     =  self._get_data('ad_lvl')
        self.ar         =  self._get_data('ar')
        self.ar_lvl     =  self._get_data('ar_lvl')
        self.mr         =  self._get_data('mr')
        self.mr_lvl     =  self._get_data('mr_lvl')
        self.hp         =  self._get_data('hp')
        self.hp_lvl     =  self._get_data('hp_lvl')
        self.mp         =  self._get_data('mp')
        self.mp_lvl     =  self._get_data('mp_lvl')
        self.hp5        =  self._get_data('hp5')
        self.hp5_lvl    =  self._get_data('hp5_lvl')
        self.mp5        =  self._get_data('mp5')
        self.mp5_lvl    =  self._get_data('mp5_lvl')

        self.base_ats    =   self.ats
        # self.base_ad     =   self.ad  + self.ad_lvl  * self.base_building_multiplier(self.lvl)
        # self.base_ad     =   BaseDescriptor('ad')
        self.base_ar     =   self.ar  + self.ar_lvl  * self.base_building_multiplier(self.lvl)
        self.base_mr     =   self.mr  + self.mr_lvl  * self.base_building_multiplier(self.lvl)
        self.base_hp     =   self.hp  + self.hp_lvl  * self.base_building_multiplier(self.lvl)
        self.base_mp     =   self.mp  + self.mp_lvl  * self.base_building_multiplier(self.lvl)
        self.base_hp5    =   self.hp5 + self.hp5_lvl * self.base_building_multiplier(self.lvl)
        self.base_mp5    =   self.mp5 + self.mp5_lvl * self.base_building_multiplier(self.lvl)

        self.bonus_ats   =   [['lvlbonus', self.ats_lvl * self.base_building_multiplier(self.lvl)]]
        # self.bonus_ad    =   [[0, 10]]
        self.bonus_ad    =   []
        self.bonus_ar    =   []
        self.bonus_mr    =   []
        self.bonus_hp    =   []
        self.bonus_mp    =   []
        self.bonus_hp5   =   []
        self.bonus_mp5   =   []

        self.total_ats   =   self.base_ats + sum(    [    bonus[1] for bonus in self.bonus_ats    ]    )
        # self.total_ad    =   self.base_ad  + sum(    [    bonus[1] for bonus in self.bonus_ad     ]    )
        # self.total_ad    =   TotalDescriptor('ad')
        self.total_ar    =   self.base_ar  + sum(    [    bonus[1] for bonus in self.bonus_ar     ]    )
        self.total_mr    =   self.base_mr  + sum(    [    bonus[1] for bonus in self.bonus_mr     ]    )
        self.total_hp    =   self.base_hp  + sum(    [    bonus[1] for bonus in self.bonus_hp     ]    )
        self.total_mp    =   self.base_mp  + sum(    [    bonus[1] for bonus in self.bonus_mp     ]    )
        self.total_hp5   =   self.base_hp5 + sum(    [    bonus[1] for bonus in self.bonus_hp5    ]    )
        self.total_mp5   =   self.base_mp5 + sum(    [    bonus[1] for bonus in self.bonus_mp5    ]    )

        self.current_hp  =   self.total_hp
        self.current_mp  =   self.total_mp


        pass
    def _load_skill(self, skill):
        '''str-skill := p,q,w,e,r'''
        mod = import_module('trial.{}.{}'.format(self.__class__.__name__.lower(), skill))
        return getattr(mod, skill.upper())(CHAMP=self)
    def base_building_multiplier(self, lvl):
        return (lvl - 1) * (0.685 + 0.0175 * lvl) 
    

    @property
    def base_ad(self):
        return self.ad  + self.ad_lvl  * self.base_building_multiplier(self.lvl)




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
    def die(self):
        # stop_simulation()
        # report_final_state()
        print(self, 'died')









    def __str__(self):
        return '{}{}'.format(self.__class__.__name__, hex(id(self)))




if __name__ == '__main__':
    # ass = Champion(10, 'qweqw')
    # pprint(globals())
    # print(allchamps.zyra.p)
    pass






