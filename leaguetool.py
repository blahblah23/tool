






from globals_ import *
# from globs import pprint

# import trial.kassadin.kassadin
from trial.kassadin.kassadin import Kassadin 
# Kassadin = trial.kassadin.kassadin.Kassadin

import helpers
import bonustat
import time_


time = time_.Time()

kassadin0 = champ1 = Kassadin(lvl=11, scheme='qweqw')
kassadin2 = champ2 = Kassadin(lvl=8, scheme='qweeq')
champ1.target = champ2
champ2.target = champ1

subscribeThisLater()

# print(kassadin0.base_ats)
# print(kassadin0.bonus_ats)
# print(kassadin0.total_ats)
print(kassadin2.current_hp)

time_.Timer(['TEMP-cast', 'kassadin0.E'], 
            200, 
            kassadin0.W.cast
            # kassadin0.AUTO.cast
            ).go()
time_.Timer(['TEMP-auto', 'kassadin0.E'], 
            1000, 
            kassadin0.AUTO.cast
            ).go()
time.go()


# time.printall()

print(kassadin2.current_hp)



############
# TODO using @classmethod allows to call a method without needing an instance 
############





# print(kassadin.E.STACKER.counter)
# print(kassadin2.E.STACKER.counter)

# kassadin.Q.cast()
# pprint(kassadin2.current_hp)
# kassadin2.Q.cast()
# kassadin2.q()

# kassadin2.q()
# kassadin2.q()
# kassadin2.q()

# kassadin2.q()


# print(kassadin.E.STACKER.counter)
# print(kassadin2.E.STACKER.counter)



# pprint(kassadin2.current_hp)


# kassadin.bonus_ad.append(bonustat.Bonus('testbonus', 10))
# print('kassadin.ad:', 53.544  + 3.3  * helpers.bbm(11))
# print('kassadin.total_ad:', kassadin.total_ad)


# for __ in range(12):
#     kassadin.E.cast()


# pprint(kassadin2.current_hp)
# pprint(kassadin2.current_mp)














