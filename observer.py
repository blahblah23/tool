







class Observer:
    def note(self, event):
        print('From', event)



class Subject:
    def __init__(self):
        super().__init__()
        self.subscribers = []
    def subscribeObserver(self, obs):
        # '''foo([obs1, obs2, obs3....])'''
        # for obs in obsvrs:
        #     obs.subscribers.append(self)
        self.subscribers.append(obs)
    def unsubscribeObserver(self, obs):
        # '''foo([obs1, obs2, obs3....])'''
        # for obs in obsvrs:
        #     obs.subscribers.remove(self)
        self.subscribers.remove(obs)
    def notify(self):
        for obs in self.subscribers:
            obs.note()



class AbilityUsed(Subject):
    pass



























