






from globals_ import *
# from globs import pprint
import trial.kassadin.kassadin

Kassadin = trial.kassadin.kassadin.Kassadin


kassadin = champ1 = Kassadin(lvl=11, scheme='qweqw')
kassadin2 = champ2 = Kassadin(lvl=8, scheme='qweeq')
champ1.tgt = champ2
champ2.tgt = champ1

subscribeThisLater()

print(kassadin.E.STACKER.counter)
print(kassadin2.E.STACKER.counter)

kassadin.q()
kassadin2.q()
kassadin2.q()
# kassadin2.E.cast()

print(kassadin.E.STACKER.counter)
print(kassadin2.E.STACKER.counter)

# print(kassadin.P)

# pprint(kassadin.STATS)
# for t in kassadin.STATS.stats.items():
#     print(t)
# pprint(kassadin.E.get_mdmg().__dict__)

pprint(kassadin2.STATS.stats['current_hp'])
for __ in range(12):
    kassadin.E.cast()

# pprint(kassadin2.EFFECT_HANDLER.CHAMP)
# pprint(kassadin2.EFFECT_HANDLER)
pprint(kassadin2.STATS.stats['current_hp'])



