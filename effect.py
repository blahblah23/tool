











from globals_ import *





class Effect(KnowsCHAMP, KnowsOWNER):
    def __init__(self, dmg, slow, **kwargs):
        super().__init__(**kwargs)

        self.dmg = dmg
        self.slow = slow










