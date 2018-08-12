








class Hp5:
    def __init__(self, CHAMP, PARENT, x):
        self.CHAMP  = CHAMP
        self.PARENT = PARENT
        self.heal   = Heal(CHAMP, self, x)
        self.timer  = Timer('hp5', 500, self.giveHeal)
    def giveHeal(self):
        self.heal(self.CHAMP)
        self.CHAMP.takeHeal(self.heal)




class Mp5:
    def __init__(self, CHAMP, PARENT, x):
        self.CHAMP  = CHAMP
        self.PARENT = PARENT
        self.x      = x
        self.timer  = Timer('mp5', 500, self.giveHeal)














