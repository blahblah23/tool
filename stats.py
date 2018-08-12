





from globals_ import *
import data

class Stats(KnowsCHAMP):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.lvl = self.CHAMP.lvl
        
        if True:        # self.stats = {all values}
            self.stats = {      # rawdata
                'cdr':       0,
                'ap':        0,
                'crit':      0,
                'critdmg':   2,
                'lifesteal': 0,
                'vamp':      0,
                'arP':       0,
                'mP':        0,
                'hspower':   0,
                'tenac':     0,
                **data.data[self.CHAMP.__class__.__name__],
            }
            self.stats = {      # base bonus
                **self.stats,
                'base_ats': self.stats['ats'],
                'base_ad':  self.stats['ad']  + self.stats['ad_lvl']  * self.base_building_multiplier(self.lvl),
                'base_ar':  self.stats['ar']  + self.stats['ar_lvl']  * self.base_building_multiplier(self.lvl),
                'base_mr':  self.stats['mr']  + self.stats['mr_lvl']  * self.base_building_multiplier(self.lvl),
                'base_hp':  self.stats['hp']  + self.stats['hp_lvl']  * self.base_building_multiplier(self.lvl),
                'base_mp':  self.stats['mp']  + self.stats['mp_lvl']  * self.base_building_multiplier(self.lvl),
                'base_hp5': self.stats['hp5'] + self.stats['hp5_lvl'] * self.base_building_multiplier(self.lvl),
                'base_mp5': self.stats['mp5'] + self.stats['mp5_lvl'] * self.base_building_multiplier(self.lvl),

                'bonus_ats': [['lvlbonus', self.stats['ats_lvl'] * self.base_building_multiplier(self.lvl)]],
                'bonus_ad':  [],
                'bonus_ar':  [],
                'bonus_mr':  [],
                'bonus_hp':  [],
                'bonus_mp':  [],
                'bonus_hp5': [],
                'bonus_mp5': [],
            }
            self.stats = {      # total
                **self.stats,
                'total_ats': self.stats['base_ats'] + sum(    [    bonus[1] for bonus in self.stats['bonus_ats']    ]    ),
                'total_ad':  self.stats['base_ad' ] + sum(    [    bonus[1] for bonus in self.stats['bonus_ad' ]    ]    ),
                'total_ar':  self.stats['base_ar' ] + sum(    [    bonus[1] for bonus in self.stats['bonus_ar' ]    ]    ),
                'total_mr':  self.stats['base_mr' ] + sum(    [    bonus[1] for bonus in self.stats['bonus_mr' ]    ]    ),
                'total_hp':  self.stats['base_hp' ] + sum(    [    bonus[1] for bonus in self.stats['bonus_hp' ]    ]    ),
                'total_mp':  self.stats['base_mp' ] + sum(    [    bonus[1] for bonus in self.stats['bonus_mp' ]    ]    ),
                'total_hp5': self.stats['base_hp5'] + sum(    [    bonus[1] for bonus in self.stats['bonus_hp5']    ]    ),
                'total_mp5': self.stats['base_mp5'] + sum(    [    bonus[1] for bonus in self.stats['bonus_mp5']    ]    ),
            }
            self.stats = {      # current
                **self.stats,

                'current_hp': self.stats['total_hp'],
                'current_mp': self.stats['total_mp'],
            }

            
            pass


        if True:        # self.stats = {nested dicts: DATA, base, bonus, total, current}
            '''
            self.stats = { 
                'DATA': {
                    'cdr':       0,
                    'ap':        0,
                    'crit':      0,
                    'critdmg':   2,
                    'lifesteal': 0,
                    'vamp':      0,
                    'arP':       0,
                    'mP':        0,
                    'hspower':   0,
                    'tenac':     0,
                    **data.data[self.CHAMP.__class__.__name__]
                },
                'base': {
                    'ats': self.DATA['ats'],
                    'ad':  self.DATA['ad']  + self.DATA['ad_lvl']  * self.base_building_multiplier(self.lvl),
                    'ar':  self.DATA['ar']  + self.DATA['ar_lvl']  * self.base_building_multiplier(self.lvl),
                    'mr':  self.DATA['mr']  + self.DATA['mr_lvl']  * self.base_building_multiplier(self.lvl),
                    'hp':  self.DATA['hp']  + self.DATA['hp_lvl']  * self.base_building_multiplier(self.lvl),
                    'mp':  self.DATA['mp']  + self.DATA['mp_lvl']  * self.base_building_multiplier(self.lvl),
                    'hp5': self.DATA['hp5'] + self.DATA['hp5_lvl'] * self.base_building_multiplier(self.lvl),
                    'mp5': self.DATA['mp5'] + self.DATA['mp5_lvl'] * self.base_building_multiplier(self.lvl),
                },
                'bonus': {
                    'ats': [{'lvlbonus': self.DATA['ats_lvl'] * self.base_building_multiplier(self.lvl)}],
                    'ad':  [],
                    'ar':  [],
                    'mr':  [],
                    'hp':  [],
                    'mp':  [],
                    'hp5': [],
                    'mp5': [],
                },
                'total': {
                    'ats': [],
                    'ad':  [],
                    'ar':  [],
                    'mr':  [],
                    'hp':  [],
                    'mp':  [],
                    'hp5': [],
                    'mp5': [],
                },
                'current': {
                    'hp':  [],
                    'mp':  [],
                },
            }
            '''


            pass

        if True:        # simple dicts:     self.DATA, self.base, self.bonus, self.total, self.current
            '''
            self.DATA =  {  
                            'cdr':       0,
                            'ap':        0,
                            'crit':      0,
                            'critdmg':   2,
                            'lifesteal': 0,
                            'vamp':      0,
                            'arP':       0,
                            'mP':        0,
                            'hspower':   0,
                            'tenac':     0,
                            **data.data[self.CHAMP.__class__.__name__]
            }
            self.base =  {
                            'ats': self.DATA['ats'],
                            'ad':  self.DATA['ad']  + self.DATA['ad_lvl']  * self.base_building_multiplier(self.lvl),
                            'ar':  self.DATA['ar']  + self.DATA['ar_lvl']  * self.base_building_multiplier(self.lvl),
                            'mr':  self.DATA['mr']  + self.DATA['mr_lvl']  * self.base_building_multiplier(self.lvl),
                            'hp':  self.DATA['hp']  + self.DATA['hp_lvl']  * self.base_building_multiplier(self.lvl),
                            'mp':  self.DATA['mp']  + self.DATA['mp_lvl']  * self.base_building_multiplier(self.lvl),
                            'hp5': self.DATA['hp5'] + self.DATA['hp5_lvl'] * self.base_building_multiplier(self.lvl),
                            'mp5': self.DATA['mp5'] + self.DATA['mp5_lvl'] * self.base_building_multiplier(self.lvl),
            }
            self.bonuses =  {
                               'ats': [{'lvlbonus': self.DATA['ats_lvl'] * self.base_building_multiplier(self.lvl)}],
                               'ad':  [],
                               'ar':  [],
                               'mr':  [],
                               'hp':  [],
                               'mp':  [],
                               'hp5': [],
                               'mp5': [],
            }
            self.totals =  {
                            'ats': [],
                            'ad':  [],
                            'ar':  [],
                            'mr':  [],
                            'hp':  [],
                            'mp':  [],
                            'hp5': [],
                            'mp5': [],
            }
            self.current =  {
                            'current_hp': [],
                            'current_mp': [],
            }
            '''

            pass

    def base_building_multiplier(self, lvl):
        return (lvl - 1) * (0.685 + 0.0175 * lvl)  


