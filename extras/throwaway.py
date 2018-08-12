

from pprint import pprint





if True: #conways game of life
    # import itertools
    # def neighbors(point):
    #     x, y = point
    #     yield x + 1, y
    #     yield x - 1, y
    #     yield x, y + 1
    #     yield x, y - 1
    #     yield x + 1, y + 1
    #     yield x + 1, y - 1
    #     yield x - 1, y + 1
    #     yield x - 1, y - 1
    # 
    # def advance(board):
    #     newstate = set()
    #     recalc = board | set(itertools.chain(*map(neighbors, board)))
    #     
    #     for point in recalc:
    #         count = sum((neigh in board) for neigh in neighbors(point))
    #         if count == 3 or (count == 2 and point in board):
    #             newstate.add(point)
    #     return newstate
    # 
    # glider = {(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)}
    # 
    # for i in range(1000):
    #     glider = advance(glider)
    #     print(glider)
    
    pass


if True:  # shit  
    # import sys
    # 
    # print(sys.path)
    # print(type(sys.path))
    # print(s)
    
    # class Base:
    #     def __init__(self):
    #         print('base init')
    # 
    # class Class(Base):
    #     
    #     def __init__(self):
    #         super().__init__()
    #         print('child init')
    #         
    #     def foo(self):
    #         print('foo')
    #     
    #     def foi(self):
    #         print('foi')
    #         
    #         
    # me = Class()
    
    # print(me.foo)
    # print(me.foi)E
    # print(me.foo)
    # print(me.foo)
    
    # me.foi()        # same as saying Class.foi(me)
    # me.foo()
    
    # class Basee:
    #     def __init__(self):
    #         print('base init')
    # 
    # class Me(Basee):
    #     def __init__(self):
    #         super().__init__()
    #         print('me init')
    #     
    # 
    # me = Me()
    
    # class basee:
    #     def __init__(self):
    #         pass
    # 
    # class kid(basee):
    #     def __init__(self):
    #         basee.__init__(self)
    
    # class Spam:
    #     def __init__(self):
    #         self.a = self.__class__.values['a']
    #         self.b = self.__class__.values['b']
    #         self.c = self.__class__.values['c']
    #         print(self.a, self.b, self.c)
    # # self.__class__
    # 
    # class Ham(Spam):    
    #     values = {'a': 1,
    #               'b': 2,
    #               'c': 3}    
    #     def __init__(self):
    #         super().__init__()
    #         
    # class Bacon(Spam):    
    #     values = {'a': 4,
    #               'b': 5,
    #               'c': 6}    
    #     def __init__(self):
    #         super().__init__()
    
    # x = Ham()
    # y = Bacon()
    # print(x.a, x.b, x.c)
    # print(y.a, y.b, y.c)

    # spam = 18
    # eggs_keylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # eggs_desired_values = {}
    # eggs_rawdata = {'a'   : 0.65789473684211,
    #           'a_x' : 4,                  
    #           'b'   : 55.88,
    #           'b_x' : 1.66,
    #           'c'   : 19.012,
    #           'c_x' : 3.4,
    #           'd'   : 30,
    #           'd_x' : 0.5,
    #           'e'   : 498.44,
    #           'e_x' : 83,
    #           'f'   : 231.8,
    #           'f_x' : 35,
    #           'g'   : 5.424,
    #           'g_x' : 0.55,
    #           'h'   : 6.972,
    #           'h_x' : 0.4}
    # for x in eggs_keylist:
    #     eggs_desired_values[x] = eggs_rawdata[x] + eggs_rawdata[x + '_x'] * (spam - 1)
    # print(eggs_desired_values)
    
    # spam = 19
    # eggs_keylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # eggs_desired_values = {}
    # eggs_rawdata = {'a'   : 0.65789473684211,
    #                 'a_x' : 4,                  
    #                 'b'   : 55.88,
    #                 'b_x' : 1.66,
    #                 'c'   : 19.012,
    #                 'c_x' : 3.4,
    #                 'd'   : 30,
    #                 'd_x' : 0.5,
    #                 'e'   : 498.44,
    #                 'e_x' : 83,
    #                 'f'   : 231.8,
    #                 'f_x' : 35,
    #                 'g'   : 5.424,
    #                 'g_x' : 0.55,
    #                 'h'   : 6.972,
    #                 'h_x' : 0.4}
    # for x in eggs_keylist:
    #     eggs_desired_values[x] = eggs_rawdata[x] + eggs_rawdata[x + '_x'] * (spam - 1)
    # print(eggs_desired_values)
    
    # tup = (x for x in range(3))
    # 
    # mygenerator = (x*x for x in range(3))
    # print(dir(mygenerator))
    # for i in mygenerator:
    #     print(i)
    # 
    # print(type(mygenerator))
    # print(type(tup))
    # 
    # for i in mygenerator:
    #     print(i + 1)

    # ls = {**{'a': 1}, **{'b': 2}}
    # ls.update({'d': 4, 'e': 5, 'f': 6})
    # print(ls)
    
    # def total():
    #     return base + bons
    # 
    # def scaled_total_bonus():
    #     return total() * 0.4
    # 
    # base = 5
    # bons = 5
    # 
    # bons += scaled_total_bonus()
    # 
    # # total is good here
    # print(total())
    # 
    # bons += 3
    # 
    # # total is bugged here
    # # should be 18.2
    # print(total())
    
    # def scaled_bonus():
    #     return a * 0.4
    # 
    # a = 5
    # 
    # a += scaled_bonus()
    # 
    # # total is good here
    # print(a)
    # 
    # a += 3
    # 
    # # total is bugged here
    # # should be 11.2
    # print(a)
    # 
    # # update with every change to stat?
    # # update every time stat is needed?
    
    # def scaled_bonus():
    #     return a * 0.4
    # 
    # a = 5
    # 
    # a += scaled_bonus()
    # 
    # # total is good here
    # print(a)
    # 
    # a += 3
    # 
    # # total is bugged here
    # # should be 11.2
    # print(a)
    # 
    # # update with every change to stat?
    # update every time stat is needed?
    
    # def total():
    #     return sum(ba + bo)
    # 
    # def scaled_bonus():
    #     return total() * 0.4
    # 
    # ba = [5]
    # bo = [5, 1, 2]
    # 
    # bo.append(scaled_bonus())
    # # total is good here
    # print(total())
    # print(bo)
    # 
    # # bo += 3
    # # total is bugged here
    # print(total())
    
    # a = 50
    # 
    # # b = a * 2
    # 
    # def b():
    #     return a * 2
    # 
    # a = 12
    # 
    # print(b())
    
    # b = {'abc': 124}
    # 
    # print(list(b.values())[0])
    # print(b.values())
    # 
    # a = {'buffStat': {'ad': 123,
    #                   'ats': 123,
    #                   'hp': 123,
    #                   'hp5': 123,}  }
    # 
    # # print(a['buffStat'].values())
    # print(dir(a['buffStat'].values()))
    
    # 
    # a = 3
    # b = [1, 2, b[0] + b[1] + a]
    # 
    # total = a + sum(items in b)
    
    # def foo(stat):
    #     return str(stat)
    # 
    # foo(boobs)
    
    # bufflist = []
    # 
    # def foo():    
    #     if t == 2:
    #         bufflist.extend(['vayne ult', 800])
    #     if t == 802:
    #         bufflist.remove(800)
    #         bufflist.remove('vayne ult')
    # 
    # t = 0
    # 
    # 
    # while t < 10000:    
    #     
    #     if not self.aa_being_delayed: 
    #         aa_timer += 1
    #     
    #     t += 1
    
    #   ::Things To Do::   
    #   
    #   start auto
    #       make sure auto is ready     0
    #           set champ not free
    #           run_A_timer()
    #       
    #       upon reaching windup time   500
    #           apply damage + all other on hit effects to target
    #           set champ free
    #   
    #       upon reaching A_t          1600
    #           reset A_t
    
    #   if somehow your A_t gets reduced below A_timer (through attack speed buff normally)
    #       there needs to be a way to reset A_t since the auto is now ready
    
    # for(var = 0; var < 3; var++){
    #     dostuff();
    # }
    
    # for x in [0, 1, 2]:
    #     dostuff()
    
    # # javascript dictionary aka associative array
    # var x = new Object();
    # x["Key"] = "Value";
    
    # 
    # t_autostart = t
    # set champ status = occupied
    # at t = t_autostart + windup_t
    # at t = t_autostart + auto_t
    
    
    #                   what is an auto attack?....   
    #   every tick:
    #       if auto is prudent:
    #           create a timer at 0
    #           set champ status = occupied
    #       at timer = windup_t, fire auto, set champ status = free
    #       at timer = auto_t, reset timer
    
    # t = 0
    # while t < 1000:
    #     if auto is prudent:
    #         auto()
    #     t += 1
    
    #   0 
    #   500 windup_t
    #   700 receive buff that makes auto_t 600
    
    #   now the timer is above auto_t, we never reach it, it never resets
    #   how to solve this?
    
    #   1600 auto_t, reset time (normally)
    #   
    #       check if timer >= auto_t every tick
    #           reset timer
    
    # alist = [1,2,3,4,5]
    # 
    # 
    # def func():
    #     alist.append(alist[-1] + 1)
    #     print(alist[-1])
    # 
    # 
    # 
    # 
    # for a in alist:
    #     func()
    
    # class Thing:
    #     
    #     # def __repr__(self):
    #     #     return 'a thing'
    #     
    #     # def __str__(self):
    #     #     return '{}'.format(self)
    #     def foo(self):
    #         pass
    # 
    # a_thing = Thing()
    # 
    # 
    # # print(a_thing.__class__.__name__)
    # # print(str(a_thing.foo))
    # # print(Thing.__dict__)
    # print(dir(a_thing.foo))
    
    
    # a = {1: 'a', 2: 'b'}
    # 
    # # for item in a:
    # #     print(a[item])
    # 
    # del a[1]
    # print(a)
    
    
    # ist = {365: 'abc'}
    # 
    # print(ist)
    # 
    # ist[365] += ['def']
    # 
    # print(ist)
    
    
    # make it a list so that i can have multiple functions
    # at one timestamp
    
    # time = 0
    # event = 'event'
    
    # alist = [ [time, event, event, event], [time, event]]
    
    # # time: [event, event, event], time: [event]
    # newdict = {}
    # 
    # for thing in alist:
    #     newdict[thing[0]] = thing[1:]
    
    # print(newdict)
    
    # dic = {'a': 1}
    # 
    # if 'a' in dic.keys():
    #     print('exists')
    
    # class parent:
    #     def __init__(self, **kwargs):
    #         self.lvl = kwargs['first']
    #         print(self.lvl)
    #     def func(self):
    #         return self.func
    # 
    # class child(parent):
    #     def __init__(self, **kwargs):
    #         super().__init__(**kwargs)
    # 
    # 
    # # ch = child(first='fefsef', second='second')
    # 
    # par = parent(first='2')
    # 
    # 
    # a = {'a': [9, 9], 'b': [9, 9]}
    # c = {1, 2}
    # # print({key: [num+1 for num in a[key]] for key in a})
    # # print([num+1 for num in a['a']])
    # #.strip('\'')
    # b = str(a)
    # # print(b)
    # # print([x for x in b])
    # # print(b.replace('\'', ''))
    # 
    # print(a.keys())
    # print(a.keys.__doc__)
    # # print(dir(a))
    # # print(a)
    # print(min())
    
    
    # a = (1,2)
    # b = ['a'] * 3
    # 
    # # print(type(a) == 'tuple')
    # # print(type(a))
    # # print(a.__class__.__name__ == 'tuple')
    # 
    # print(a.__name__)
    
    # def func(one, *args, **kwargs):
    # # def func(*args, one, **kwargs):
    # # def func(*args, one, **kwargs):
    #     print(one)
    #     print(*args)
    #     print(args)
    #     print({**kwargs})
    #     print(kwargs, '\n')
    #     
    # # func(1,4,5,six=6, seven=7)
    # func(*[1,4,5])
    # func(1,4,5, {'six': 6, 'seven': 7})
    # func(1,4,5, **{'six': 6, 'seven': 7})
    # func(1,4,5, **{2, 3})
    
    # print(func.__annotations__)
    # print(dir(func))
    
    
    # dic = {1: }
    # s = '{33.6: [quarry_build({stone: 3}), hunter_build(17)],'
    # 
    # # s.translate()
    # 
    # print(str.translate.__doc__)
    
    # a = []
    # b = [34534]
    
    # if 'a' in a or b:
    #     print('yes')
    
    # def foo(arg):
    #     print(arg)
    #     
    # foo(arg='this')
    # 
    # 
    # a={'abc': 2}
    # 
    # print(a.keys())
    
    # def mult(a, b):
    #     print(a * b)
    # 
    # a = {(23,)}
    # # a = [(23,)]
    # 
    # # print(type(a[0]))
    # a.add(4)
    # a.add(4)
    # print(dir(a))
    # print(a.discard.__doc__)
    # print(a)
    

    
    
    pass
