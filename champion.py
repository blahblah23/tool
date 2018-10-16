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
import stats
import regen
import auto

class Champion:
    champID = [0, 2, 3, 4, 5]
    autoclass_map = {'melee': auto.AutoMelee, 'ranged': auto.AutoRanged}

    def __init__(self, lvl, scheme, target=None, **kwargs):
        super().__init__(**kwargs)

        allChamps.append(self)
        self.ID = self.champID.pop(0)
        self.lvl = lvl
        self.target = target
        self.scheme = scheme


        self.shields  = []
        self.pshields = []
        self.mshields = []
        
        self.onhits = []
        self.dmg_reductions= []


        self.STATS          =         stats.Stats(CHAMP=self)
        
        # self.REGEN          =         regen.Regen(CHAMP=self)
        self.ABILITY_USED   =      observer.AbilityUsed() ### this design seems bad


        self.AUTO = self.autoclass_map[self.autoclass](CHAMP = self)
        self.P = self._load_skill('p')
        self.Q = self._load_skill('q')
        self.W = self._load_skill('w')
        self.E = self._load_skill('e')
        self.R = self._load_skill('r')
    def _load_skill(self, skill):
        '''str-skill := p,q,w,e,r'''
        mod = import_module('trial.{}.{}'.format(self.__class__.__name__.lower(), skill))
        return getattr(mod, skill.upper())(CHAMP=self)

    def q(self):
        # other code
        # other code
        # self.abilityUsed()
        self.ABILITY_USED.notify()



    def __str__(self):
        # return '{}{}'.format(self.__class__.__name__, hex(id(self)))
        return '{}{}'.format(self.__class__.__name__, self.ID)
    def __getattr__(self, attr):
        return getattr(self.STATS, attr)






if __name__ == '__main__':
    # ass = Champion(10, 'qweqw')
    # pprint(globals())
    # print(allchamps.zyra.p)
    pass















