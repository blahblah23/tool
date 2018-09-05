











from globals_ import *





class Effect(KnowsCHAMP, KnowsOWNER):
    def __init__(self, mdmg=None, pdmg=None, tdmg=None, slow=None, **kwargs):
        super().__init__(**kwargs)

        self.mdmg = mdmg
        self.pdmg = pdmg
        self.tdmg = tdmg
        self.slow = slow