if True:  # get komodo to work
    
    
    # import os
    #                      # os.path.realpath(__file__)
    # path = os.path.dirname(os.path.abspath(__file__))
    # print(os.getcwd())     
    # os.chdir(path)
    
    
    
    
    pass


if True:  # *args **kwargs
    
    # *args
    # inside parameter definition
    #       args initialized to a tuple receiving excess positional parameters
    #       args tuple then can be used inside func definition
    # inside func call argument list
    #       unpacks iterable, passing it's items as positional args
    
    # **kwargs
    # inside parameter definition
    #       kwargs initialized to a dict receiving excess keyword arguments
    #       kwargs dict available inside func def
    # inside func call argument list
    #       unpacks a dict, passes k:v as keyword=arg
    
    # def foo(a=0, b=0, **kwargs):
    #     print(a, b, kwargs['c'])
    # 
    # foo(**{'a': 2, 'b': 3, 'c': 4})

    pass
if True:  # Statemachines
    if True:    # weird one class
        # class StateMachine:
        #     def __init__(self):
        #         self.handlers = {}
        #         self.startState = None
        #         self.endStates = []
        #     def add_state(self, name, handler, end_state=0):
        #         name = name.upper()
        #         self.handlers[name] = handler
        #         if end_state:
        #             self.endStates.append(name)
        #     def set_start(self, name):
        #         self.startState = name.upper()
        #     def run(self, cargo):
        #         handler = self.handlers[self.startState]
        #         while True:
        #             newState, cargo = handler(cargo)
        #             if newState.upper() in self.endStates:
        #                 print("reached ", newState)
        #                 break 
        #             else: handler = self.handlers[newState.upper()]
        # 
        # goods = ["great","super", "fun", "good", "easy"]
        # bads = ["boring", "hard", "ugly", "bad"]
        # 
        # def do_stuff(txt):
        #     splitted_txt = txt.split(None,1)
        #     return splitted_txt if len(splitted_txt) > 1 else (txt,"")
        # def start_transitions(txt):
        #     word, txt = do_stuff(txt)
        #     if word == "Python":    newState = "Python_state"
        #     else:                   newState = "error_state"
        #     return (newState, txt)
        # def python_state_transitions(txt):
        #     word, txt = do_stuff(txt)
        #     if word == "is":    newState = "is_state"
        #     else:               newState = "error_state"
        #     return (newState, txt)
        # def is_state_transitions(txt):
        #     word, txt = do_stuff(txt)
        #     if word == "not":       newState = "not_state"
        #     elif word in goods:     newState = "pos_state"
        #     elif word in bads:      newState = "neg_state"
        #     else:                   newState = "error_state"
        #     return (newState, txt)
        # def not_state_transitions(txt):
        #     word, txt = do_stuff(txt)
        #     if word in goods:   newState = "neg_state"
        #     elif word in bads:  newState = "pos_state"
        #     else:               newState = "error_state"
        #     return (newState, txt)    
        # if True:
        #     m = StateMachine()
        #     m.add_state("Start", start_transitions)
        #     m.add_state("Python_state", python_state_transitions)
        #     m.add_state("is_state", is_state_transitions)
        #     m.add_state("not_state", not_state_transitions)
        #     m.add_state("neg_state", None, end_state=1)
        #     m.add_state("pos_state", None, end_state=1)
        #     m.add_state("error_state", None, end_state=1)
        #     m.set_start("Start")
        #     m.run("Python is great")
        #     m.run("Python is hard")
        #     m.run("Perl is ugly")        
        # 
        pass
    if True:    # 4 classes
        # class State:
        #     def __str__(self):
        #         return self.__class__.__name__
        # class LockedState(State):
        #     def on_event(self, event):
        #         if event == 'unlocking':  return UnlockedState()        
        #         return self
        # class UnlockedState(State):
        #     def on_event(self, event):
        #         if event == 'locking': return LockedState()
        #         return self
        # class SimpleDevice:
        #     def __init__(self):
        #         self.state = LockedState()
        #         print('startstate =', self.state)
        #     def on_event(self, event):
        #         print('input =', event)
        #         self.state = self.state.on_event(event)
        #         print('state =', self.state)
        #         
        # device = SimpleDevice()        
        # device.on_event('locking')
        # device.on_event('unlocking')
        # print(device.state)
        
        print()
        
        
        
        pass
    if True:    # https://www.youtube.com/watch?v=E45v2dD3IQU&t=473s
        # from random import randint
        # from time import clock
        # class LightOn:
        #     def execute(self):
        #         print('light is on')        
        # class LightOff:
        #     def execute(self):
        #         print('light is off')        
        # class Transition:
        #     def __init__(self, to_state):
        #         self.to_state = to_state                
        #     def execute(self):
        #         print('transitioning...' + self.to_state) 
        # class SimpleFSM:
        #     def __init__(self, owner):
        #         self.owner = owner
        #         self.states = {'on': LightOn(), 'off': LightOff()}
        #         self.transitions = {}
        #         self.cur_state = None
        #         self.trans = None
        #     def set_state(self, state_name):
        #         self.cur_state = self.states[state_name]
        #     def transition(self, trans_name):
        #         self.trans = self.transitions[trans_name]
        #     def execute(self):
        #         if (self.trans):
        #             self.trans.execute()
        #             self.set_state(self.trans.to_state)
        #             self.trans = None
        #         self.cur_state.execute()
        # class Char:
        #     def __init__(self):
        #         self.FSM = SimpleFSM(self)
        #         self.light_on = True        
        # if __name__ == '__main__':            
        #     if True:        # instantiation
        #         light = Char()
        #         light.FSM.transitions['toon'] = Transition('on')
        #         light.FSM.transitions['tooff'] = Transition('off')
        #         light.FSM.set_state('on')
        #         pass           
        #     for i in range(5):
        #         start_time = clock()
        #         time_interval = 1
        #         if (randint(0,2)):
        #             if (light.light_on):
        #                 light.FSM.transition('tooff')
        #                 light.light_on = False
        #             else:
        #                 light.FSM.transition('toon')
        #                 light.light_on = True
        #         light.FSM.execute()
        #     print(light.FSM.states)
        # 
        # 
        
        
        pass
    pass
