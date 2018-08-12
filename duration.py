



name, length, 


class Duration:
    def __init__(self, timerclass, owner, timerinfo):
        self.owner = owner
        self.timer = timerclass(timerinfo[0], timerinfo[1], self.end)
    def start(self):
        self.timer.begin()
    def end(self):
        self.owner.end()
    def refresh(self):
        self.timer.refresh()
        


timer
start
refresh
end
reduce
extend
notify
































