



from pprint import pprint
import os
from importlib import import_module
from champ_names import champ_names_for_packages

# class Str:
#     def __str__(self):
#         return '{}{}'.format(self.__class__.__name__, hex(id(self)))
#         return '{}{}'.format(self.__class__.__name__, self.ID)
class SuperInit:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
class KnowsCHAMP:
    def __init__(self, CHAMP, **kwargs):
        super().__init__(**kwargs)
        self.CHAMP = CHAMP
class KnowsOWNER:
    def __init__(self, OWNER, **kwargs):
        super().__init__(**kwargs)
        self.OWNER = OWNER

class ABS_Skill(SuperInit, KnowsCHAMP):
    CASTIME = 250
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        skill = self.__class__.__name__.lower()
        self.lvl = skilvl(skill, self.CHAMP.lvl, self.CHAMP.scheme)
        self.lvlups = self.lvl - 1
    def drop_stack(self):
        pass
class ABS_P(ABS_Skill):
    pass
class ABS_Q(ABS_Skill):
    pass
class ABS_W(ABS_Skill):
    pass
class ABS_E(ABS_Skill):
    pass
class ABS_R(ABS_Skill):
    pass


def skilvl(skill, champlvl, scheme):
    scheme = scheme.lower()
    last   = scheme.replace(scheme[3], '').replace(scheme[4], '')
    lis    = [scheme[0], scheme[1], scheme[2], scheme[3], scheme[3], 'r', scheme[3], scheme[4], 
                scheme[3], scheme[4], 'r', scheme[4], scheme[4], last, last, 'r', last, last]
    lis    = lis[0:champlvl]
    return lis.count(skill.lower())

def skilvlups(skill, champlvl, scheme):
    scheme = scheme.lower()
    last   = scheme.replace(scheme[3], '').replace(scheme[4], '')
    lis    = [scheme[0], scheme[1], scheme[2], scheme[3], scheme[3], 'r', scheme[3], scheme[4], 
                scheme[3], scheme[4], 'r', scheme[4], scheme[4], last, last, 'r', last, last]
    lis    = lis[0:champlvl]
    return lis.count(skill.lower()) - 1

def subscribeThisLater():
    '''item[1]() := iterable of the subjects'''
    for item in toSubscribe:
        for subject in item[1]():
            subject.subscribeObserver(item[0]) 

def getAllChampAbilityUseComponents():
    return [champ.ABILITY_USED for champ in allChamps]

allChamps = []
toSubscribe = []


if __name__ == '__main__':
    # print(   skilvl('r',11,'QWEEW'))
    # print(skilvlups('r',11,'QWEEW'))
    # print(Components.General)
    # print(dir(Components.General))
    print([x.lower() for x in champ_names_word_only])
    pass