if True:  # loose vs tight coupling shown with and without observer pattern
    # class Sound:
    #     def note__jump(self):
    #         self.playsound()
    #     def playsound(self):
    #         pass        
    # class Mario:
    #     def __init__(self):
    #         self.obsvrs = [sound]
    #     def jump(self):
    #         self.notify__jump()
    #     def notify__jump(self):
    #         for obs in self.obsvrs:
    #             obs.note__jump()    
    # sound = Sound()
    # 
    # 
    # 
    # class Sound:
    #     def playsound(self):
    #         pass
    # class Mario:
    #     def jump(self):
    #         sound.playsound()        
    # sound = Sound()
    
    
    
    
    
    pass
if True:  # loose vs tight coupling using an interface
    # 
    # import serial
    # class PlatformConnect:
    #     def serial_connect(self):
    #         self.ser = serial.Serial()
    #     def serial_disconnect(self):
    #         self.ser.close()
    # platform = PlatformConnect()
    # 
    # 
    # 
    # import serial
    # class PlatformConnect:
    #     def __init__(self, s2p):
    #         self._s2p = s2p
    # class S2P:
    #     def serial_connect(self):
    #         self.ser = serial.Serial()
    #     def serial_disconnect(self):
    #         self.ser.close()
    #     def readline(self):
    #         return self.ser.readline()
    #     def write(self, data):
    #         self.ser.write(data=data)
    # def factory_PlatformConnect():
    #     return PlatformConnect(S2P())
    # platform = factory_PlatformConnect()
    
    
    pass
