







from globals_ import *
import dmgheal

class P(ABS_P):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.dmg_reduction = dmgheal.DmgReduction(CHAMP = self.CHAMP,
                                                  OWNER = self,
                                                  amount = 0.85,
                                                  tags = {'magic'})

        self.CHAMP.dmg_reductions.append(self.dmg_reduction)


# P
# innate: self is permanently ghosted and takes 15% reduced mDmg.

# tgting         passive
# affects        self


