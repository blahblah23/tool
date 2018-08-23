






from globals_ import *
# from globs import pprint
import trial.kassadin.kassadin
import helpers
import bonustat

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

print(kassadin.E.STACKER.counter)
print(kassadin2.E.STACKER.counter)



pprint(kassadin2.current_hp)


kassadin.bonus_ad.append(bonustat.Bonus('testbonus', 10))
print('kassadin.ad:', 53.544  + 3.3  * helpers.bbm(11))
print('kassadin.total_ad:', kassadin.total_ad)


for __ in range(12):
    kassadin.E.cast()


pprint(kassadin2.current_hp)