if True:  # command pattern
    
    # def greet(z):
    #     print("Hello", z)
    # 
    # # pass the callable around, and invoke it later
    # greet_command = lambda: greet("World")
    # greet_command()
    # 
    # # The command pattern as an oo-design 
    # # pattern makes more sense if your commands need 
    # # to be able to do more than just be invoked. 
    # # Common usecase is when you need to be able to 
    # # undo/redo your actions. Then a command class is 
    # # a good way to couple the forward and backwards                     
    # # actions together. For example:
    # 
    # class MoveFileCommand:
    #     def __init__(self, src, dest):
    #         self.src = src
    #         self.dest = dest
    #         os.rename(self.src, self.dest)
    #     def undo(self):
    #         os.rename(self.dest, self.src)
    # 
    # undo_stack = []
    # undo_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    # undo_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))
    # # foo.txt is now renamed to baz.txt
    # undo_stack.pop().undo() # Now it's bar.txt
    # undo_stack.pop().undo() # and back to foo.txt
        
    
    
    pass
if True:  # __getattr__ for blending line between composition and inheritance
    
    # class Ex:
    #     def foo(self):
    #         print('foo', self)
    
    # class Composed:
    #     def __init__(self):
    #         self.component = Ex()
    
    #     def __getattr__(self, attr):
    #         '''this is called when an attribute or
    #         method isn't found on this class;
    #         so delegate the right place to look'''
    #         return getattr(self.component, attr)
    #         # print('dont have attribute')
    
    # c = Composed()
    # c.foo()
    
    # print(dir(Composed))
    # print(Composed.__init_subclass__.__doc__)
    
    
    
    
    
    pass
