











from globals_ import *
import observer
import stats
import effecthandler

class Champion:
    def __init__(self, lvl, scheme, tgt=None, **kwargs):
        super().__init__(**kwargs)

        allChamps.append(self)

        self.lvl = lvl
        self.tgt = tgt
        self.scheme = scheme

        self.EFFECT_HANDLER = effecthandler.EffectHandler(CHAMP=self)
        self.ABILITY_USED   =      observer.AbilityUsed() ### this design seems bad
        self.STATS          =         stats.Stats(CHAMP=self)

        self.P = self._load_skill('p')
        self.Q = self._load_skill('q')
        self.W = self._load_skill('w')
        self.E = self._load_skill('e')
        self.R = self._load_skill('r')

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
    def _load_skill(self, skill):
        '''str-skill := p,q,w,e,r'''
        mod = import_module('trial.{}.{}'.format(self.__class__.__name__.lower(), skill))
        return getattr(mod, skill.upper())(CHAMP=self)
    
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






