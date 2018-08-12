





# components============================================


# class Suppress:
#     def apply():
#         block_move(target)
#         block_attack(target)
#         ...
#     
# 
# 
# def block_attack():
#     self.can_attack = False
#     
# def interupt_attack(target):
#     target.


class Champ:
    pass
class Malzahar(Champ):
    def __init__(self):
        self.target = 'vayne'
        self.r = R(self)
class R:
    def __init__(self, owner):
        self.owner = owner
        self.suppress = Suppress(owner)    # ult has a suppress component
    def apply(self):
        self.suppress.apply()
class Suppress:
    def __init__(self, owner):
        self.owner = owner
        self.block_move = BlockMove(owner)
    def apply():
        self.block_move.apply()
class BlockMove:
    ''''''
    def __init__(self, owner):
        self.owner = owner
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass

class Init:
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
        self.init()

m = Malzahar()
m.r.foo()





class Champ:
    pass
class Malzahar(Champ):
    def __init__(self):
        self.target = 'vayne'
        self.r = R(self)
class R:
    def __init__(self, owner):
        self.owner = owner
        self.suppress = Suppress(owner)    # ult has a suppress component
    def apply(self):
        self.suppress.apply()
class Suppress:
    def __init__(self, owner):
        self.owner = owner
        self.block_move = BlockMove(owner)
    def apply():
        self.block_move.apply()
def BlockMove:
    ''''''
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass

m = Malzahar()
m.r.foo()








class Champ:
    def __init__(self):
        self.blockmove = []
        self.blockattack = []
        self.blockability = []
        self.blocksumm = []
        self.blockitem = []
class Malzahar(Champ):
    def __init__(self):
        self.target = 'vayne'
        self.r = R(self)
class R(Init):
    def init(self):
        self.suppress = Suppress(owner)    # ult has a suppress component
    def apply(self):
        self.suppress.apply()
class Suppress(Init):
    def init(self):
        self.block_move = BlockMove(owner)
    def apply():
        self.block_move.apply()
class BlockMove(Init):
    ''''''
    def init(self):
        pass
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class BlockAttack(Init):
    ''''''
    def init(self):
        pass
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class BlockAbility(Init):
    ''''''
    def init(self):
        pass
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class BlockSumm(Init):
    ''''''
    def init(self):
        pass
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class BlockItem(Init):
    ''''''
    def init(self):
        pass
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class InterruptChannelled(Init):
    ''''''
    def init(self):
        pass
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class InterruptCharged(Init):
    ''''''
    def init(self):
        pass
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass

class Init:
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
        self.init()

m = Malzahar()
m.r.foo()







class Champ:
    pass
class Malzahar(Champ):
    def __init__(self):
        self.target = 'vayne'
        self.r = R(self, self.target)
class R:
    def init(self, owner, target):
        self.owner = owner
        self.target = target
        self.suppress = Suppress(owner)    # ult has a suppress component
    def apply(self):
        self.suppress.apply()
class Suppress:
    def init(self, owner, target):
        self.owner = owner
        self.target = target
        self.block_move = BlockMove(owner)
    def apply():
        self.block_move.apply()
class BlockMove:
    ''''''
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class BlockAttack:
    ''''''
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class BlockAbility:
    ''''''
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class BlockSumm:
    ''''''
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class BlockItem:
    ''''''
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class InterruptChannelled:
    ''''''
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass
class InterruptCharged:
    ''''''
    def __init__(self, owner, target):
        self.owner = owner
        self.target = target
    def apply(self):
        #make self.owner.target unable to move
        pass
    def remove(self):
        pass


m = Malzahar()
m.r.foo()