if True:  # observer stuff
    # class Observer:
    #     def __init__(self, event):
    #         self.reg(event)
    #     def reg(self, *args):
    #         for listt in args:
    #             listt.observers.append(self)
    #     def note(self, event, arg):
    #         print('Got', arg, 'From', event)
    # class Event:
    #     def __init__(self):
    #         self.observers = []
    #     def notify(self, arg):
    #         for item in self.observers:
    #             item.note(self, arg)
    # event = Event()
    # item = Observer(event)
    # event.notify('@@@@')
    
    # class Caller:
    #     
    #     def call_to_item(self, string, item):
    #         item.got_call(self, string)
    # 
    # class X:
    # 
    #     def got_call(self, caller, string):
    #         print('Got', string, 'From', caller)
    # 
    # 
    # caller = Caller()
    # x = X()
    # 
    # 
    # caller.call_to_item('test', x)
    
    
    # class Caller:
    #     
    #     def call_to_item(self, item):
    #         item.got_call()
    # 
    # class X:
    # 
    #     def got_call(self):
    #         print('Got it')
    # 
    # 
    # caller = Caller()
    # x = X()
    # caller.call_to_item(x)
    
    
    pass
if True:  # observer stuff
    # class Event:
    #     pass
    
    # # class Observable:
    #     def __init__(self):
    #         self.list = []
    #     def subscribe(self, item):
    #         self.list.append(item)
    #     def fire(self, **kwargs):
    #         event = Event()
    #         event.sourcevent = self
    #         for k, v in kwargs.iteritems():
    #             event.k = v
    #         for x in self.list:
    #             x(event)

    # Your Job class can subclass Observable. When something of interest happens, call self.fire(type="progress", percent=50) or the like.
    
    
    pass
