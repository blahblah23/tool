






# class ShieldClass:
#     def __init__(self, owner, size):
#         self.owner = owner
#         self.size = size
# 
#     def activate(self, target):
#         target.shields.append(Shield())
#         pass
        
class Shield:
    def __init__(self, owner, size, duration):
        self.owner = owner
        self.size = size
        self.timer = Timer()
        
    def go(self, target):
        target.shields.append(self)
        self.timer.go()


take dmg
activate
resolve



































