

from collections import deque


class Client:
    def __init__(self):
        self._lamp = Light()
        self._switch = Switch()
    @property
    def switch(self):
        return self._switch
    def press(self, cmd):
        cmd = cmd.strip().upper()
        if cmd == "ON":
            self._switch.execute(LightOnCmd(self._lamp))
        elif cmd == "OFF":
            self._switch.execute(LightOffCmd(self._lamp))
        else:
            print("Argument 'ON' or 'OFF' is required.")

class Switch:
    """INVOKER"""
    def __init__(self):
        self._history = deque()
    @property
    def history(self):
        return self._history
    def execute(self, command):
        self._history.appendleft(command)
        command.execute()

class Command:
    """interface"""
    def __init__(self, obj):
        self._obj = obj
    def execute(self):
        raise NotImplementedError
class LightOnCmd(Command):
    def execute(self):
        self._obj.turn_on()
class LightOffCmd(Command):
    def execute(self):
        self._obj.turn_off()

class Light:
    """RECEIVER"""
    def turn_on(self):
        print("The light is on")
    def turn_off(self):
        print("The light is off")

# Execute if this file is run as a script and not imported as a module
if __name__ == "__main__":



    client = Client()


    client.press("ON")
    client.press("OFF")
    client.press("****")

    print(client.switch.history)







class Cmd_GiveHeal:
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        receiver.giveHeal()

class Timer:
    def __init__(self, name, length, cmd):
        self.start = t.t
        self.name = name
        self.length = length    #depends on attack speed or other things
        self.cmd = cmd
        self.end = t.t + length
    def __repr__(self):
        return '{}-timer'.format(self.name)
    def go(self):
        t.timers.add(self)
    def stop(self):
        t.timers.discard(self)
    def update_length(self, diff):
        self.length += diff
        self.end += diff
    
    def setCommand(self, cmd):
        self.cmd = cmd
    def execute(self):
        self.cmd.execute()



class Hp5:
    '''receiver'''
    def __init__(self, CHAMP, PARENT, x):
        self.CHAMP  = CHAMP
        self.PARENT = PARENT
        self.heal   = Heal(CHAMP, self, x)
        self.timer  = Timer('hp5', 500, self.giveHeal)
    def giveHeal(self):
        self.heal(self.CHAMP)
        self.CHAMP.takeHeal(self.heal)