if True:  # observer stuff
    # class Observer:
    #     listt = []
    #     def __init__(self):
    #         self.listt.append(self)
    #         self.observables = {}
    #     def observe(self, event_name, callback):
    #         self.observables[event_name] = callback
    # class Event:
    #     def __init__(self, name, data):
    #         self.listt = []
    #         self.name = name
    #         self.data = data
    #     def fire(self):
    #         for o in self.listt:
    #             if self.name in o.observables:
    #                 o.observables[self.name](self.data)  
    # class Room(Observer):    
    #     def __init__(self):
    #         super().__init__()
    #     def someone_arrived(self, who):
    #         print(who + ' has arrived')
    # ev = Event('someone arrived', 'Lenard')
    # room = Room()
    # room.observe('someone arrived',  room.someone_arrived)
    # ev.fire()
    
    pass
if True:  # my observer
    # class Event:
    #     def __init__(self, name, data):
    #         self.name = name
    #         self.data = data
    #         self.notify()
    #     def notify(self):
    #         for o in listt:
    #             o.note()
    # class Obs:
    #     def reg(self, *args):
    #         for listt in args:
    #             listt.observers.append(self)
    
    pass
if True:  # encode, decode
    

    # str is text representation in bytes, unicode is text representation in characters.

    # You decode text from bytes to unicode and encode a unicode into bytes with some encoding.

    # That is:

    # >>> 'abc'.decode('utf-8')  # str to unicode
    # u'abc'
    # >>> u'abc'.encode('utf-8') # unicode to str
    # 'abc' 

    pass
