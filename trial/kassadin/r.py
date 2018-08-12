



from globals_ import *


class R(ABS_R):
    pass



# R

# tgt range: 500 
# rad: 150 
# cost: 50 / 100 / 200 / 400 / 800 mana 
# cd: '6+-2.0&3' 

# active: after small delay, self blinks to tgt location, do mDmg all to nearby ems on arrival.

# mDmg: '80+20.0&3' (+ 30% ap) (+ 2% max mana)
# each subsequent R in 15 s doubles its mana cost and incrs its dmg, stacking up to 4 times.

# ++ dmg per stack: '40+10.0&3' (+ 10% ap) (+ 1% max mana)max mDmg: '240+60.0&3' (+ 70% ap) (+ 6% max mana)

# tgting         ground
# affects        ems
# dmg            mag

# type           aoe
# sShield        blocked
# grounded       disabled

# knockdown      unstoppable


