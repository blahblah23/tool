







def foo():
    print('foo')
def handle_time(*args):
    Timer(*args)


class StateMachine:
    def __init__(self):
        self.state = [Idle()]
        # self.states = [Idle, Casting, Stunned, Silenced]
        pass
    def change(self, new):
        '''new === New(args)'''
        new.change(self)
class State:
    def change(self, SM):
        '''StateMachine delegates here'''
        for state in SM.state:
            if state prevents self: break
            either delete or keep it
                
        
        
class Idle(State):
    def __init__(self):
        self.permissable = [Casting, Stunned, Silenced]
class Casting(State):
    def __init__(self):
        self.permissable = [Idle, Stunned, Silenced]
class Stunned(State):
    def __init__(self, length=1000):
        self.length = length
        self.permissable = [Idle, Casting, Silenced]
class Silenced(State):
    def __init__(self):
        self.permissable = [Idle, Casting, Stunned]
class Stasis(State):
    def __init__(self):
        self.permissable = []

class Test:
    def __init__(self):
        # print(dir(Test))
        print(Test.__dict__)
# test = Test()

SM = StateMachine()
print(SM.state)
SM.change(Stunned())
print(SM.state)
# print(SM.state[0].length)




print(dir([]))
