if True:  # regex snippets
    
    #               .       - Any Character Except New Line
    #               \d      - Digit (0-9)
    #               \D      - Not a Digit (0-9)
    #               \w      - Word Character (a-z, A-Z, 0-9, _)
    #               \W      - Not a Word Character
    #               \s      - Whitespace (space, tab, newline)
    #               \S      - Not Whitespace (space, tab, newline)
    #               
    #               \b      - Word Boundary
    #               \B      - Not a Word Boundary
    #               ^       - Beginning of a String
    #               $       - End of a String
    #               
    #               []      - Matches Characters in brackets
    #               [^ ]    - Matches Characters NOT in brackets
    #               |       - Either Or
    #               ( )     - Group
    #               
    #               Quantifiers:
    #               *       - 0 or More
    #               +       - 1 or More
    #               ?       - 0 or One
    #               {3}     - Exact Number
    #               {3,}    - 3 or more
    #               {3,4}   - Range of Numbers (Minimum, Maximum)
    #               
    #               
    #               #### Sample Regexs ####
    #               
    #               [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

    pass
if True:  # regex example

    # import re
    # emails = '''
    # CoreyMSchafer@gmail.com
    # corey.schafer@university.edu
    # corey-321-schafer@my-work.net
    # '''
    # pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    # matches = pattern.finditer(emails)
    # for match in matches:
    #     print(match)

    pass
if True:  # regex match.group() example
    # import re
    # urls = '''
    # https://www.google.com
    # http://coreyms.com
    # https://youtube.com
    # https://www.nasa.gov
    # '''
    # pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    # # subbed_urls = pattern.sub(r'\2\3', urls)
    # # print(subbed_urls)
    # matches = pattern.finditer(urls)
    # for match in matches:
    #     print(match.group(0))
        
    pass
