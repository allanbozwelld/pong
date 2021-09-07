from event.events import Quit, Tick, EventManager, Initialization


class Model(object):
    def __init__(self, manager: EventManager):
        self.running: bool = False
        self.manager: EventManager = manager

        manager.register(event=self)

    def run(self):
        self.running: bool = True
        self.manager.post(event=Initialization())

        while self.running:
            self.manager.post(event=Tick())

    def notify(self, event: object):
        if isinstance(event, Quit):
            self.running: bool = False
