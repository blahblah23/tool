


# owner.summCDR = 0.7

def foo():
    

class Barrier:
    DURA   =   2000
    CDWN   =   180000
    def __init__(self, owner):
        self.i_dura =   ['{} BARRIER DURA',    self.DURA,                self.end_buff]
        self.i_CD   =   ['{} BARRIER COOLD',   self.CDWN*owner.sumCDR,   self.set_rdy, True]
        self.owner  =   owner
        self.c_shield =   Shield(self,   95+20*owner.lvl,   self.i_dura)
        self.c_cd     =   Timer(*i_CD)
        self.rdy    =   True
        
    def set_rdy(self, boolean):
        self.rdy = boolean
        
    def go(self):
        self.shield.go(self.owner)
        self.cd.go()
        self.rdy = False

    def end_buff(self):
        self.owner.shields.remove(self.shield)
        self.shield.end()
        
        
    
cooldown
shield
value formula: 95+20*lvl
duration
apply function
remove function
owner
notify


self-target only





