if True:  # popular champs
    
    #   Alistar
    #   Blitzcrank
    #   Braum
    #   Caitlyn
    #   Camille
    #   Darius
    #   Ezreal
    #   Fiora
    #   Gangplank
    #   Janna
    #   Jarvan IV
    #   Jax
    #   Jhin
    #   Jinx
    #   Kai'Sa
    #   Kassadin
    #   Kha'Zix
    #   Lee Sin
    #   Lulu
    #   Morgana
    #   Nami
    #   Rakan
    #   Sejuani
    #   Sion
    #   Soraka
    #   Swain
    #   Thresh
    #   Tristana
    #   Twisted Fate
    #   Varus
    #   Vayne
    #   Xayah
    #   Yasuo
    #   Zac

    
    
    pass
if True:  # cam move settings
    #   MapScrollSpeed:
    #  4294967295	-0.0100 
    #  4294967286	-0.1000 faster than champ
    #  4294967284	-0.1200 same as champ
    #  4294967282	-0.1400 slower than champ
    #  4294967276	-0.2000 makes cam reverse, slower than champ
    #  4294967246	-0.5000 makes cam reverse
    
    pass
if True:  # formatted output

    #   {0} access first arg
    #   {1} access second arg
    #   {2} access third arg
    #   ...
    #   
    #   index can be followed by a colon.....{0:5d} 
    #   
    #   first num after colon sets space for field {:5} means 5 spaces
    #   
    #   '{} {} {}' == '{0} {1} {2}'
    #   
    #   '<' 	 left-aligned in available space. usually default for strings.
    #   '>' 	right-aligned in available space.       default for numbers.
    #   '^' 	     centered in available space.
    #   '0' 	If width field is preceded by zero, sign-aware zero-padding for numeric types will be enabled.
    #   ',' 	signals use of comma for thousands separator:  1,000,000
    #   '=' 	Forces the padding to be placed after the sign (if any) but before the digits.
    #   

    # print('{:7,}{:^10}{}'.format(0, 'Lux', 'stun_cast'))
    # print('{:7,}{:^10}{}'.format(1000, 'Vayne', 'stun_cast'))
    # print('{:7,}{:^10}{}'.format(1000, 'Lux', 'stun_cast_aseoiashgsefspef'))

    # print('{}{}{}'.format(0, 'Lux', 'stun_cast'))
    # print('{}{}{}'.format(1000, 'Vayne', 'stun_cast'))
    # print('{}{}{}'.format(1000, 'Lux', 'stun_cast_aseoiashgsefspef'))

    pass
if True:  # @decorator syntx sugar


    # ##########################
    # @decorator
    # def foo(self): 
    #     return self._foo
    # ##########################
    # # is syntactic sugar, the same as:
    # ##########################
    # def foo(self): 
    #     return self._foo
    # foo = decorator(foo)
    # ##########################

    # def decorator(foo):
    #     def wrapper():
    #         print("blah")
    #         foo()
    #         print("blah.")
    #     return wrapper

    # def foo():
    #     print("foo")

    # foo = decorator(foo)
    # foo()


    pass
if True:  # descriptors and property() de-mystified


    # @property uses same syntax sugar as any decorator   
    class Eggs:
        def __init__(self,x):
            self.x = x

        @property
        def x(self):
            return self._x

        @x.setter
        def x(self, x):
            '''sefsekofe'''
            if x < 0: self._x = 0
            else:     self._x = x
    
    eggs = Eggs(1001)
    # pprint(dir(eggs))
    # pprint(dir(Eggs))
    pprint(dir(Eggs.x))
    pprint(Eggs.x.fset.__doc__)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass

if True:  # super() experiment

    
    # class A:
    #     def __init__(self):
    #         print('A init')
    #         super().__init__()
    
    # class B:
    #     def __init__(self):
    #         print('B init')
    #         super().__init__()

    # class C(B,A):
    #     def __init__(self):
    #         print('C init')
    #         super().__init__()
    #     pass

    # c = C()
    # # b = A()

    # # print(A.__mro__)
    # # print(B.__mro__)
    # # print(C.__mro__)








    pass



'''python
def __set__(self, obj, value):
    if self.hitpoints_attr <= 0:
        self.obj.die()
    self.value = value
'''


